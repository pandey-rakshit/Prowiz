# Execution & Testing Steps

Follow the steps below to execute and verify the SQL topper queries using **Python, Pandas, and SQLite**.

---

# 1. Clone / Download the Project

Download the project folder and navigate into it.

```bash
cd task5
```

---

# 2. Install Required Dependencies

Ensure Python is installed, then install required packages.

```bash
pip install pandas
```

SQLite comes preinstalled with Python, so no additional installation is required.

---

# 3. Project Structure

The project should follow this structure:

```
task5/
│
├── data/
│   └── students.db
│
├── src/
│   ├── __init__.py
│   ├── database.py
│   ├── table_a.py
│   ├── table_b.py
│   └── table_c.py
│
└── main.py
```

---

# 4. Run the Program

Execute the main script to:

* Load the datasets into SQLite
* Execute SQL queries
* Display results using Pandas

```bash
python main.py
```

---

# 5. What the Program Does

The script performs the following steps:

1. Creates three tables in SQLite:

   * `students_a`
   * `students_b`
   * `students_c`

2. Inserts the respective dataset for each case.

3. Executes SQL queries to identify the **second topper** based on different ranking rules.

4. Displays:

   * Original table data
   * SQL query executed
   * Result of the query

---

# 6. Expected Output

The terminal will display:

### Case A

Second topper determined using `ROW_NUMBER()`.

### Case B

Second topper determined using `ROW_NUMBER()` with **alphabetical tie-breaking**.

### Case C

Second topper determined using `DENSE_RANK()` allowing **multiple students to share the same rank**.

Each section prints:

* Table data
* SQL query used
* Result returned by the query

---

# 7. Verify Results

Check that the output matches the expected ranking logic:

| Case | Logic                            | Expected Result       |
| ---- | -------------------------------- | --------------------- |
| A    | Simple ranking                   | Sahil (95)            |
| B    | Tie broken by alphabetical order | Simpson (97)          |
| C    | Same marks share rank            | Sahil (95), John (95) |

If these results appear, the SQL queries and Python execution are working correctly.
