import pandas as pd
from src.utils.helpers import strip_currency, to_numeric, drop_nulls, add_ratio
from config.settings import PREMIUM_PRICE_CUTOFF
from config.schema import PRICE_COLS

# Outlier decision: 200 products (7.95%) have Unit Price USD > $921.50 (IQR upper bound).
# 183 products (7.27%) have Unit Cost USD > $411.50 (IQR upper bound).
# These are the same SKUs — legitimate high-end desktops and TVs.
# Decision: Keep. Flag as Is Premium Product for separate segment analysis.
# Threshold: Unit Price USD > 921.50 (IQR upper bound from Phase 2 outlier check).
# See docs/cleaning_decisions.md


def _add_margin_usd(df: pd.DataFrame) -> pd.DataFrame:
    df = df.copy()
    df["Margin USD"] = df["Unit Price USD"] - df["Unit Cost USD"]
    return df


def _add_premium_flag(df: pd.DataFrame) -> pd.DataFrame:
    df = df.copy()
    df["Is Premium Product"] = df["Unit Price USD"] > PREMIUM_PRICE_CUTOFF
    return df


def clean(df: pd.DataFrame) -> pd.DataFrame:
    df = strip_currency(df, PRICE_COLS)
    df = to_numeric(df, PRICE_COLS)
    df = _add_margin_usd(df)
    df = add_ratio(df, numerator="Margin USD", denominator="Unit Price USD", new_col="Margin Pct", scale=100)
    df = _add_premium_flag(df)
    df = drop_nulls(df, subset=["ProductKey", "Unit Cost USD", "Unit Price USD"])
    return df