from dataclasses import dataclass, replace, field
from pathlib import Path
from uuid import uuid4

from hellsicht.kernel.types.analysis import Analysis


@dataclass(frozen=True)
class Project:
    """
    Represents a project.

    Attributes:
        name (str): The name of the project.
        project_directory (Path): The directory of the project.
        analysis_results (set[AnalysisResult]): The set of analyzed files for the project.

    """
    name: str
    project_directory: Path
    analysis_results: set[Analysis] = field(default_factory=set)



def create_new_analysis_skeleton(project: Project) -> Analysis:
    """
    Create a new analysis skeleton for the given project.

    Args:
        project (Project): The project for which to create the analysis skeleton.

    Returns:
        Analysis: The newly created analysis object.

    Example:
        project = Project()
        analysis = create_new_analysis_skeleton(project)
    """
    name: str = str(uuid4())
    path: Path = project.project_directory.joinpath(f'{name}.analysis')
    path.mkdir(parents=True)
    return Analysis(name, path, path.joinpath('progress.json'))


def add_analysis_result(project: Project, *results: Analysis) -> Project:
    """
    Args:
        project: A Project object representing the project to which analysis results should be added.
        *results: A variable number of AnalysisResult objects representing the analysis results to be added to the project.

    Returns:
        A Project object with the provided analysis results added to its existing analysis results.

    """
    return replace(project, analysis_results=project.analysis_results.union(results))
