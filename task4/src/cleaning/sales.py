import pandas as pd
from src.utils.helpers import parse_dates, drop_nulls, add_elapsed_days, add_date_parts
from config.settings import DATASET_END_DATE, BULK_ORDER_THRESHOLD, ONLINE_STORE_KEY

# CRITICAL CORRECTION — Is Online derivation:
# Original assumption: null Delivery Date = online order. WRONG.
# Verified by cross-checking StoreKey against stores table (check_online_consistency.py).
# Actual logic:
#   - Physical store purchase: customer takes item home immediately — no delivery date.
#   - Online order: item is shipped to customer — always has a delivery date.
# Is Online must be derived from StoreKey == 0 (authoritative source: stores table).
# See docs/cleaning_decisions.md

# Is Delivery Pending: 82 rows (0.13%) have Delivery Date > DATASET_END_DATE.
# These are online orders (StoreKey=0) placed before cutoff, not yet delivered.
# Delivery Days nulled for these rows — time cannot be computed.

# Outlier: 1,808 rows (2.88%) have Quantity >= 9 (IQR upper bound 8.5).
# Kept. Flagged as Is Bulk Order for separate analysis.



def _add_online_flag(df: pd.DataFrame) -> pd.DataFrame:
    df = df.copy()
    df["Is Online"] = df["StoreKey"] == ONLINE_STORE_KEY
    return df


def _add_delivery_pending_flag(df: pd.DataFrame) -> pd.DataFrame:
    df = df.copy()
    cutoff = pd.Timestamp(DATASET_END_DATE)
    df["Is Delivery Pending"] = (
        df["Delivery Date"].notna() & (df["Delivery Date"] > cutoff)
    )
    return df


def _add_bulk_order_flag(df: pd.DataFrame) -> pd.DataFrame:
    df = df.copy()
    df["Is Bulk Order"] = df["Quantity"] >= BULK_ORDER_THRESHOLD
    return df


def _join_unit_price(df: pd.DataFrame, products: pd.DataFrame) -> pd.DataFrame:
    price_lookup = products[["ProductKey", "Unit Price USD"]]
    return df.merge(price_lookup, on="ProductKey", how="left")


def clean(df: pd.DataFrame, products: pd.DataFrame) -> pd.DataFrame:
    df = parse_dates(df, ["Order Date", "Delivery Date"])
    df = _add_online_flag(df)
    df = _add_delivery_pending_flag(df)
    df = _add_bulk_order_flag(df)
    df = add_elapsed_days(df, "Order Date", "Delivery Date", "Delivery Days")
    df.loc[df["Is Delivery Pending"], "Delivery Days"] = None
    df = add_date_parts(df, date_col="Order Date", parts=["year", "month", "quarter"])
    df = _join_unit_price(df, products)
    df = drop_nulls(df, subset=["Order Number", "CustomerKey", "ProductKey", "StoreKey", "Order Date"])
    return df