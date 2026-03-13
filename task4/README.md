# Global Electronics Retailer — Data Analysis Project

This project performs **data cleaning, validation, exploratory data analysis (EDA), and revenue analysis** on a global electronics retailer dataset.

The dataset covers **sales, customers, products, stores, and exchange rates** between **2016-01-01 and 2021-02-20**.

The objective of this project is to:

* Clean and validate raw transactional data
* Engineer analytical features
* Perform exploratory data analysis
* Identify revenue drivers and operational insights
* Produce structured findings for business decision making

---

# Dataset Overview

| Dataset         | Rows   | Description                      |
| --------------- | ------ | -------------------------------- |
| customers       | 15,266 | Customer demographic information |
| sales           | 62,884 | Transaction-level order data     |
| products        | 2,517  | Product catalogue                |
| stores          | 67     | Physical and online stores       |
| exchange_rates  | 11,215 | Currency exchange rates          |
| data_dictionary | 37     | Metadata reference               |

Dataset time range:

2016-01-01 → 2021-02-20

---

# Project Structure

The project follows a **modular analytics pipeline design** separating validation, cleaning, transformation, analysis, and visualization logic.

```
src
├── analysis
│   ├── customers.py
│   ├── decline.py
│   ├── premium.py
│   ├── products.py
│   ├── revenue.py
│   ├── sales.py
│   ├── store_perf.py
│   ├── stores.py
│   └── helpers.py
│
├── checks
│   ├── date.py
│   ├── delivery.py
│   ├── duplicate.py
│   ├── foreign_key.py
│   ├── future_date.py
│   ├── negative.py
│   ├── null.py
│   ├── outlier.py
│   ├── range.py
│   └── schema.py
│
├── cleaning
│   ├── customers.py
│   ├── exchange_rates.py
│   ├── products.py
│   ├── sales.py
│   └── stores.py
│
├── transform
│   └── currency.py
│
├── utils
│   └── helpers.py
│
├── viz
│   ├── base.py
│   └── style.py
│
├── loader.py
├── validator.py
├── reporter.py
│
├── run_phase2.py
├── run_phase3.py
│
├── check_delivery_days.py
├── check_online_consistency.py
└── check_pending_deliveries.py
```

---

# Architecture Overview

The project is organized into **functional modules**, each responsible for a specific stage of the data pipeline.

| Module        | Purpose                                           |
| ------------- | ------------------------------------------------- |
| analysis      | Business analysis and insight generation          |
| checks        | Data validation rules used during Phase 2         |
| cleaning      | Dataset-specific cleaning and feature engineering |
| transform     | Data transformations used during cleaning         |
| utils         | Shared helper utilities                           |
| viz           | Visualization utilities and styling               |
| loader.py     | Loads raw datasets                                |
| validator.py  | Executes validation checks                        |
| reporter.py   | Generates validation reports                      |
| run_phase2.py | Executes the validation pipeline                  |
| run_phase3.py | Executes the cleaning pipeline                    |

---

# Data Pipeline Flow

The data pipeline follows a **three-stage processing flow**:

```
Raw Data
   ↓
Loader
   ↓
Validation (Phase 2)
   ↓
Cleaning & Feature Engineering (Phase 3)
   ↓
Processed Parquet Datasets
   ↓
Exploratory Data Analysis
```

---

# Module Responsibilities

## loader.py

Responsible for loading raw datasets and ensuring correct encodings.

Key tasks:

* load CSV datasets
* handle encoding issues
* ensure schema consistency

---

## checks/

Contains **data validation checks** used during Phase 2.

Validation includes:

* null value detection
* duplicate detection
* foreign key validation
* range checks
* date consistency checks
* negative value detection
* outlier detection

Each check is implemented as a **separate module for modular validation logic**.

---

## cleaning/

Contains dataset-specific cleaning pipelines.

Each dataset has a dedicated cleaning module:

| File              | Dataset                                 |
| ----------------- | --------------------------------------- |
| customers.py      | Customer demographic cleaning           |
| products.py       | Product pricing and margin calculations |
| sales.py          | Order data cleaning and derived metrics |
| stores.py         | Store metadata cleaning                 |
| exchange_rates.py | Exchange rate normalization             |

---

## transform/

Contains reusable transformation logic.

Example:

`currency.py`

* currency normalization
* exchange rate application

---

## analysis/

Contains business analysis modules used during EDA.

Each module focuses on a specific analytical dimension:

| File          | Analysis Area              |
| ------------- | -------------------------- |
| customers.py  | Customer demographics      |
| products.py   | Product catalogue insights |
| sales.py      | Sales performance          |
| revenue.py    | Revenue distribution       |
| premium.py    | Premium product analysis   |
| stores.py     | Store network analysis     |
| store_perf.py | Store-level performance    |
| decline.py    | Revenue decline analysis   |

---

## viz/

Visualization utilities used across analysis modules.

| File     | Purpose                         |
| -------- | ------------------------------- |
| base.py  | Chart creation helpers          |
| style.py | Visualization styling and theme |

---

# Execution Scripts

## Phase 2 — Validation

```
python src/run_phase2.py
```

Performs:

* dataset loading
* validation checks
* validation report generation

Output:

```
outputs/reports/phase2_validation.json
```

---

## Phase 3 — Cleaning

```
python src/run_phase3.py
```

Performs:

* dataset cleaning
* feature engineering
* output dataset generation

Outputs saved to:

```
data/processed/
```


# Key Outputs

| Output                       | Description                   |
| ---------------------------- | ----------------------------- |
| customers_clean.parquet      | Cleaned customer dataset      |
| products_clean.parquet       | Cleaned product dataset       |
| sales_clean.parquet          | Cleaned transactional dataset |
| stores_clean.parquet         | Cleaned store dataset         |
| exchange_rates_clean.parquet | Cleaned exchange rate dataset |

---

# Key Business Insights

Highlights from the analysis:

* **65+ customers generate the highest revenue**
* **Computers dominate revenue contribution**
* **Online store is 17x more productive per storefront**
* **Premium products generate 28% of total revenue**
* **Q4 is consistently the strongest sales quarter**
* **US drives more revenue than all other countries combined**

Full findings are documented in:

```
docs/eda_findings.md
```

---

# Documentation

Detailed technical documentation is provided in the `docs` directory:

| File                  | Description                                 |
| --------------------- | ------------------------------------------- |
| cleaning_decisions.md | Data cleaning logic and decisions           |
| phase3_run_results.md | Execution summary of cleaning pipeline      |
| eda_findings.md       | Business insights from exploratory analysis |

---

# Tools Used

* Python
* Pandas
* NumPy
* Matplotlib
* Seaborn
* Jupyter Notebook
* Parquet storage format


---

# Utility Scripts

Additional validation scripts are included for investigative checks:

| Script                      | Purpose                             |
| --------------------------- | ----------------------------------- |
| check_delivery_days.py      | Verify delivery time calculations   |
| check_online_consistency.py | Validate online vs in-store logic   |
| check_pending_deliveries.py | Validate pending delivery detection |

These scripts were used to verify business assumptions discovered during analysis.

---

# Key Design Principles

The project architecture follows several design principles:

* **Modular pipeline design**
* **Separation of validation and cleaning**
* **Reusable transformation logic**
* **Dataset-specific cleaning modules**
* **Traceable validation reporting**

This structure ensures the project is **maintainable, extensible, and suitable for real-world analytics workflows**.
