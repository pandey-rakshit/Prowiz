import logging

from loader    import load_all
from validator import run_all
from reporter  import (
    print_header,
    print_load_summary,
    print_schema,
    print_nulls_dupes_fk,
    print_date_coverage,
    print_negative_and_delivery,
    print_range_and_future,
    print_outliers,
    save_report,
)

logging.basicConfig(level=logging.WARNING, format="%(levelname)s | %(message)s")


def main():
    print_header("phase 2 - ingestion and validation")

    datasets = load_all()
    if not datasets:
        print("  no datasets found - place CSVs in data/raw/")
        return

    print_load_summary(datasets)
    report = run_all(datasets)

    print_header("validation results")
    print_schema(report)
    print_nulls_dupes_fk(report)
    print_date_coverage(report)
    print_negative_and_delivery(report)
    print_range_and_future(report)
    print_outliers(report)

    save_report(report)
    print_header("phase 2 complete")


if __name__ == "__main__":
    main()