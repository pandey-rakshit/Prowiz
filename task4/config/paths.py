
from pathlib import Path

ROOT_DIR    = Path(__file__).parent.parent
DATA_RAW    = ROOT_DIR / "data" / "raw"
DATA_PROC   = ROOT_DIR / "data" / "processed"
OUTPUTS     = ROOT_DIR / "outputs"
CHARTS_DIR  = OUTPUTS / "charts"
REPORTS_DIR = OUTPUTS / "reports"
LOGS_DIR    = ROOT_DIR / "logs"

RAW_FILES = {
    "customers"      : DATA_RAW / "Customers.csv",
    "data_dictionary": DATA_RAW / "Data_Dictionary.csv",
    "exchange_rates" : DATA_RAW / "Exchange_Rates.csv",
    "products"       : DATA_RAW / "Products.csv",
    "sales"          : DATA_RAW / "Sales.csv",
    "stores"         : DATA_RAW / "Stores.csv",
}

PROCESSED_FILES = {
    "customers"     : DATA_PROC / "customers_clean.parquet",
    "exchange_rates": DATA_PROC / "exchange_rates_clean.parquet",
    "products"      : DATA_PROC / "products_clean.parquet",
    "sales"         : DATA_PROC / "sales_clean.parquet",
    "stores"        : DATA_PROC / "stores_clean.parquet",
    "master"        : DATA_PROC / "master_fact.parquet",
}