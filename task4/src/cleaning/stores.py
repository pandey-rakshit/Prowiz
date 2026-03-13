import pandas as pd
from src.utils.helpers import parse_dates, to_numeric, drop_nulls, add_elapsed_years

# Decision: Square Meters is null for 1 store (1.49%).
# Row is kept. Is Online Store flag added.
# See docs/cleaning_decisions.md


def _add_online_store_flag(df: pd.DataFrame) -> pd.DataFrame:
    df = df.copy()
    df["Is Online Store"] = df["Square Meters"].isna()
    return df


def clean(df: pd.DataFrame) -> pd.DataFrame:
    df = parse_dates(df, ["Open Date"])
    df = to_numeric(df, ["Square Meters"])
    df = _add_online_store_flag(df)
    df = add_elapsed_years(df, date_col="Open Date", new_col="Store Age Years")
    df = drop_nulls(df, subset=["StoreKey", "Country"])
    return df