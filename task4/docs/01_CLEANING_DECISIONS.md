# Data Cleaning Decisions

Source: Phase 2 validation — `outputs/reports/phase2_validation.json`
Dataset date range: 2016-01-01 to 2021-02-20

---

## 1. Null Handling

### customers — State Code
| Nulls | Null % | Decision | Reason |
|-------|--------|----------|--------|
| 10 | 0.07% | Keep rows, leave null | Negligible volume. Not used in any key analysis. |

### sales — Delivery Date
| Nulls | Null % | Decision | Reason |
|-------|--------|----------|--------|
| 49,719 | 79.06% | Keep rows | Structural — physical store customers take items home immediately. No shipping occurs. |

- Physical store orders (49,719) → null Delivery Date → no Delivery Days. Expected and correct.
- Online orders (13,165) → always have a Delivery Date → Delivery Days computed.

### stores — Square Meters
| Nulls | Null % | Decision | Reason |
|-------|--------|----------|--------|
| 1 | 1.49% | Keep row, add Is Online Store flag | Single row with no physical size — this is the online store entry (StoreKey=0). |

### products / exchange_rates
No nulls found. No action required.

---

## 2. Duplicate and Referential Integrity Checks

| Check | Result | Action |
|-------|--------|--------|
| Duplicates (all datasets) | 0 duplicate rows | None |
| Sales to Customers FK | 0 orphans | None |
| Sales to Products FK | 0 orphans | None |
| Sales to Stores FK | 0 orphans | None |
| Date coverage (sales vs exchange rates) | Fully covered | None |

---

## 3. Data Type Fixes

### products — Unit Cost USD and Unit Price USD
Raw values contain dollar symbol (e.g. $6.62). pd.to_numeric() coerces these to NaN silently.
- Fix: helpers.strip_currency() applied before to_numeric() in clean/products.py.
- Discovered during Phase 3 run — products_clean.parquet was returning 0 rows.

---

## 4. Additional Validation Checks

| Check | Columns | Result | Action |
|-------|---------|--------|--------|
| Negative values | sales.Quantity, products.Unit Cost USD, products.Unit Price USD | 0 violations | None |
| Delivery before order date | sales.Order Date, Delivery Date | 0 violations | None |
| Future dates — Order Date | sales.Order Date | 0 violations | None |
| Future dates — Birthday | customers.Birthday | 0 violations | None |
| Future dates — Delivery Date | sales.Delivery Date | 82 rows (0.13%) | Flag as Is Delivery Pending |

### Is Delivery Pending — 82 rows
- 82 online orders placed before 2021-02-20 with Delivery Date beyond the dataset cutoff.
- These are real in-transit orders — dataset was cut off before delivery completed.
- Decision: Keep rows. Add Is Delivery Pending = True flag. Set Delivery Days = null for these rows.
- Reference date: DATASET_END_DATE = 2021-02-20 stored in config/settings.py.

---

## 5. Range Checks (Post-Clean, Phase 3)

Applied after cleaning on derived columns. All passed.

| Dataset | Column | Valid Range | Violations |
|---------|--------|-------------|------------|
| sales | Delivery Days | 1-30 | 0 |
| customers | Age | 18-100 | 0 |
| products | Margin Pct | 0-100 | 0 |

---

## 6. Outlier Detection (IQR Method)

| Dataset | Column | Outlier Count | Outlier % | Outlier Range | Decision |
|---------|--------|--------------|-----------|---------------|----------|
| products | Unit Price USD | 200 | 7.95% | $967-$3,199 | Keep. Legitimate high-end products. Flag as Is Premium Product. |
| products | Unit Cost USD | 183 | 7.27% | $413-$1,060 | Keep. Same SKUs as price outliers. No separate flag needed. |
| sales | Quantity | 1,808 | 2.88% | 9-10 units | Keep. Max is 10. Real bulk order pattern. Flag as Is Bulk Order. |
| stores | Square Meters | 0 | 0% | — | None |

### Is Premium Product (products)
- Is Premium Product = True where Unit Price USD > 921.50
- 921.50 is the IQR upper bound from Phase 2 outlier check
- Covers 200 products (7.95%) — high-end desktops and large-screen TVs
- Cost outliers (183 rows) are the same SKUs — no separate flag needed
- Threshold: PREMIUM_PRICE_CUTOFF = 921.50 in config/settings.py

### Is Bulk Order (sales)
- Is Bulk Order = True where Quantity >= 9
- 9 is one above the IQR upper bound of 8.5
- Covers 1,808 rows (2.88%) — max quantity in dataset is 10
- Threshold: BULK_ORDER_THRESHOLD = 9 in config/settings.py

---

## 7. Derived Flags Added

### sales
| Flag | Logic | Source |
|------|-------|--------|
| Is Online | StoreKey == ONLINE_STORE_KEY | stores table — authoritative source |
| Is Delivery Pending | Delivery Date > DATASET_END_DATE | dataset cutoff |
| Is Bulk Order | Quantity >= BULK_ORDER_THRESHOLD | IQR outlier bound |

### stores
| Flag | Logic |
|------|-------|
| Is Online Store | Square Meters is null — StoreKey 0 is the only online store |

### products
| Flag | Logic |
|------|-------|
| Is Premium Product | Unit Price USD > PREMIUM_PRICE_CUTOFF |

---

## 8. Is Online — Correction

Initial implementation derived Is Online from null Delivery Date. This was incorrect.

Verified by check_online_consistency.py cross-tabulation:
- Physical store orders (49,719) → null Delivery Date → customer collects in store → no delivery
- Online orders (13,165) → always have Delivery Date → item is shipped to customer

Is Online is now derived from StoreKey == ONLINE_STORE_KEY which is the authoritative source.
ONLINE_STORE_KEY = 0 stored in config/settings.py.

Charts affected — re-run required on sales notebook:
- Online vs In-Store order count (labels were swapped)
- Online vs In-Store revenue (labels were swapped)
- Delivery days distribution (was filtered on wrong channel)

---

## 9. Constants in config/settings.py

| Constant | Value | Purpose |
|----------|-------|---------|
| DATASET_END_DATE | 2021-02-20 | Reference date for pending delivery detection |
| ONLINE_STORE_KEY | 0 | StoreKey of the single online store |
| PREMIUM_PRICE_CUTOFF | 921.50 | IQR upper bound for premium product flag |
| BULK_ORDER_THRESHOLD | 9 | IQR upper bound + 1 for bulk order flag |