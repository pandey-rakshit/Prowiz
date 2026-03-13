import pandas as pd
import logging

log = logging.getLogger(__name__)

OUTLIER_COLS = {
    "sales"   : ["Quantity", "Revenue USD"],
    "products": ["Unit Price USD", "Unit Cost USD"],
    "stores"  : ["Square Meters"],
}


def _to_numeric_safe(series: pd.Series) -> pd.Series:
    cleaned = series.astype(str).str.replace(r"[$,£€\s]", "", regex=True)
    return pd.to_numeric(cleaned, errors="coerce")


def _iqr_bounds(series: pd.Series) -> tuple:
    q1  = series.quantile(0.25)
    q3  = series.quantile(0.75)
    iqr = q3 - q1
    return q1 - 1.5 * iqr, q3 + 1.5 * iqr


def _check_col(name: str, df: pd.DataFrame, col: str) -> dict:
    series       = _to_numeric_safe(df[col]).dropna()
    low, high    = _iqr_bounds(series)
    mask         = (series < low) | (series > high)
    count        = int(mask.sum())
    pct          = round(count / len(df) * 100, 2)
    outliers     = series[mask]

    result = {
        "dataset"      : name,
        "column"       : col,
        "lower_bound"  : round(low, 2),
        "upper_bound"  : round(high, 2),
        "outlier_count": count,
        "outlier_pct"  : pct,
        "outlier_min"  : round(outliers.min(), 2) if count else None,
        "outlier_max"  : round(outliers.max(), 2) if count else None,
    }

    if count:
        log.warning("%s.%s: %d outliers (%.2f%%) bounds=[%.2f, %.2f]", name, col, count, pct, low, high)
    else:
        log.info("%s.%s outlier check: ok", name, col)

    return result


def run(name: str, df: pd.DataFrame) -> list:
    cols = OUTLIER_COLS.get(name, [])
    return [_check_col(name, df, col) for col in cols if col in df.columns]