import pandas as pd


def run(
    child_df   : pd.DataFrame,
    child_col  : str,
    parent_df  : pd.DataFrame,
    parent_col : str,
    label      : str,
) -> dict:
    child_keys  = set(child_df[child_col].dropna().unique())
    parent_keys = set(parent_df[parent_col].dropna().unique())
    orphans     = child_keys - parent_keys

    return {
        "check"       : label,
        "orphan_count": len(orphans),
        "sample"      : sorted(list(orphans))[:5],
    }