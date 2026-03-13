"""
Check whether the 82 rows with Delivery Date > DATASET_END_DATE
belong to a single store or multiple stores.

If all 82 belong to StoreKey 0 (online store) — makes sense.
Online orders placed just before cutoff may still be in transit.

If they belong to physical stores — unexpected, needs investigation.

Run from project root: python check_pending_deliveries.py
"""

import pandas as pd
from config.settings import DATASET_END_DATE, ONLINE_STORE_KEY
from config.paths import PROCESSED_FILES


def main():
    sales  = pd.read_parquet(PROCESSED_FILES["sales"])
    stores = pd.read_parquet(PROCESSED_FILES["stores"])

    cutoff  = pd.Timestamp(DATASET_END_DATE)
    pending = sales[sales["Delivery Date"] > cutoff].copy()

    print(f"Total rows with Delivery Date > {DATASET_END_DATE} : {len(pending)}")
    print()

    # which stores do these belong to
    store_counts = (
        pending.groupby("StoreKey")
        .size()
        .reset_index(name="row_count")
        .merge(stores[["StoreKey", "Country", "Is Online Store"]], on="StoreKey", how="left")
        .sort_values("row_count", ascending=False)
    )

    print("Breakdown by store:")
    print(store_counts.to_string(index=False))
    print()

    online_pending   = pending[pending["StoreKey"] == ONLINE_STORE_KEY]
    physical_pending = pending[pending["StoreKey"] != ONLINE_STORE_KEY]

    print(f"Online store  (StoreKey={ONLINE_STORE_KEY}) : {len(online_pending)} rows")
    print(f"Physical stores                             : {len(physical_pending)} rows")

    if len(physical_pending) > 0:
        print()
        print("UNEXPECTED — physical stores have future delivery dates:")
        print(physical_pending[["Order Number", "StoreKey", "Order Date", "Delivery Date"]].head(10))


if __name__ == "__main__":
    main()