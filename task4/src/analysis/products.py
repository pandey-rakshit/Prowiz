import pandas as pd
from .helpers import top_n, pct_split, summary_stats, value_counts_pct, group_agg


def category_split(df: pd.DataFrame) -> pd.DataFrame:
    return value_counts_pct(df, "Category")


def subcategory_split(df: pd.DataFrame) -> pd.DataFrame:
    return value_counts_pct(df, "Subcategory")


def top_brands_by_count(df: pd.DataFrame, n: int = 10) -> pd.Series:
    return top_n(df, "Brand", n=n, agg="count")


def top_brands_by_margin(df: pd.DataFrame, n: int = 10) -> pd.Series:
    return top_n(df, "Brand", n=n, agg="mean", value_col="Margin Pct")


def margin_distribution(df: pd.DataFrame) -> pd.Series:
    return df["Margin Pct"].dropna()


def margin_by_category(df: pd.DataFrame) -> pd.DataFrame:
    return group_agg(df, by=["Category"], col="Margin Pct", agg="mean").round(2)


def price_distribution(df: pd.DataFrame) -> pd.Series:
    return df["Unit Price USD"].dropna()


def margin_stats(df: pd.DataFrame) -> pd.Series:
    return summary_stats(df, "Margin Pct")


def products_by_category_subcategory(df: pd.DataFrame) -> pd.DataFrame:
    return df.groupby(["Category", "Subcategory"]).size().reset_index(name="count")