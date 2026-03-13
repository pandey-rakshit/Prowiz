import pandas as pd
import logging

log = logging.getLogger(__name__)

FUTURE_DATE_COLS = {
    "sales"    : ["Order Date", "Delivery Date"],
    "customers": ["Birthday"],
}


def run(name: str, df: pd.DataFrame, reference_date: pd.Timestamp) -> list:
    results = []
    cols = FUTURE_DATE_COLS.get(name, [])

    for col in cols:
        if col not in df.columns:
            continue
        valid = df[col].dropna()
        mask  = valid > reference_date
        count = int(mask.sum())
        pct   = round(count / len(df) * 100, 2)
        result = {
            "dataset": name,
            "column" : col,
            "future_count": count,
            "future_pct"  : pct,
        }
        results.append(result)
        if count:
            log.warning("%s.%s has %d future dates (%.2f%%)", name, col, count, pct)
        else:
            log.info("%s.%s future date check: ok", name, col)

    return results