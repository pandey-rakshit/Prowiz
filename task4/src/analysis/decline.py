import pandas as pd

def revenue_by_year_country(sales: pd.DataFrame, customers: pd.DataFrame) -> pd.DataFrame:
    df = sales.merge(customers[["CustomerKey", "Country"]], on="CustomerKey", how="left")
    return df.groupby(["Order Date Year", "Country"])["Revenue USD"].sum().reset_index()


def revenue_by_year_category(sales: pd.DataFrame, products: pd.DataFrame) -> pd.DataFrame:
    df = sales.merge(products[["ProductKey", "Category"]], on="ProductKey", how="left")
    return df.groupby(["Order Date Year", "Category"])["Revenue USD"].sum().reset_index()


def revenue_by_year_channel(sales: pd.DataFrame) -> pd.DataFrame:
    df = sales.copy()
    df["Channel"] = df["Is Online"].map({True: "Online", False: "In-Store"})
    return df.groupby(["Order Date Year", "Channel"])["Revenue USD"].sum().reset_index()


def yoy_by_country(sales: pd.DataFrame, customers: pd.DataFrame) -> pd.DataFrame:
    df = revenue_by_year_country(sales, customers)
    df = df.sort_values(["Country", "Order Date Year"])
    df["Prev Revenue"] = df.groupby("Country")["Revenue USD"].shift(1)
    df["YoY Growth Pct"] = ((df["Revenue USD"] - df["Prev Revenue"]) / df["Prev Revenue"] * 100).round(2)
    return df.dropna(subset=["YoY Growth Pct"])


def yoy_by_category(sales: pd.DataFrame, products: pd.DataFrame) -> pd.DataFrame:
    df = revenue_by_year_category(sales, products)
    df = df.sort_values(["Category", "Order Date Year"])
    df["Prev Revenue"] = df.groupby("Category")["Revenue USD"].shift(1)
    df["YoY Growth Pct"] = ((df["Revenue USD"] - df["Prev Revenue"]) / df["Prev Revenue"] * 100).round(2)
    return df.dropna(subset=["YoY Growth Pct"])


def seasonal_by_category(sales: pd.DataFrame, products: pd.DataFrame) -> pd.DataFrame:
    df = sales.merge(products[["ProductKey", "Category"]], on="ProductKey", how="left")
    return df.groupby(["Order Date Quarter", "Category"])["Revenue USD"].sum().unstack().fillna(0).round(2)


def q4_lift(sales: pd.DataFrame) -> pd.DataFrame:
    df = sales[sales["Order Date Year"] < 2021].copy()
    df["Is Q4"] = df["Order Date Quarter"] == 4
    q4 = df[df["Is Q4"]].groupby("Order Date Year")["Revenue USD"].sum()
    rest = df[~df["Is Q4"]].groupby("Order Date Year")["Revenue USD"].sum() / 3
    result = pd.DataFrame({"Q4 Revenue": q4, "Avg Other Quarter": rest})
    result["Q4 Lift Pct"] = ((result["Q4 Revenue"] - result["Avg Other Quarter"]) / result["Avg Other Quarter"] * 100).round(2)
    return result