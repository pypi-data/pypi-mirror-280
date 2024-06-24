from collections.abc import Iterable
from dataclasses import dataclass, replace
from functools import partial
from json import dump, load
from pathlib import Path
from uuid import uuid4

from pandas import DataFrame, read_parquet

from hellsicht.kernel.types.progress import ProgressTracker, Progress, update_progress
from hellsicht.kernel.types.shape import DataShape
from hellsicht.types import JSONType


@dataclass(frozen=True)
class Analysis:
    """
    A class representing an analysis.

    Attributes:
        name (str): The name of the analysis.
        path (Path): The path to the analysis file.
        progress: (ProgressTracker): Tracks the process of the analysis.
        average_chunk_size (float): The average size of each data chunk.
        chunk_count (int): The number of data chunks in the analysis.
        rows (int): The total number of rows in the analysis.
        description (str, optional): A description of the analysis (default: None).
        data_shape (DataShape, optional): The shape of the analysis data (default: None).
        job_id (str, optional): The unique identifier of the analysis job (default: None).
    """
    name: str
    path: Path
    progress: ProgressTracker
    average_chunk_size: float = 0
    chunk_count: int = 0
    rows: int = 0
    description: str | None = None
    data_shape: DataShape | None = None
    job_id: str | None = None

    @classmethod
    def new_from_path(cls, path: Path, name: str | None = None) -> 'Analysis':
        return cls(name if name else str(uuid4()), path, path.joinpath('progress.json'))

    def __hash__(self) -> int:
        return hash(self.path.as_uri())


def _get_chunk_name(chunk_no: int) -> str:
    """
    Args:
        chunk_no: An integer representing the chunk number.

    Returns:
        A string that is the name of the chunk file, following the format 'chunk_{chunk_no}.parquet'.
    """
    return f'chunk_{chunk_no}.parquet'


def _update_average(average: float, n: int, update: int) -> float:
    return (average * n + update) / (n+1)


def _metadata_file(analysis: Analysis) -> Path:
    """
    Args:
        analysis: The analysis object containing information about the file path.

    Returns:
        Path: The path to the metadata file.
    """
    return analysis.path.joinpath('.metadata.json')


def write_metadata(analysis: Analysis, **metadata: JSONType):
    """
    Args:
        analysis: The analysis object for which the metadata is being written.
        **metadata: Key-value pairs of metadata information to be written for the analysis.

    """
    with _metadata_file(analysis).open('w', encoding='utf-8') as out:
        dump(metadata, out)


def get_metadata(analysis: Analysis) -> JSONType:
    """
    Args:
        analysis (Analysis): The analysis object for which to retrieve metadata.

    Returns:
        JSONType: The metadata associated with the analysis object.

    """
    file: Path = _metadata_file(analysis)
    if not file.exists():
        return dict()
    with file.open( encoding='utf-8') as src:
        return load(src)


def save_chunk(analysis: Analysis, chunk: DataFrame) -> Analysis:
    """
    Args:
        analysis: An instance of the Analysis class representing the analysis to be performed.
        chunk: A DataFrame containing the chunk of data to be saved.

    Returns:
        An instance of the Analysis class with updated attributes.

    """
    chunk.to_parquet(analysis.path.joinpath(_get_chunk_name(analysis.chunk_count)), index=False)
    return replace(
        analysis,
        chunk_count=analysis.chunk_count + 1,
        rows=analysis.rows + len(chunk),
        average_chunk_size=_update_average(analysis.average_chunk_size, analysis.chunk_count, len(chunk))
    )


def load_chunk(analysis: Analysis, chunk_no: int) -> DataFrame:
    """
    Load the specified chunk of data from the analysis.

    Args:
        analysis: The analysis object representing the data analysis.
        chunk_no: The number of the chunk to load.

    Returns:
        DataFrame: The loaded chunk as a pandas DataFrame.
    """
    if chunk_no > analysis.chunk_count:
        raise IndexError(f'Chunk {chunk_no} out of bounds: Analysis has only {analysis.chunk_count} chunks.')
    return read_parquet(analysis.path.joinpath(_get_chunk_name(chunk_no)))


def get_chunks(analysis: Analysis) -> Iterable[DataFrame]:
    """
    Args:
        analysis: An instance of the Analysis class.

    Returns:
        An Iterable containing DataFrames that represent the chunks of the analysis.

    Raises:
        None.

    Example usage:
        analysis = Analysis()
        chunks = get_chunks(analysis)
        for chunk in chunks:
            # Do something with each chunk
    """
    return map(partial(load_chunk, analysis), range(analysis.chunk_count))


def update_shape(analysis: Analysis, shape: DataShape) -> Analysis:
    """
    Args:
        analysis: An instance of the Analysis class containing the analysis data.
        shape: A DataShape object representing the updated shape.

    Returns:
        An instance of the Analysis class with the shape updated.
    """
    return replace(analysis, data_shape=shape)



class AnalysisSource:
    """
    A class representing a data analysis source.

    Attributes:
        _analysis (Analysis): The analysis object associated with the source.

    Methods:
        __init__(analysis: Analysis) -> None:
            Initializes an AnalysisSource instance with the given Analysis object.

        load_chunk(chunk_no: int) -> DataFrame:
            Loads and returns a chunk of data from the analysis source based on the specified chunk number.

        __iter__() -> Iterable[DataFrame]:
            Returns an iterator over the chunks of data in the analysis source.

        shape -> DataShape:
            Returns the shape of the data stored in the analysis source.

        metadata -> JSONType:
            Returns the metadata associated with the analysis source.
    """
    def __init__(self, analysis: Analysis):
        self._analysis: Analysis = analysis

    def load_chunk(self, chunk_no: int) -> DataFrame:
        """
        Args:
            chunk_no: An integer representing the number of the chunk to be loaded.

        Returns:
            DataFrame: A pandas DataFrame containing the loaded chunk.
        """
        return load_chunk(self._analysis, chunk_no)

    def __len__(self) -> int:
        return self._analysis.chunk_count

    def __iter__(self) -> Iterable[DataFrame]:
        """

        The __iter__ method is used to make an object iterable. It returns an iterator object that allows iteration over
        the chunks of data.

        Parameters:
            self: The object itself.

        Returns:
            An iterator object that yields DataFrame chunks.

        """
        return get_chunks(self._analysis)

    @property
    def shape(self) -> DataShape:
        """
        Returns the shape of the data.

        Returns:
            DataShape: The shape of the data.

        """
        return self._analysis.data_shape

    @property
    def metadata(self) -> JSONType:
        """Get the metadata for the method.

        Returns:
            JSONType: The metadata for the method.

        """
        return get_metadata(self._analysis)


class AnalysisResult(AnalysisSource):
    """

    Class: AnalysisResult

    AnalysisResult is a subclass of AnalysisSource and represents the result of an analysis. It provides methods to save
    the analysis results, update the shape, and add metadata to the analysis.

    Methods:
    - __init__(self, analysis: Analysis)
      Initializes an instance of AnalysisResult with the given analysis.

    - save_chunk(self, chunk: DataFrame) -> int
      Saves a chunk of analysis results by appending it to the existing analysis. Returns the number of rows in the chunk.

    - shape(self, shape: DataShape)
      Setter method to update the shape of the analysis. The shape parameter should be an instance of DataShape.

    - metadata(self, **metadata: JSONType)
      Setter method to add metadata to the analysis. The metadata should be provided as keyword arguments.

    """
    def __init__(self, analysis: Analysis):
        super().__init__(analysis)


    def save_chunk(self, chunk: DataFrame) -> int:
        """
        Args:
            chunk: The chunk of data to be saved.

        Returns:
            int: The number of rows in the saved chunk.
        """
        self._analysis = save_chunk(self._analysis, chunk)
        return len(chunk)

    def update_progress(self, progress: Progress):
        """
        Updates the progress of the analysis.

        Args:
            progress: An instance of the Progress class representing the updated progress.

        Returns:
            None

        """
        update_progress(self._analysis.progress, progress)

    @AnalysisSource.shape.setter
    def shape(self, shape: DataShape):
        """Updates the shape of the analysis data.

        Args:
            shape (DataShape): The new shape of the analysis data.
        """
        self._analysis = update_shape(self._analysis, shape)

    @AnalysisSource.metadata.setter
    def metadata(self, **metadata: JSONType):
        """
        Args:
            **metadata: A dictionary containing the metadata for the AnalysisSource object.
                This dictionary should have key-value pairs corresponding to the metadata attributes.
        """
        write_metadata(self._analysis, **metadata)

    @property
    def analysis(self) -> Analysis:
        return self._analysis
