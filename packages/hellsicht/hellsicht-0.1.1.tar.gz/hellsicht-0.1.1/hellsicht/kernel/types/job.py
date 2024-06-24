from concurrent.futures import Future
from dataclasses import dataclass, field
from multiprocessing import Process
from typing import Generic
from uuid import uuid4

from toolz import compose

from hellsicht.servers.internal.types import ParameterType, ResultType, ServiceRequest, InternalServer


@dataclass(frozen=True)
class Job(Generic[ParameterType, ResultType]):
    process: Future
    request: ServiceRequest[ParameterType]
    server: InternalServer[ParameterType, ResultType]
    job_id: str = field(default_factory=compose(str, uuid4), init=False)
    description: str | None = None

    def __hash__(self) -> int:
        return hash(self.job_id)

    @property
    def finished(self) -> bool:
        return not self.process.running()