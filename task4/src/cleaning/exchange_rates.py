import pandas as pd
from src.utils.helpers import parse_dates, drop_nulls
from config.settings import BASE_CURRENCY


def _assert_usd_baseline(df: pd.DataFrame) -> None:
    usd = df[(df["Currency"] == BASE_CURRENCY) & (df["Exchange"] != 1.0)]
    if not usd.empty:
        raise ValueError(f"USD exchange rate is not 1.0 on {len(usd)} rows")


def clean(df: pd.DataFrame) -> pd.DataFrame:
    df = parse_dates(df, ["Date"])
    df = drop_nulls(df, subset=["Date", "Currency", "Exchange"])
    _assert_usd_baseline(df)
    return df