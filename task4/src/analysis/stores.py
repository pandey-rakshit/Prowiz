import pandas as pd
from .helpers import top_n, group_agg, summary_stats


def _physical(df: pd.DataFrame) -> pd.DataFrame:
    return df[df["Is Online Store"] == False]


def online_vs_physical(df: pd.DataFrame) -> pd.Series:
    return df["Is Online Store"].map({True: "Online", False: "Physical"}).value_counts()


def stores_by_country(df: pd.DataFrame) -> pd.Series:
    return top_n(_physical(df), "Country", n=20, agg="count")


def store_size_distribution(df: pd.DataFrame) -> pd.Series:
    return _physical(df)["Square Meters"].dropna()


def store_size_stats(df: pd.DataFrame) -> pd.Series:
    return summary_stats(_physical(df), "Square Meters")


def store_age_distribution(df: pd.DataFrame) -> pd.Series:
    return _physical(df)["Store Age Years"].dropna()


def avg_store_size_by_country(df: pd.DataFrame) -> pd.DataFrame:
    return (
        group_agg(_physical(df), by=["Country"], col="Square Meters", agg="mean")
        .round(0)
        .sort_values("Square Meters", ascending=False)
    )


def revenue_per_store(df: pd.DataFrame, sales: pd.DataFrame) -> pd.DataFrame:
    # physical stores only — StoreKey 0 (online) excluded, analysed separately
    revenue = group_agg(sales, by=["StoreKey"], col="Revenue USD", agg="sum")
    return (
        _physical(df)
        .merge(revenue, on="StoreKey", how="left")
        .sort_values("Revenue USD", ascending=False)
    )


def online_store_revenue(df: pd.DataFrame, sales: pd.DataFrame) -> float:
    # StoreKey 0 revenue reported separately — dwarfs all physical stores
    online_key = df[df["Is Online Store"] == True]["StoreKey"].iloc[0]
    return sales[sales["StoreKey"] == online_key]["Revenue USD"].sum()


def store_size_vs_revenue(df: pd.DataFrame, sales: pd.DataFrame) -> pd.DataFrame:
    revenue = group_agg(sales, by=["StoreKey"], col="Revenue USD", agg="sum")
    merged  = _physical(df).merge(revenue, on="StoreKey", how="left")
    return merged[["Square Meters", "Revenue USD", "Country"]].dropna()