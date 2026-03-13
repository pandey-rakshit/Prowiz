import pandas as pd
from .helpers import group_agg, time_series, top_n


def revenue_by_age_group(sales: pd.DataFrame, customers: pd.DataFrame) -> pd.DataFrame:
    df = sales.merge(customers[["CustomerKey", "Age Group"]], on="CustomerKey", how="left")
    return group_agg(df, by=["Age Group"], col="Revenue USD", agg="sum").sort_values("Revenue USD", ascending=False)


def revenue_by_gender(sales: pd.DataFrame, customers: pd.DataFrame) -> pd.DataFrame:
    df = sales.merge(customers[["CustomerKey", "Gender"]], on="CustomerKey", how="left")
    return group_agg(df, by=["Gender"], col="Revenue USD", agg="sum")


def revenue_by_continent(sales: pd.DataFrame, customers: pd.DataFrame) -> pd.DataFrame:
    df = sales.merge(customers[["CustomerKey", "Continent"]], on="CustomerKey", how="left")
    return group_agg(df, by=["Continent"], col="Revenue USD", agg="sum").sort_values("Revenue USD", ascending=False)


def revenue_premium_vs_standard(sales: pd.DataFrame, products: pd.DataFrame) -> pd.DataFrame:
    df = sales.merge(products[["ProductKey", "Is Premium Product"]], on="ProductKey", how="left")
    df["Segment"] = df["Is Premium Product"].map({True: "Premium", False: "Standard"})
    return group_agg(df, by=["Segment"], col="Revenue USD", agg="sum")


def revenue_bulk_vs_standard(sales: pd.DataFrame) -> pd.DataFrame:
    df = sales.copy()
    df["Order Type"] = df["Is Bulk Order"].map({True: "Bulk", False: "Standard"})
    return group_agg(df, by=["Order Type"], col="Revenue USD", agg="sum")


def revenue_by_quarter(sales: pd.DataFrame) -> pd.DataFrame:
    return group_agg(sales, by=["Order Date Year", "Order Date Quarter"], col="Revenue USD", agg="sum")


def avg_order_value_by_channel(sales: pd.DataFrame) -> pd.DataFrame:
    df = sales.copy()
    df["Channel"] = df["Is Online"].map({True: "Online", False: "In-Store"})
    return group_agg(df, by=["Channel"], col="Revenue USD", agg="mean").round(2)


def avg_order_value_by_country(sales: pd.DataFrame, customers: pd.DataFrame) -> pd.DataFrame:
    df = sales.merge(customers[["CustomerKey", "Country"]], on="CustomerKey", how="left")
    return group_agg(df, by=["Country"], col="Revenue USD", agg="mean").round(2).sort_values("Revenue USD", ascending=False)


def revenue_by_category_channel(sales: pd.DataFrame, products: pd.DataFrame) -> pd.DataFrame:
    df = sales.merge(products[["ProductKey", "Category"]], on="ProductKey", how="left")
    df["Channel"] = df["Is Online"].map({True: "Online", False: "In-Store"})
    return df.groupby(["Category", "Channel"])["Revenue USD"].sum().unstack().fillna(0).round(2)