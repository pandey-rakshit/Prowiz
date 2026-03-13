# Task 5 — SQL Topper in Class

Write SQL queries to identify the **second topper in the class** under different ranking rules.

---

# A) Second Topper in Class

### Data

| Name    | Marks |
| ------- | ----- |
| Sahil   | 95    |
| Kaushik | 90    |
| John    | 89    |
| Kara    | 87    |
| Simpson | 97    |

### SQL Query

```sql
WITH temp AS (
    SELECT 
        name,
        marks,
        ROW_NUMBER() OVER (ORDER BY marks DESC) AS rnk
    FROM students_a
)

SELECT
    name,
    marks
FROM temp
WHERE rnk = 2;
```

### Result

| Name  | Marks |
| ----- | ----- |
| Sahil | 95    |

---

# B) Second Topper (Tie Broken by Name)

If two candidates have the **same marks**, the candidate whose **name comes first alphabetically** receives the **better (lower) rank**.

### Data

| Name    | Marks |
| ------- | ----- |
| Sahil   | 95    |
| Kaushik | 97    |
| John    | 89    |
| Kara    | 87    |
| Simpson | 97    |

### SQL Query

```sql
WITH temp AS (
    SELECT 
        name,
        marks,
        ROW_NUMBER() OVER (ORDER BY marks DESC, name ASC) AS rnk
    FROM students_b
)

SELECT
    name,
    marks
FROM temp
WHERE rnk = 2;
```

### Result

| Name    | Marks |
| ------- | ----- |
| Simpson | 97    |

Explanation:

* Kaushik (97) → Rank 1
* Simpson (97) → Rank 2 (same marks but alphabetical order decides rank)

---

# C) Second Topper(s) with Same Rank for Same Marks

If multiple candidates have **same marks**, they receive the **same rank**.

### Data

| Name    | Marks |
| ------- | ----- |
| Sahil   | 95    |
| Kaushik | 97    |
| John    | 95    |
| Kara    | 87    |
| Simpson | 97    |

### SQL Query

```sql
WITH temp AS (
    SELECT 
        name,
        marks,
        DENSE_RANK() OVER (ORDER BY marks DESC) AS rnk
    FROM students_c
)

SELECT
    name,
    marks
FROM temp
WHERE rnk = 2;
```

### Result

| Name  | Marks |
| ----- | ----- |
| Sahil | 95    |
| John  | 95    |

Explanation:

* Rank 1 → Kaushik (97), Simpson (97)
* Rank 2 → Sahil (95), John (95)

---

# Execution Result (Python + Pandas)

### Table A

| Name    | Marks |
| ------- | ----- |
| Simpson | 97    |
| Sahil   | 95    |
| Kaushik | 90    |
| John    | 89    |
| Kara    | 87    |

**Second Topper**

| Name  | Marks |
| ----- | ----- |
| Sahil | 95    |

---

### Table B

| Name    | Marks |
| ------- | ----- |
| Kaushik | 97    |
| Simpson | 97    |
| Sahil   | 95    |
| John    | 89    |
| Kara    | 87    |

**Second Topper**

| Name    | Marks |
| ------- | ----- |
| Simpson | 97    |

---

### Table C

| Name    | Marks |
| ------- | ----- |
| Kaushik | 97    |
| Simpson | 97    |
| Sahil   | 95    |
| John    | 95    |
| Kara    | 87    |

**Second Topper(s)**

| Name  | Marks |
| ----- | ----- |
| Sahil | 95    |
| John  | 95    |
