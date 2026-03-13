import pandas as pd


def run(name: str, df: pd.DataFrame, subset: list = None) -> dict:
    count = df.duplicated(subset=subset).sum()
    return {
        "dataset"       : name,
        "duplicate_rows": int(count),
        "subset"        : subset,
    }