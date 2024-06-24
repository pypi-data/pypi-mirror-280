from collections import defaultdict
from collections.abc import Collection
from dataclasses import dataclass, replace
from functools import partial
from multiprocessing import Pool
from re import Pattern, compile as regex, UNICODE, DOTALL
from typing import TypeAlias

from pandas import DataFrame

from hellsicht.kernel.types.progress import Progress
from hellsicht.servers.internal.types import wrap_error_as_service_error, ServiceRequest, ServiceResponse, add_log
from hellsicht.types import DataClass, FieldName, RegularExpression, parse_field_name


@dataclass(frozen=True)
class SelectiveAnalysis(DataClass):
    """Stores and manages selective analysis configurations.

    Attributes:
        analyze_field_by (dict[FieldName, set[tuple[str, RegularExpression]]]):
            A dictionary that maps field names to a set of regular expression patterns and corresponding names.
    """
    analyze_field_by: dict[FieldName, set[tuple[str, RegularExpression]]]

    def compile(self) -> dict[FieldName, set[tuple[str, Pattern]]]:
        """
        Compiles expressions for each field in analyze_field_by.

        Returns:
            A dictionary mapping each field name to a set of tuples.
            Each tuple consists of a name and a compiled regular expression pattern.
        """
        return dict(
            (field_, {(name, regex(pattern, UNICODE | DOTALL)) for name, pattern in expressions})
            for field_, expressions in self.analyze_field_by.items()
        )


@dataclass(frozen=True)
class FullAnalysis(DataClass):
    """Represents a full analysis with patterns for all fieldnames."""
    patterns: set[tuple[str, RegularExpression]]

    def as_selective(self, fieldnames: Collection[FieldName]) -> SelectiveAnalysis:
        """
        Args:
            fieldnames: A collection of field names for which selective analysis needs to be performed.

        Returns:
            SelectiveAnalysis: An instance of SelectiveAnalysis containing the field names and their corresponding
                               patterns.
        """
        return SelectiveAnalysis(dict((field_, self.patterns) for field_ in fieldnames))


PatternAnalysisParameter: TypeAlias = SelectiveAnalysis | FullAnalysis


def pattern_analyze_value(patterns: set[tuple[str, Pattern]], value: str) -> set[str]:
    """
    Args:
        patterns: A set of tuples representing the patterns to analyze. Each tuple consists of a name (str) and a
                  pattern (Pattern) object.
        value: The value (str) to be analyzed.

    Returns:
        A set of strings representing the names of the patterns that match the given value.
"""
    return {name for name, pattern in patterns if pattern.match(value)}


def pattern_analyze_chunk(parameter: PatternAnalysisParameter, chunk: DataFrame) -> DataFrame:
    """
    Args:
        parameter: The PatternAnalysisParameter object containing the analysis parameters.
                   It can be either an instance of SelectiveAnalysis or any other object that can be converted
                   to SelectiveAnalysis.
        chunk: The DataFrame object representing the data chunk to be analyzed.

    Returns:
        A DataFrame object with the analysis results.

    """
    select: SelectiveAnalysis = parameter if isinstance(parameter, SelectiveAnalysis) else parameter.as_selective(
        tuple(map(parse_field_name, chunk.columns))
    )
    patterns: dict[FieldName, set[tuple[str, Pattern]]] = select.compile()
    return DataFrame(
        dict(
            (column, pattern_analyze_value(patterns.get(column, set()), str(row[column])))
            for column in map(parse_field_name, chunk.columns)
        )
        for _, row in chunk.iterrows()
    )


@dataclass(frozen=True)
class PatternAnalysis(DataClass):
    """Class representing the analysis results of pattern occurrences in a dataset.

    Attributes:
        counts_per_column (dict[FieldName, dict[str, int]]): A dictionary that stores the count of each pattern
            occurrence per column in the dataset.

    """
    counts_per_column: dict[FieldName, dict[str, int]]


@wrap_error_as_service_error
def classify_by_pattern(request: ServiceRequest[PatternAnalysisParameter]) -> ServiceResponse[PatternAnalysis]:
    """
    Classifies an analysis by regular expressions.

    Args:
        request: A ServiceRequest object containing the request parameters for pattern analysis.

    Returns:
        A ServiceResponse object containing the result of the pattern analysis.

    """

    counts_per_column: dict[FieldName, dict[str, int]] = defaultdict(lambda: defaultdict(int))
    progress: Progress = Progress('frames', len(request.underlying_analysis))
    with Pool(request.process_limit) as pool:
        for result_frame in pool.map(
                partial(pattern_analyze_chunk, request.parameter),
                request.underlying_analysis
        ):
            request.result_analysis.save_chunk(result_frame)
            for column in map(parse_field_name, result_frame.columns):
                for row in result_frame[column]:
                    for value in row:
                        counts_per_column[column][value] += 1
            progress = replace(progress, current=progress.current + 1)

            request.result_analysis.update_progress(progress)
            add_log(request.log_file, 'Result chunk written')
    counts_per_column = dict((k, dict(v)) for k, v in counts_per_column.items())
    return ServiceResponse(PatternAnalysis(counts_per_column), request.request_id)
