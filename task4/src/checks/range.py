import pandas as pd
import logging

log = logging.getLogger(__name__)

RANGES = {
    "sales"    : {"Delivery Days": (1, 30)},
    "customers": {"Age"          : (18, 100)},
    "products" : {"Margin Pct"   : (0, 100)},
}


def run(name: str, df: pd.DataFrame) -> list:
    results = []
    cols = RANGES.get(name, {})

    for col, (low, high) in cols.items():
        if col not in df.columns:
            continue
        valid = df[col].dropna()
        mask  = (valid < low) | (valid > high)
        count = int(mask.sum())
        pct   = round(count / len(df) * 100, 2)
        result = {
            "dataset"        : name,
            "column"         : col,
            "range"          : f"{low} to {high}",
            "violation_count": count,
            "violation_pct"  : pct,
        }
        results.append(result)
        if count:
            log.warning("%s.%s: %d range violations (%.2f%%) outside [%s, %s]", name, col, count, pct, low, high)

    return results