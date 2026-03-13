BASE_CURRENCY    = "USD"
PLOT_THEME       = "whitegrid"
PLOT_PALETTE     = "Set2"
PLOTLY_THEME     = "plotly_white"
FIG_SIZE         = (14, 6)
DPI              = 150

# Last Order Date in dataset — used as reference for pending delivery detection
DATASET_END_DATE = "2021-02-20"

# Outlier thresholds — derived from IQR bounds in Phase 2 outlier check
# Products: Unit Price USD IQR upper bound = 921.50
PREMIUM_PRICE_CUTOFF  = 921.50
 
# Sales: Quantity IQR upper bound = 8.5 — bulk orders defined as >= 9
BULK_ORDER_THRESHOLD  = 9

# StoreKey for the single online store — verified against stores table
ONLINE_STORE_KEY = 0