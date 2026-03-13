import pandas as pd
import logging

log = logging.getLogger(__name__)

NEGATIVE_CHECKS = {
    "sales"   : ["Quantity"],
    "products": ["Unit Cost USD", "Unit Price USD"],
}


def _to_numeric_safe(series: pd.Series) -> pd.Series:
    cleaned = series.astype(str).str.replace(r"[$,£€\s]", "", regex=True)
    return pd.to_numeric(cleaned, errors="coerce")


def run(name: str, df: pd.DataFrame) -> list:
    results = []
    cols = NEGATIVE_CHECKS.get(name, [])

    for col in cols:
        if col not in df.columns:
            continue
        numeric = _to_numeric_safe(df[col])
        mask    = numeric < 0
        count   = int(mask.sum())
        pct     = round(count / len(df) * 100, 2)
        result  = {
            "dataset"       : name,
            "column"        : col,
            "negative_count": count,
            "negative_pct"  : pct,
        }
        results.append(result)
        if count:
            log.warning("%s.%s has %d negative values (%.2f%%)", name, col, count, pct)
        else:
            log.info("%s.%s negative check: ok", name, col)

    return results