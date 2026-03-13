# Phase 2 — Data Validation Results

Source report: `outputs/reports/phase2_validation.json`
Execution script: `src/run_phase2.py`

Dataset coverage:

2016-01-01 → 2021-02-20

Phase 2 performs **structural validation of raw datasets** before any cleaning or feature engineering is applied.

The goal is to detect:

* schema inconsistencies
* null values
* duplicates
* foreign key violations
* invalid dates
* negative numeric values
* statistical outliers
* delivery data inconsistencies

---

# 1. Schema Validation

No schema issues were detected.

All datasets matched the expected column definitions.

---

# 2. Null Value Analysis

| Dataset   | Column        | Null Count | Null % |
| --------- | ------------- | ---------- | ------ |
| customers | State Code    | 10         | 0.07%  |
| sales     | Delivery Date | 49,719     | 79.06% |
| stores    | Square Meters | 1          | 1.49%  |

### Interpretation

**customers — State Code**

* Very small volume (0.07%)
* Not used in joins or core analysis
* Safe to keep as null

**sales — Delivery Date**

* High null percentage (79.06%)
* Expected behavior

Explanation:

Physical store purchases are taken home immediately.
Only online orders require delivery.

| Order Type     | Delivery Date |
| -------------- | ------------- |
| Physical Store | Null          |
| Online Orders  | Present       |

**stores — Square Meters**

Only one null row.

Investigation shows this row corresponds to **StoreKey = 0**, which represents the **online store**.

---

# 3. Duplicate Detection

No duplicate rows were detected across any dataset.

| Dataset         | Duplicate Rows |
| --------------- | -------------- |
| customers       | 0              |
| data_dictionary | 0              |
| exchange_rates  | 0              |
| products        | 0              |
| sales           | 0              |
| stores          | 0              |

No deduplication was required.

---

# 4. Foreign Key Validation

Sales dataset foreign keys were validated against dimension tables.

| Relationship      | Orphan Rows |
| ----------------- | ----------- |
| Sales → Customers | 0           |
| Sales → Products  | 0           |
| Sales → Stores    | 0           |

All relationships are valid.

---

# 5. Date Coverage Validation

| Dataset        | Date Range              |
| -------------- | ----------------------- |
| Sales          | 2016-01-01 → 2021-02-20 |
| Exchange Rates | 2015-01-01 → 2021-02-20 |

Result:

Exchange rate data fully covers the entire sales dataset period.

Currency conversion can be applied safely without missing rates.

---

# 6. Negative Value Checks

Checked for invalid negative values in numeric columns.

| Dataset  | Column         | Negative Values |
| -------- | -------------- | --------------- |
| products | Unit Cost USD  | 0               |
| products | Unit Price USD | 0               |
| sales    | Quantity       | 0               |

All values are valid.

---

# 7. Future Date Validation

| Dataset   | Column        | Future Rows | %     |
| --------- | ------------- | ----------- | ----- |
| customers | Birthday      | 0           | 0%    |
| sales     | Order Date    | 0           | 0%    |
| sales     | Delivery Date | 82          | 0.13% |

### Interpretation

82 rows contain **Delivery Date beyond the dataset end date**.

These correspond to **orders still in transit** when the dataset snapshot was taken.

These rows are valid and will be flagged during cleaning.

---

# 8. Outlier Detection (IQR Method)

Outliers were detected using the **Interquartile Range (IQR)** method.

### Products — Unit Price

| Metric      | Value         |
| ----------- | ------------- |
| Upper Bound | $921.50       |
| Outliers    | 200           |
| Outlier %   | 7.95%         |
| Range       | $967 → $3,199 |

Interpretation:

These represent legitimate **high-end electronics products** such as premium desktops and televisions.

They are retained and flagged during cleaning.

---

### Products — Unit Cost

| Metric      | Value         |
| ----------- | ------------- |
| Upper Bound | $411.50       |
| Outliers    | 183           |
| Outlier %   | 7.27%         |
| Range       | $413 → $1,060 |

These correspond to the same high-value SKUs identified in price outliers.

---

### Sales — Quantity

| Metric      | Value  |
| ----------- | ------ |
| Upper Bound | 8.5    |
| Outliers    | 1,808  |
| Outlier %   | 2.88%  |
| Range       | 9 → 10 |

Interpretation:

These represent **bulk purchase orders** rather than data errors.

---

### Stores — Square Meters

| Metric   | Value |
| -------- | ----- |
| Outliers | 0     |

Store size distribution falls within expected bounds.

---

# 9. Delivery Consistency Check

Online orders were validated to ensure:

```
Delivery Date >= Order Date
```

Results:

| Metric             | Value  |
| ------------------ | ------ |
| Checked Rows       | 13,165 |
| Invalid Deliveries | 0      |

All delivery timelines are valid.

---

# Phase 2 Summary

| Check Category        | Result                   |
| --------------------- | ------------------------ |
| Schema validation     | Passed                   |
| Null analysis         | Explained and acceptable |
| Duplicate detection   | None found               |
| Foreign key integrity | Fully valid              |
| Date coverage         | Fully covered            |
| Negative values       | None                     |
| Future dates          | 82 pending deliveries    |
| Outliers              | Legitimate business data |

Phase 2 confirms that **the dataset is structurally valid and ready for cleaning and feature engineering in Phase 3**.
