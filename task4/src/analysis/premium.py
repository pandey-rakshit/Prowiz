import pandas as pd
from .helpers import group_agg


def _premium_sales(sales: pd.DataFrame, products: pd.DataFrame) -> pd.DataFrame:
    df = sales.merge(products[["ProductKey", "Is Premium Product", "Category"]], on="ProductKey", how="left")
    return df[df["Is Premium Product"] == True]


def premium_revenue_by_category(sales: pd.DataFrame, products: pd.DataFrame) -> pd.DataFrame:
    df = _premium_sales(sales, products)
    return group_agg(df, by=["Category"], col="Revenue USD", agg="sum").sort_values("Revenue USD", ascending=False)


def premium_revenue_by_country(sales: pd.DataFrame, products: pd.DataFrame, customers: pd.DataFrame) -> pd.DataFrame:
    df = _premium_sales(sales, products)
    df = df.merge(customers[["CustomerKey", "Country"]], on="CustomerKey", how="left")
    return group_agg(df, by=["Country"], col="Revenue USD", agg="sum").sort_values("Revenue USD", ascending=False)


def premium_revenue_by_age_group(sales: pd.DataFrame, products: pd.DataFrame, customers: pd.DataFrame) -> pd.DataFrame:
    df = _premium_sales(sales, products)
    df = df.merge(customers[["CustomerKey", "Age Group"]], on="CustomerKey", how="left")
    return group_agg(df, by=["Age Group"], col="Revenue USD", agg="sum").sort_values("Revenue USD", ascending=False)


def premium_revenue_by_channel(sales: pd.DataFrame, products: pd.DataFrame) -> pd.DataFrame:
    df = _premium_sales(sales, products)
    df["Channel"] = df["Is Online"].map({True: "Online", False: "In-Store"})
    return group_agg(df, by=["Channel"], col="Revenue USD", agg="sum")


def premium_vs_standard_by_category(sales: pd.DataFrame, products: pd.DataFrame) -> pd.DataFrame:
    df = sales.merge(products[["ProductKey", "Is Premium Product", "Category"]], on="ProductKey", how="left")
    df["Segment"] = df["Is Premium Product"].map({True: "Premium", False: "Standard"})
    return df.groupby(["Category", "Segment"])["Revenue USD"].sum().unstack().fillna(0).round(2)


def premium_order_count(sales: pd.DataFrame, products: pd.DataFrame) -> pd.DataFrame:
    df = sales.merge(products[["ProductKey", "Is Premium Product"]], on="ProductKey", how="left")
    df["Segment"] = df["Is Premium Product"].map({True: "Premium", False: "Standard"})
    counts  = df["Segment"].value_counts().rename("Orders")
    revenue = df.groupby("Segment")["Revenue USD"].sum().round(2)
    return pd.concat([counts, revenue], axis=1).reset_index().rename(columns={"index": "Segment"})