import pandas as pd
import logging

log = logging.getLogger(__name__)


def run(df: pd.DataFrame) -> dict:
    if "Order Date" not in df.columns or "Delivery Date" not in df.columns:
        return {}

    in_store  = df[df["Delivery Date"].notna()]
    mask      = in_store["Delivery Date"] < in_store["Order Date"]
    count     = int(mask.sum())
    pct       = round(count / len(in_store) * 100, 2)

    result = {
        "invalid_delivery_count": count,
        "invalid_delivery_pct"  : pct,
        "checked_rows"          : len(in_store),
    }

    if count:
        log.warning("sales: %d rows where Delivery Date < Order Date (%.2f%% of in-store)", count, pct)
    else:
        log.info("sales: delivery date order check ok")

    return result