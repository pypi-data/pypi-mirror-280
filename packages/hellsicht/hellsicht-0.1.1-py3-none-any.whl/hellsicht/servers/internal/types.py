from dataclasses import dataclass, field
from datetime import datetime
from functools import wraps
from json import dump
from pathlib import Path
from typing import Protocol, TypeVar, Generic
from uuid import uuid4

from toolz import compose

from hellsicht.kernel.types.analysis import Analysis, AnalysisSource, AnalysisResult
from hellsicht.types import JSONType, DataClass

ParameterType = TypeVar('ParameterType', bound=DataClass)
ResultType = TypeVar('ResultType', bound=DataClass)




@dataclass(frozen=True)
class ServiceRequest(Generic[ParameterType]):
    """
    ServiceRequest

    A class representing a service request.

    Attributes:
        underlying_analysis (Analysis | None): A handle to an Analysis instance.
        result_analysis (Analysis): An instance of the Analysis class.
        parameter (ParameterType): The parameter for the service request.
        request_id (str): The ID of the service request. Generated automatically.
        log_file (Path | None): The path to the log file for the service request. Defaults to None.
        process_limit (int | None): The limit for the number of processes used for the service request. Defaults to None.

    Methods:
        analysis() -> Analysis:
            Getter method that returns an instance of the Analysis class.

    """
    underlying_analysis: AnalysisSource | None
    result_analysis: AnalysisResult
    parameter: ParameterType
    request_id: str = field(default_factory=compose(str, uuid4), init=False)
    log_file: Path | None = None
    process_limit: int | None = None




@dataclass(frozen=True)
class ServiceResponse(Generic[ResultType]):
    """

    Class representing a service response.

    Attributes:
        result (ResultType): The result of the service operation.
        request_id (str): The unique identifier of the request.

    """
    result: ResultType
    request_id: str


@dataclass(frozen=True)
class ServiceError:
    """

    Docstring for class ServiceError:

    This class represents an error encountered during the execution of a service.

    Attributes:
        type (str): The type of the error.
        message (str): The error message.

    """
    type: str
    message: str


class InternalServer(Protocol[ParameterType, ResultType]):
    """
    Internal server for data analysis
    """
    def __call__(self, request: ServiceRequest[ParameterType]) -> ServiceResponse[ResultType] | ServiceError:
        """
        Args:
            request: The service request object that contains the parameters for the method.

        Returns:
            ServiceResponse[ResultType] if the method execution is successful, or ServiceError if an error occurs.

        Raises:
            N/A

        """
        ...

    __name__: str


def wrap_error_as_service_error(
        server: InternalServer[ParameterType, ResultType]
) -> InternalServer[ParameterType, ResultType]:
    """
    Wraps an internal server method and converts any raised exceptions into a ServiceError.

    Args:
        server: An instance of the InternalServer class representing the original server method to be wrapped.

    Returns:
        An instance of the InternalServer class that wraps the original server method and handles exceptions by
        converting them into a ServiceError.

    Raises:
        None.
    """

    @wraps(server)
    def _wrapped(request: ServiceRequest[ParameterType]) -> ServiceResponse[ResultType] | ServiceError:
        try:
            return server(request)
        except Exception as error:
            return ServiceError(type(error).__name__, str(error))

    return _wrapped


def add_log(logfile: Path | None, message: str, **entries: JSONType):
    """
    Args:
        logfile: The path to the log file. If None, the log entry will not be written to a file.
        message: The log message to be written.
        **entries: Additional log entry information in key-value pairs.

    """
    if logfile:
        with logfile.open('a', encoding='utf-8') as out:
            dump(dict(entries, message=message, timestamp=datetime.now().isoformat()), out)
            out.write('\n')
