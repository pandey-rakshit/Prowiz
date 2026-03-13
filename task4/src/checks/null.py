import pandas as pd


def run(name: str, df: pd.DataFrame) -> pd.DataFrame:
    nulls = df.isnull().sum()
    pct   = (nulls / len(df) * 100).round(2)

    report = pd.DataFrame({
        "dataset" : name,
        "column"  : nulls.index,
        "nulls"   : nulls.values,
        "null_pct": pct.values,
    })

    return report[report["nulls"] > 0].reset_index(drop=True)