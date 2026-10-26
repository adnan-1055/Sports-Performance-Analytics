
"""Data-quality checks for sports performance records."""

import pandas as pd


def check_required_columns(
    data: pd.DataFrame,
    required_columns: list[str],
) -> list[str]:
    """Return required columns that are missing."""
    return [
        column
        for column in required_columns
        if column not in data.columns
    ]


def check_missing_values(data: pd.DataFrame) -> dict[str, int]:
    """Count missing values in each column."""
    return {
        column: int(count)
        for column, count in data.isna().sum().items()
        if count > 0
    }


def check_positive_values(
    data: pd.DataFrame,
    columns: list[str],
) -> dict[str, int]:
    """Count zero or negative values in numeric columns."""
    issues = {}

    for column in columns:
        if column not in data.columns:
            continue

        values = pd.to_numeric(data[column], errors="coerce")
        issues[column] = int((values <= 0).sum())

    return {column: count for column, count in issues.items() if count > 0}
