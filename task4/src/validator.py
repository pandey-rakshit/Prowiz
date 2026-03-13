import logging
from config.schema import FK_PAIRS
from src.checks import schema, null, duplicate, foreign_key, date, negative, delivery, future_date, range, outlier

log = logging.getLogger(__name__)

DATASET_END_DATE = "2021-02-20"


def _run_schema(datasets: dict, report: dict):
    for name, df in datasets.items():
        issues = schema.run(name, df)
        if issues:
            report["schema_issues"][name] = issues
        log.info("%s schema: %s", name, "ok" if not issues else issues)


def _run_nulls_and_dupes(datasets: dict, report: dict):
    for name, df in datasets.items():
        nulls = null.run(name, df)
        if not nulls.empty:
            report["null_reports"][name] = nulls
        dupes = duplicate.run(name, df)
        report["duplicates"][name] = dupes
        if dupes["duplicate_rows"]:
            log.warning("%s has %d duplicate rows", name, dupes["duplicate_rows"])


def _run_fk_checks(datasets: dict, report: dict):
    required = {"sales", "customers", "products", "stores"}
    if not required.issubset(datasets.keys()):
        return
    for child_name, child_col, parent_name, parent_col, label in FK_PAIRS:
        result = foreign_key.run(
            datasets[child_name], child_col,
            datasets[parent_name], parent_col,
            label,
        )
        report["fk_checks"].append(result)
        log.info("fk %s: %d orphans", label, result["orphan_count"])


def _run_date_coverage(datasets: dict, report: dict):
    if "sales" not in datasets or "exchange_rates" not in datasets:
        return
    result = date.run(datasets["sales"], datasets["exchange_rates"])
    report["date_coverage"] = result


def _run_new_checks(datasets: dict, report: dict):
    import pandas as pd
    ref_date = pd.Timestamp(DATASET_END_DATE)

    for name, df in datasets.items():
        report["negative_checks"].extend(negative.run(name, df))
        report["future_date_checks"].extend(future_date.run(name, df, ref_date))
        report["range_checks"].extend(range.run(name, df))
        report["outlier_checks"].extend(outlier.run(name, df))

    if "sales" in datasets:
        report["delivery_check"] = delivery.run(datasets["sales"])


def run_all(datasets: dict) -> dict:
    report = {
        "schema_issues"     : {},
        "null_reports"      : {},
        "duplicates"        : {},
        "fk_checks"         : [],
        "date_coverage"     : {},
        "negative_checks"   : [],
        "future_date_checks": [],
        "range_checks"      : [],
        "outlier_checks"    : [],
        "delivery_check"    : {},
    }
    _run_schema(datasets, report)
    _run_nulls_and_dupes(datasets, report)
    _run_fk_checks(datasets, report)
    _run_date_coverage(datasets, report)
    _run_new_checks(datasets, report)
    return report