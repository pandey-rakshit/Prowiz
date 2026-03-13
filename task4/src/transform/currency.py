import logging
import pandas as pd

log = logging.getLogger(__name__)

# Unit Price USD is carried forward from clean/sales.py.
# Date coverage is fully covered per Phase 2 validation.
# Any unmatched row after merge is unexpected — raises instead of silently dropping.


def _merge_exchange_rate(sales: pd.DataFrame, rates: pd.DataFrame) -> pd.DataFrame:
    rates_lookup = rates[["Date", "Currency", "Exchange"]].rename(
        columns={"Date": "Order Date", "Currency": "Currency Code"}
    )
    return sales.merge(rates_lookup, on=["Order Date", "Currency Code"], how="left")


def _compute_revenue(df: pd.DataFrame) -> pd.DataFrame:
    df = df.copy()
    df["Revenue USD"] = (df["Quantity"] * df["Unit Price USD"] / df["Exchange"]).round(2)
    return df


def _assert_no_missing_revenue(df: pd.DataFrame) -> None:
    missing = df["Revenue USD"].isna().sum()
    if missing:
        raise ValueError(f"{missing} rows have no Revenue USD — check exchange rate coverage")


def apply(sales: pd.DataFrame, rates: pd.DataFrame) -> pd.DataFrame:
    df = _merge_exchange_rate(sales, rates)
    df = _compute_revenue(df)
    _assert_no_missing_revenue(df)
    return df