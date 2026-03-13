import logging

from src.loader import load_all
from config.paths import PROCESSED_FILES

from src.cleaning import customers, sales, products, exchange_rates, stores
from src.transform import currency

logging.basicConfig(level=logging.INFO, format="%(levelname)s | %(message)s")
log = logging.getLogger(__name__)


def _save(df, key: str):
    path = PROCESSED_FILES[key]
    path.parent.mkdir(parents=True, exist_ok=True)
    df.to_parquet(path, index=False)
    log.info("saved %s -> %s  shape=%s", key, path.name, df.shape)


def main():
    raw = load_all()

    clean_products       = products.clean(raw["products"])
    clean_customers      = customers.clean(raw["customers"])
    clean_exchange_rates = exchange_rates.clean(raw["exchange_rates"])
    clean_stores         = stores.clean(raw["stores"])
    clean_sales          = sales.clean(raw["sales"], clean_products)

    _save(clean_customers,      "customers")
    _save(clean_products,       "products")
    _save(clean_exchange_rates, "exchange_rates")
    _save(clean_stores,         "stores")

    sales_with_revenue = currency.apply(clean_sales, clean_exchange_rates)
    _save(sales_with_revenue, "sales")

    log.info("phase 3 complete")


if __name__ == "__main__":
    main()