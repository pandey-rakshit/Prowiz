import pandas as pd
from .helpers import group_agg


def _physical(stores: pd.DataFrame) -> pd.DataFrame:
    return stores[stores["Is Online Store"] == False]


def store_revenue_with_meta(stores: pd.DataFrame, sales: pd.DataFrame) -> pd.DataFrame:
    revenue = group_agg(sales, by=["StoreKey"], col="Revenue USD", agg="sum")
    orders  = sales.groupby("StoreKey").size().reset_index(name="Order Count")
    df = _physical(stores).merge(revenue, on="StoreKey", how="left")
    df = df.merge(orders, on="StoreKey", how="left")
    df["Avg Order Value"] = (df["Revenue USD"] / df["Order Count"]).round(2)
    return df


def revenue_by_size_band(stores: pd.DataFrame, sales: pd.DataFrame) -> pd.DataFrame:
    df = store_revenue_with_meta(stores, sales)
    bins   = [0, 500, 1000, 1500, 2100]
    labels = ["Small (<500)", "Medium (500-1000)", "Large (1000-1500)", "XLarge (1500+)"]
    df["Size Band"] = pd.cut(df["Square Meters"], bins=bins, labels=labels)
    return df.groupby("Size Band", observed=True)["Revenue USD"].agg(["sum", "mean", "count"]).round(2).reset_index()


def revenue_by_country_store(stores: pd.DataFrame, sales: pd.DataFrame) -> pd.DataFrame:
    df = store_revenue_with_meta(stores, sales)
    return df.groupby("Country").agg(
        Store_Count=("StoreKey", "count"),
        Total_Revenue=("Revenue USD", "sum"),
        Avg_Revenue=("Revenue USD", "mean"),
    ).round(2).sort_values("Avg_Revenue", ascending=False).reset_index()


def store_age_vs_revenue(stores: pd.DataFrame, sales: pd.DataFrame) -> pd.DataFrame:
    df = store_revenue_with_meta(stores, sales)
    return df[["Store Age Years", "Revenue USD", "Country"]].dropna()


def low_performers(stores: pd.DataFrame, sales: pd.DataFrame, threshold: float = 300000) -> pd.DataFrame:
    df = store_revenue_with_meta(stores, sales)
    return df[df["Revenue USD"] < threshold][["StoreKey", "Country", "Square Meters", "Store Age Years", "Revenue USD"]].sort_values("Revenue USD")