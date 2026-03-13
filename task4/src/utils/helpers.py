import pandas as pd


def parse_dates(df: pd.DataFrame, cols: list) -> pd.DataFrame:
    df = df.copy()
    for col in cols:
        df[col] = pd.to_datetime(df[col], errors="coerce")
    return df


def strip_currency(df: pd.DataFrame, cols: list) -> pd.DataFrame:
    df = df.copy()
    for col in cols:
        df[col] = df[col].astype(str).str.replace(r"[$,£€\s]", "", regex=True)
    return df


def to_numeric(df: pd.DataFrame, cols: list) -> pd.DataFrame:
    df = df.copy()
    for col in cols:
        df[col] = pd.to_numeric(df[col], errors="coerce")
    return df


def drop_nulls(df: pd.DataFrame, subset: list) -> pd.DataFrame:
    return df.dropna(subset=subset).reset_index(drop=True)


def add_age(df: pd.DataFrame, date_col: str, new_col: str = "Age") -> pd.DataFrame:
    df = df.copy()
    reference = pd.Timestamp.today()
    df[new_col] = (reference - df[date_col]).dt.days // 365
    return df


def add_elapsed_years(df: pd.DataFrame, date_col: str, new_col: str) -> pd.DataFrame:
    df = df.copy()
    reference = pd.Timestamp.today()
    df[new_col] = (reference - df[date_col]).dt.days // 365
    return df


def add_elapsed_days(df: pd.DataFrame, start_col: str, end_col: str, new_col: str) -> pd.DataFrame:
    df = df.copy()
    df[new_col] = (df[end_col] - df[start_col]).dt.days
    return df


def add_date_parts(df: pd.DataFrame, date_col: str, parts: list = None) -> pd.DataFrame:
    df = df.copy()
    part_map = {
        "year"   : df[date_col].dt.year,
        "month"  : df[date_col].dt.month,
        "quarter": df[date_col].dt.quarter,
    }
    for part in (parts or part_map.keys()):
        df[f"{date_col} {part.capitalize()}"] = part_map[part]
    return df


def add_bins(df: pd.DataFrame, col: str, bins: list, labels: list, new_col: str) -> pd.DataFrame:
    df = df.copy()
    df[new_col] = pd.cut(df[col], bins=bins, labels=labels, right=False)
    return df


def add_ratio(df: pd.DataFrame, numerator: str, denominator: str, new_col: str, scale: float = 1.0) -> pd.DataFrame:
    df = df.copy()
    df[new_col] = (df[numerator] / df[denominator] * scale).round(2)
    return df