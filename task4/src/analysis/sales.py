import pandas as pd
from .helpers import top_n, group_agg, time_series, summary_stats, yoy_growth

def revenue_by_month(df: pd.DataFrame) -> pd.DataFrame:
    return time_series(df, date_col="Order Date", value_col="Revenue USD", freq="ME")


def revenue_by_year(df: pd.DataFrame) -> pd.DataFrame:
    return group_agg(df, by=["Order Date Year"], col="Revenue USD", agg="sum")


def yoy_revenue_growth(df: pd.DataFrame) -> pd.DataFrame:
    return yoy_growth(df, date_col="Order Date Year", value_col="Revenue USD")


def online_vs_instore(df: pd.DataFrame) -> pd.DataFrame:
    df = df.copy()
    df["Channel"] = df["Is Online"].map({True: "Online", False: "In-Store"})
    counts  = df["Channel"].value_counts().rename("orders")
    revenue = df.groupby("Channel")["Revenue USD"].sum().round(2)
    return pd.concat([counts, revenue], axis=1).reset_index().rename(columns={"index": "Channel"})


def revenue_by_country(df: pd.DataFrame, n: int = 10) -> pd.Series:
    return top_n(df, "Country", n=n, agg="sum", value_col="Revenue USD")


def top_products_by_revenue(df: pd.DataFrame, n: int = 10) -> pd.Series:
    return top_n(df, "Product Name", n=n, agg="sum", value_col="Revenue USD")


def revenue_by_category(df: pd.DataFrame) -> pd.DataFrame:
    return group_agg(df, by=["Category"], col="Revenue USD", agg="sum").sort_values("Revenue USD", ascending=False)


def revenue_by_month_year(df: pd.DataFrame) -> pd.DataFrame:
    return group_agg(df, by=["Order Date Year", "Order Date Month"], col="Revenue USD", agg="sum")


def delivery_days_stats(df: pd.DataFrame) -> pd.Series:
    # Online orders only — physical store customers collect in store, no delivery date exists
    # Exclude Is Delivery Pending rows — delivery not yet completed at dataset cutoff
    online_complete = df[(df["Is Online"] == True) & (df["Is Delivery Pending"] == False)]
    return summary_stats(online_complete, "Delivery Days")