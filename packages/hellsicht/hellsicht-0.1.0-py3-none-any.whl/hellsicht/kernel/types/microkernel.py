from collections.abc import Sequence
from concurrent.futures import ProcessPoolExecutor, Future
from dataclasses import dataclass, replace, field
from pathlib import Path
from typing import Any

from hellsicht.kernel.types.analysis import Analysis, AnalysisSource, AnalysisResult
from hellsicht.kernel.types.job import Job
from hellsicht.kernel.types.project import Project, add_analysis_result, create_new_analysis_skeleton
from hellsicht.servers.internal.preprocessing.tabular import preprocess_tabular_file
from hellsicht.servers.internal.types import ServiceRequest, ParameterType, InternalServer


@dataclass(frozen=True)
class Microkernel:
    """
    Class Microkernel represents the core component of a system that is responsible for orchestration and execution of
    jobs within a project.

    Attributes:
        project (Project): The project that the microkernel is associated with.
        executor (ProcessPoolExecutor): The executor used for running jobs. Default value is a new ProcessPoolExecutor.
        running_jobs (set[Job]): A set of currently running jobs within the microkernel. Default value is an empty set.

    """
    project: Project
    executor: ProcessPoolExecutor = field(default_factory=ProcessPoolExecutor)
    running_jobs: set[Job] = field(default_factory=set)


def get_server_by_name(kernel: Microkernel, name: str) -> InternalServer[Any, Any]:
    if name == 'tabular':
        return preprocess_tabular_file
    raise NameError(name)


def analyse_data_with_internal_server(
        kernel: Microkernel,
        parameter: ParameterType,
        on: AnalysisSource | None,
        to: AnalysisResult,
        server: str) -> Microkernel:
    """
    Args:
        kernel: The Microkernel object representing the target microkernel.
        parameter: The ParameterType object containing the input parameters for analysis.
        on: The Analysis object that is the base of the new analysis or None if the analysis is not based on a prior
            analysis.
        to: Analysis object to store analysis results to.
        server: The string representing the name of the internal server to use for analysis.

    Returns:
        Microkernel: The modified Microkernel object with the new running job added.

    """
    result: AnalysisResult = AnalysisResult(create_new_analysis_skeleton(kernel.project))
    log_file: Path = result._analysis.path.joinpath('internal.log')
    request: ServiceRequest[ParameterType] = ServiceRequest(on, to, parameter, log_file)
    server_func: InternalServer[ParameterType, Any] = get_server_by_name(kernel, server)
    future: Future = kernel.executor.submit(server_func, request)
    job: Job[ParameterType, Any] = Job(future, request, server_func)
    return replace(kernel, running_jobs=kernel.running_jobs.union({job}))


def analysis_result_from_job(job: Job) -> Analysis:
    """
    Args:
        job: The job object containing the necessary information for analysis.

    Returns:
        AnalysisResult: The analysis result object containing the analysis outcome.

    Example usage:
        job = Job(...)
        result = analysis_result_from_job(job)
        print(result)
    """
    return job.request.result_analysis.analysis


def wait_for_jobs(kernel: Microkernel) -> Microkernel:
    """
    Waits for all running jobs in the microkernel to complete.

    Args:
        kernel (Microkernel): The microkernel object.

    Returns:
        Microkernel: The updated microkernel object after all jobs have completed.
    """
    completed_jobs = set()
    for job in kernel.running_jobs:
        if job.process.done():
            completed_jobs.add(job)
    return replace(
        kernel,
        project=add_analysis_result(kernel.project, *map(analysis_result_from_job, completed_jobs)),
        running_jobs=kernel.running_jobs - completed_jobs
    )
