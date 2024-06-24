from collections.abc import Sequence, Generator
from csv import reader
from dataclasses import dataclass, replace
from io import StringIO
from itertools import chain
from pathlib import Path

from pandas import DataFrame

from hellsicht.kernel.types.progress import Progress
from hellsicht.servers.internal.types import ServiceRequest, ServiceResponse, wrap_error_as_service_error, add_log
from hellsicht.types import DataClass

DELIMITER_REPLACEMENT: str = chr(1)


@dataclass(frozen=True)
class TableParameter(DataClass):
    """

    A class representing parameters for a table.

    Attributes:
        file_path (Path): The path to the file that shall be analysed.
        delimiter (str): The delimiter used to separate values in the table (default is ',').
        encoding (str): The encoding used to read and write the table file (default is 'utf-8').
        errors (str): The error handling strategy when reading or writing the table file (default is 'surrogateescape').
        result_block_size (int): The maximum number of rows to process at a time (default is 10000).

    """
    file_path: Path
    delimiter: str = ','
    encoding: str = 'utf-8'
    errors: str = 'surrogateescape'
    result_block_size: int = 10000


@dataclass(frozen=True)
class TableAnalysis(DataClass):
    """
    Class TableAnalysis

    Represents an analysis of a table with its columns.

    Attributes:
        columns (Sequence[str]): A sequence of strings representing the columns of the table.

    """
    columns: Sequence[str]
    lines_total: int
    chunks_total: int


def _extra_columns(index: int) -> Generator[str, None, None]:
    while True:
        yield f'{index}_extra_column'
        index += 1


@wrap_error_as_service_error
def preprocess_tabular_file(request: ServiceRequest[TableParameter]) -> ServiceResponse[TableAnalysis]:
    """
    Preprocesses a tabular file and saves the chunks as Parquet files.

    Args:
        request: A ServiceRequest object containing the table parameters.

    Returns:
        A ServiceResponse object containing the table analysis and the request ID.
    """
    encoding: str = request.parameter.encoding
    errors: str = request.parameter.errors
    delimiter: str = request.parameter.delimiter
    progress: Progress = Progress('bytes', request.parameter.file_path.stat().st_size)
    with request.parameter.file_path.open(encoding=encoding, errors=errors) as src:
        header: str = src.readline()
        header = header.replace(delimiter, DELIMITER_REPLACEMENT)
        columns: Sequence[str] = next(reader(StringIO(header), delimiter=DELIMITER_REPLACEMENT))
        columns = [f'{no}_{column}' for no, column in enumerate(columns)]
        lines_total: int = 0
        line_counter: int = 0
        current_chunk: int = 0
        current_block: list[dict[str, str]] = list()
        while True:
            line: str = src.readline().replace(delimiter, DELIMITER_REPLACEMENT)
            if not line:
                break
            current_block.append(
                dict(
                    zip(
                        chain(columns, _extra_columns(len(columns))),
                        next(reader(StringIO(line), delimiter=DELIMITER_REPLACEMENT))
                    )
                )
            )
            if len(current_block[-1]) > len(columns):
                add_log(request.log_file, 'Column change detected', former=list(columns), now=list(current_block[-1]))
                columns = list(current_block[-1])

            line_counter += 1
            lines_total += 1
            if line_counter >= request.parameter.result_block_size:
                result: DataFrame = DataFrame(current_block)
                request.result_analysis.save_chunk(result)
                line_counter = 0
                current_chunk += 1
                current_block.clear()
                progress = replace(progress, current=src.tell())
                request.result_analysis.update_progress(progress)
                add_log(request.log_file, 'Starting new chunk', current_chunk=current_chunk)

        result = DataFrame(current_block)
        request.result_analysis.save_chunk(result)
        progress = replace(progress, current=src.tell())
        request.result_analysis.update_progress(progress)
    return ServiceResponse(TableAnalysis(columns, lines_total, current_chunk + 1), request.request_id)
