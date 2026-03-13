# Phase 3 — Cleaning Pipeline Execution

Date: 2026-03-12
Script: `run_phase3.py`

---

# Objective

Phase 3 performs **data cleaning and feature engineering** based on validation decisions from Phase 2.

The output of this phase is a set of **cleaned parquet datasets** used for analysis.


---

## Load Summary

| Dataset        | Shape       | Encoding |
|----------------|-------------|----------|
| customers      | (15266, 10) | latin-1  |
| data_dictionary| (37, 3)     | utf-8    |
| exchange_rates | (11215, 3)  | utf-8    |
| products       | (2517, 10)  | utf-8    |
| sales          | (62884, 9)  | utf-8    |
| stores         | (67, 5)     | utf-8    |

Note: data_dictionary is a reference file. Not cleaned or saved to parquet.

---

## Clean Summary

| Dataset        | Raw Shape   | Clean Shape | Rows Dropped | Columns Added                                                                 |
|----------------|-------------|-------------|--------------|-------------------------------------------------------------------------------|
| customers      | (15266, 10) | (15266, 12) | 0            | Age, Age Group                                                                |
| products       | (2517, 10)  | (2517, 12)  | 0            | Margin USD, Margin Pct                                                        |
| exchange_rates | (11215, 3)  | (11215, 3)  | 0            | none — dates parsed only                                                      |
| stores         | (67, 5)     | (67, 7)     | 0            | Store Age Years, Is Online Store                                              |
| sales          | (62884, 9)  | (62884, 17) | 0            | Is Online, Delivery Days, Order Date Year, Order Date Month, Order Date Quarter, Unit Price USD, Revenue USD |

---

## Observations

- Zero rows dropped across all datasets — consistent with decisions in cleaning_decisions.md
- customers required latin-1 encoding due to special characters in name column (e.g. ü at byte 0xfc)
- products Unit Cost USD and Unit Price USD contained $ symbols — stripped before numeric conversion
- sales expanded from 9 to 17 columns — all 8 derived columns added correctly
- Revenue USD successfully computed for all 62,884 rows — no missing values

---

## Output Files

| File                          | Shape       | Location                    |
|-------------------------------|-------------|-----------------------------|
| customers_clean.parquet       | (15266, 12) | data/processed/             |
| products_clean.parquet        | (2517, 12)  | data/processed/             |
| exchange_rates_clean.parquet  | (11215, 3)  | data/processed/             |
| stores_clean.parquet          | (67, 7)     | data/processed/             |
| sales_clean.parquet           | (62884, 17) | data/processed/             |


