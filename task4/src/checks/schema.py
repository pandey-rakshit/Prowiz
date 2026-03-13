import pandas as pd
from config.schema import SCHEMA


def run(name: str, df: pd.DataFrame) -> list:
    issues = []
    expected = SCHEMA.get(name, {})

    for col, expected_dtype in expected.items():
        if col not in df.columns:
            issues.append(f"missing column: {col}")
            continue
        actual = str(df[col].dtype)
        if "datetime" in expected_dtype and "datetime" not in actual:
            issues.append(f"dtype mismatch: {col} expected datetime, got {actual}")

    return issues