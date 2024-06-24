from dataclasses import asdict, dataclass
from json import load, dump
from typing import IO, Protocol

from dacite import from_dict


@dataclass(frozen=True)
class Progress:
    """
    A class representing the progress of a task.

    Attributes:
        unit (str): The unit of measurement for the progress.
        total (int or float): The total amount of progress.
        current (int or float): The current progress. Default value is 0.0.

    """
    unit: str
    total: int | float
    current: int | float = 0.0

    @property
    def finished(self) -> bool:
        return self.current >= self.total


class ProgressTracker(Protocol):
    """
    The ProgressTracker class is a protocol that provides a method for opening a file. It is used to track the progress
    of file operations.

    Methods:
        open(mode='r', buffering=-1, encoding=None, errors=None, newline=None) -> IO[str]:
            This method opens a file and returns a file object of type IO[str].

    Parameters:
        - mode (str): Specifies the mode in which the file is opened. Defaults to 'r' (read mode).
        - buffering (int): Specifies the buffering policy. Defaults to -1 (default buffering).
        - encoding (str): Specifies the encoding to be used for the file. Defaults to None (system default encoding).
        - errors (str): Specifies how encoding and decoding errors should be handled. Defaults to None
                        (strict handling).
        - newline (str): Specifies the newline character(s) to be used when reading or writing to the file.
                         Defaults to None (use system default).

    Returns:
        IO[str]: A file object representing the opened file.

    Examples:
        tracker = ProgressTracker()
        file = tracker.open('r', -1, 'utf-8', 'strict', '\n')

    Note:
        - The mode parameter can take values 'r', 'w', 'a', or 'x' for read, write, append, or exclusive create mode respectively.
        - The buffering parameter can take values -1, 0, 1, or any positive integer for default, no buffering, line buffering, or buffer size respectively.
        - The encoding parameter determines the encoding of the file contents. Common values include 'utf-8', 'ascii', 'latin-1', etc.
        - The errors parameter determines how encoding and decoding errors are handled. Common values include 'strict', 'ignore', 'replace', etc.
        - The newline parameter determines the newline character(s) to be used. Common values include '\n', '\r\n', etc.
    """
    def open(self, mode='r', buffering=-1, encoding=None, errors=None, newline=None) -> IO[str]:
        ...


def update_progress(tracker: ProgressTracker | None, progress: Progress) -> None:
    """Updates the progress in the given tracker.

    Args:
        tracker: A tracker to write the progress data.
        progress: The progress to be written.

    """
    if tracker:
        with tracker.open('w', encoding='utf-8') as out:
            dump(asdict(progress), out)


def get_progress(tracker: ProgressTracker) -> Progress:
    """
    Args:
        tracker: ProgressTracker object.

    Returns:
        Progress object containing the progress loaded from the given tracker.

    Example:
        tracker = ProgressTracker()
        progress = get_progress(tracker)
    """
    with tracker.open(encoding='utf-8') as src:
        return from_dict(Progress, load(src))
