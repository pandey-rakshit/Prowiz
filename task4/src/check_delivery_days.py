"""
Check delivery days = Delivery Date - Order Date for online orders (StoreKey=0).
Excludes Is Delivery Pending rows — delivery not yet completed.

Run from project root: python check_delivery_days.py
"""
import pandas as pd
from config.settings import ONLINE_STORE_KEY
from config.paths import PROCESSED_FILES


def main():
    sales = pd.read_parquet(PROCESSED_FILES["sales"])

    online   = sales[sales["StoreKey"] == ONLINE_STORE_KEY].copy()
    complete = online[online["Is Delivery Pending"] == False].copy()

    print(f"Total online orders              : {len(online):,}")
    print(f"Pending (delivery not completed) : {len(online) - len(complete):,}")
    print(f"Complete (delivery confirmed)    : {len(complete):,}")
    print()

    # recompute just to be sure
    complete["_delivery_days"] = (
        complete["Delivery Date"] - complete["Order Date"]
    ).dt.days

    print("Delivery Days stats (online orders, completed only):")
    print(complete["_delivery_days"].describe().round(2))
    print()

    print("Value counts (each day):")
    vc = complete["_delivery_days"].value_counts().sort_index()
    print(vc.to_string())
    print()

    # flag anything unexpected
    zero_or_neg = complete[complete["_delivery_days"] <= 0]
    over_30     = complete[complete["_delivery_days"] > 30]

    print(f"Zero or negative delivery days : {len(zero_or_neg)}")
    print(f"Over 30 days                   : {len(over_30)}")

    if len(over_30):
        print("\nSample over 30 days:")
        print(over_30[["Order Number", "Order Date", "Delivery Date", "_delivery_days"]].head(10))


if __name__ == "__main__":
    main()