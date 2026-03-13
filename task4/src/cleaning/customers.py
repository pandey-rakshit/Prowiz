import pandas as pd
from src.utils.helpers import parse_dates, drop_nulls, add_age, add_bins

# Decision: State Code nulls (10 rows, 0.07%) are kept.
# See docs/cleaning_decisions.md

AGE_BINS   = [0, 25, 35, 50, 65, 120]
AGE_LABELS = ["<25", "25-34", "35-49", "50-64", "65+"]


def clean(df: pd.DataFrame) -> pd.DataFrame:
    df = parse_dates(df, ["Birthday"])
    df = add_age(df, date_col="Birthday", new_col="Age")
    df = add_bins(df, col="Age", bins=AGE_BINS, labels=AGE_LABELS, new_col="Age Group")
    df = drop_nulls(df, subset=["CustomerKey", "Gender", "Country"])
    return df