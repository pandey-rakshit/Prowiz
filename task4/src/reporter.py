import json
import pandas as pd
from config.paths import REPORTS_DIR


def print_header(title: str):
    print(f"\n{'─' * 55}\n  {title}\n{'─' * 55}")


def print_load_summary(datasets: dict):
    print_header("datasets loaded")
    for name, df in datasets.items():
        print(f"  {name:<20} rows={df.shape[0]:>7,}  cols={df.shape[1]}")


def print_schema(report: dict):
    if not report["schema_issues"]:
        print("\n  schema: all ok")
        return
    print("\n  schema issues:")
    for ds, issues in report["schema_issues"].items():
        for issue in issues:
            print(f"    [{ds}] {issue}")


def print_nulls_dupes_fk(report: dict):
    if not report["null_reports"]:
        print("\n  nulls: none found")
    else:
        print("\n  null report:")
        for name, df in report["null_reports"].items():
            print(f"\n    [{name}]\n{df.to_string(index=False)}")

    print("\n  duplicates:")
    for name, d in report["duplicates"].items():
        print(f"    {name:<20} {d['duplicate_rows']:>5} rows  [{'FOUND' if d['duplicate_rows'] else 'none'}]")

    if report["fk_checks"]:
        print("\n  foreign key checks:")
        for fk in report["fk_checks"]:
            status = "ok" if fk["orphan_count"] == 0 else f"orphans: {fk['orphan_count']}"
            print(f"    {fk['check']:<30} {status}")


def print_date_coverage(report: dict):
    cov = report.get("date_coverage")
    if not cov:
        return
    print(f"\n  date coverage:\n    sales: {cov['sales_range']}\n    rates: {cov['rates_range']}\n    covered: {cov['fully_covered']}")


def print_negative_and_delivery(report: dict):
    print("\n  negative value checks:")
    for r in report["negative_checks"]:
        status = f"FOUND {r['negative_count']} rows ({r['negative_pct']}%)" if r["negative_count"] else "ok"
        print(f"    {r['dataset']}.{r['column']:<25} {status}")
    dc = report.get("delivery_check")
    if dc:
        status = f"FOUND {dc['invalid_delivery_count']} rows ({dc['invalid_delivery_pct']}%)" if dc["invalid_delivery_count"] else "ok"
        print(f"\n  delivery date check: {status}")


def print_range_and_future(report: dict):
    print("\n  future date checks:")
    for r in report["future_date_checks"]:
        status = f"FOUND {r['future_count']} rows ({r['future_pct']}%)" if r["future_count"] else "ok"
        print(f"    {r['dataset']}.{r['column']:<25} {status}")
    print("\n  range checks:")
    for r in report["range_checks"]:
        status = f"FOUND {r['violation_count']} rows ({r['violation_pct']}%) outside {r['range']}" if r["violation_count"] else "ok"
        print(f"    {r['dataset']}.{r['column']:<25} {status}")


def print_outliers(report: dict):
    print("\n  outlier checks:")
    for r in report["outlier_checks"]:
        status = f"FOUND {r['outlier_count']} rows ({r['outlier_pct']}%) bounds=[{r['lower_bound']}, {r['upper_bound']}]" if r["outlier_count"] else "ok"
        print(f"    {r['dataset']}.{r['column']:<25} {status}")


def save_report(report: dict):
    REPORTS_DIR.mkdir(parents=True, exist_ok=True)
    path = REPORTS_DIR / "phase2_validation.json"
    serialisable = {}
    for k, v in report.items():
        if isinstance(v, dict) and any(isinstance(d, pd.DataFrame) for d in v.values()):
            serialisable[k] = {n: d.to_dict(orient="records") for n, d in v.items()}
        else:
            serialisable[k] = v
    with open(path, "w") as f:
        json.dump(serialisable, f, indent=2, default=str)
    print(f"\n  report saved: {path}")