import pandas as pd


def top_n(df: pd.DataFrame, col: str, n: int = 10, agg: str = "sum", value_col: str = None) -> pd.Series:
    if agg == "count":
        return df.groupby(col).size().nlargest(n)
    return df.groupby(col, observed=False)[value_col].agg(agg).nlargest(n)


def group_agg(df: pd.DataFrame, by: list, col: str, agg: str = "sum") -> pd.DataFrame:
    return df.groupby(by, observed=False)[col].agg(agg).reset_index()


def pct_split(df: pd.DataFrame, col: str) -> pd.Series:
    counts = df[col].value_counts()
    return (counts / counts.sum() * 100).round(2)


def time_series(df: pd.DataFrame, date_col: str, value_col: str, freq: str = "ME") -> pd.DataFrame:
    df = df.copy()
    df[date_col] = pd.to_datetime(df[date_col])
    return (
        df.set_index(date_col)[value_col]
        .resample(freq)
        .sum()
        .reset_index()
    )


def summary_stats(df: pd.DataFrame, col: str) -> pd.Series:
    return df[col].describe().round(2)


def value_counts_pct(df: pd.DataFrame, col: str) -> pd.DataFrame:
    counts = df[col].value_counts().reset_index()
    counts.columns = [col, "count"]
    counts["pct"] = (counts["count"] / counts["count"].sum() * 100).round(2)
    return counts


def yoy_growth(df: pd.DataFrame, date_col: str, value_col: str) -> pd.DataFrame:
    annual = df.groupby(date_col)[value_col].sum().reset_index()
    annual["yoy_growth_pct"] = annual[value_col].pct_change() * 100
    return annual.round(2)