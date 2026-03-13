import pandas as pd
from src.analysis.helpers import top_n, pct_split, summary_stats, value_counts_pct


def age_distribution(df: pd.DataFrame) -> pd.Series:
    return df["Age"].dropna()


def age_group_split(df: pd.DataFrame) -> pd.DataFrame:
    return value_counts_pct(df, "Age Group")


def gender_split(df: pd.DataFrame) -> pd.Series:
    return pct_split(df, "Gender")


def customers_by_country(df: pd.DataFrame, n: int = 10) -> pd.Series:
    return top_n(df, "Country", n=n, agg="count")


def customers_by_continent(df: pd.DataFrame) -> pd.Series:
    return pct_split(df, "Continent")


def gender_by_country(df: pd.DataFrame, n: int = 10) -> pd.DataFrame:
    top_countries = customers_by_country(df, n=n).index
    filtered = df[df["Country"].isin(top_countries)]
    return filtered.groupby(["Country", "Gender"]).size().unstack(fill_value=0)


def age_stats(df: pd.DataFrame) -> pd.Series:
    return summary_stats(df, "Age")