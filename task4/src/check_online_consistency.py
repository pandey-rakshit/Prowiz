"""
Verify consistency between two ways of identifying online orders:
  1. Is Online flag in sales (derived from null Delivery Date)
  2. StoreKey == 0 (the single online store in stores table)

These must agree 100%. Any mismatch means our Is Online flag is wrong.
Run from project root: python check_online_consistency.py
"""

import pandas as pd
from config.paths import PROCESSED_FILES


def main():
    sales  = pd.read_parquet(PROCESSED_FILES["sales"])
    stores = pd.read_parquet(PROCESSED_FILES["stores"])

    online_store_keys = stores[stores["Is Online Store"] == True]["StoreKey"].tolist()
    print(f"Online store StoreKeys in stores table : {online_store_keys}")
    print(f"Total sales rows                       : {len(sales):,}")
    print()

    sales["_via_storekey"] = sales["StoreKey"].isin(online_store_keys)

    ct = pd.crosstab(
        sales["Is Online"],
        sales["_via_storekey"],
        rownames=["Is Online (null Delivery Date)"],
        colnames=["StoreKey is online store"],
        margins=True,
    )
    print("Cross-tabulation:")
    print(ct)
    print()

    mismatch_a = sales[(sales["Is Online"] == True)  & (sales["_via_storekey"] == False)]
    mismatch_b = sales[(sales["Is Online"] == False) & (sales["_via_storekey"] == True)]

    print(f"MISMATCH A — Is Online=True  but StoreKey is NOT online store : {len(mismatch_a):,} rows")
    print(f"MISMATCH B — Is Online=False but StoreKey IS  online store    : {len(mismatch_b):,} rows")
    print()

    if len(mismatch_a) == 0 and len(mismatch_b) == 0:
        print("RESULT: flags are fully consistent — null Delivery Date always matches StoreKey 0")
        print("ACTION: no changes needed")
    else:
        print("RESULT: INCONSISTENCY FOUND — flags do not agree")
        print("ACTION: Is Online should be derived from StoreKey, not Delivery Date")
        if len(mismatch_a):
            print(f"\nSample mismatch A (first 5):")
            print(mismatch_a[["Order Number", "StoreKey", "Delivery Date", "Is Online"]].head())
        if len(mismatch_b):
            print(f"\nSample mismatch B (first 5):")
            print(mismatch_b[["Order Number", "StoreKey", "Delivery Date", "Is Online"]].head())


if __name__ == "__main__":
    main()