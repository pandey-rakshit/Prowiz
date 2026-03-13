import pandas as pd


def run(
    sales_df   : pd.DataFrame,
    rates_df   : pd.DataFrame,
    sales_col  : str = "Order Date",
    rates_col  : str = "Date",
) -> dict:
    s_min, s_max = sales_df[sales_col].min(), sales_df[sales_col].max()
    r_min, r_max = rates_df[rates_col].min(),  rates_df[rates_col].max()

    return {
        "sales_range"  : f"{s_min.date()} to {s_max.date()}",
        "rates_range"  : f"{r_min.date()} to {r_max.date()}",
        "fully_covered": bool((r_min <= s_min) and (r_max >= s_max)),
    }