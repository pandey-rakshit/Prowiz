# Execution Order

The project follows a **three-stage workflow** consisting of validation, cleaning, and analysis.

The steps should be executed in the following order.

---

# 1. Phase 2 — Data Validation

Script:

```bash
python src/run_phase2.py
```

Purpose:

* Load raw datasets
* Validate schema consistency
* Detect null values
* Detect duplicate rows
* Verify foreign key relationships
* Validate date ranges
* Detect negative values
* Detect statistical outliers

Output:

```text
outputs/reports/phase2_validation.json
```

This report summarizes all validation checks performed on the raw datasets.

---

# 2. Phase 3 — Data Cleaning & Feature Engineering

Script:

```bash
python src/run_phase3.py
```

Purpose:

* Apply cleaning rules defined during validation
* Convert and standardize data types
* Handle null values where required
* Create derived analytical columns
* Apply feature engineering
* Save processed datasets

Output location:

```text
data/processed/
```

Generated files:

* customers_clean.parquet
* products_clean.parquet
* sales_clean.parquet
* stores_clean.parquet
* exchange_rates_clean.parquet

---

# 3. Exploratory Data Analysis

After the cleaned datasets are generated, analysis notebooks can be executed.

Notebook execution order:

```text
notebooks
1_customer_analysis.ipynb
2_product_analysis.ipynb
3_sales_analysis.ipynb
4_store_analysis.ipynb
5_revenue_analysis.ipynb
6_decline_analysis.ipynb
7_premium_product_analysis.ipynb
8_store_performance_analysis.ipynb
```

Each notebook focuses on a specific analytical dimension of the business.

---

# Full Pipeline Order

The complete project workflow should be executed in this order:

```text
1. python src/run_phase2.py
2. python src/run_phase3.py
3. Run notebooks in order [1 → 8]
```

This ensures that:

* raw data is validated first
* cleaned datasets are generated
* analysis is performed only on processed data
