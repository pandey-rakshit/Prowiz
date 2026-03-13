# SQL Queries for Tables A, B, and C

## A. Table A

### Data

| Name    | Marks |
| ------- | ----- |
| Sahil   | 95    |
| Kaushik | 90    |
| John    | 89    |
| Kara    | 87    |
| Simpson | 97    |

### Create Table

```sql
CREATE TABLE students_a (
    Name TEXT,
    Marks INTEGER
);
```

### Insert Data

```sql
INSERT INTO students_a (Name, Marks) VALUES ('Sahil', 95);
INSERT INTO students_a (Name, Marks) VALUES ('Kaushik', 90);
INSERT INTO students_a (Name, Marks) VALUES ('John', 89);
INSERT INTO students_a (Name, Marks) VALUES ('Kara', 87);
INSERT INTO students_a (Name, Marks) VALUES ('Simpson', 97);
```

### Delete All Data

```sql
DELETE FROM students_a;
```

---

# B. Table B

### Data

| Name    | Marks |
| ------- | ----- |
| Sahil   | 95    |
| Kaushik | 97    |
| John    | 89    |
| Kara    | 87    |
| Simpson | 97    |

### Create Table

```sql
CREATE TABLE students_b (
    Name TEXT,
    Marks INTEGER
);
```

### Insert Data

```sql
INSERT INTO students_b (Name, Marks) VALUES ('Sahil', 95);
INSERT INTO students_b (Name, Marks) VALUES ('Kaushik', 97);
INSERT INTO students_b (Name, Marks) VALUES ('John', 89);
INSERT INTO students_b (Name, Marks) VALUES ('Kara', 87);
INSERT INTO students_b (Name, Marks) VALUES ('Simpson', 97);
```

### Delete All Data

```sql
DELETE FROM students_b;
```

---

# C. Table C

### Data

| Name    | Marks |
| ------- | ----- |
| Sahil   | 95    |
| Kaushik | 97    |
| John    | 95    |
| Kara    | 87    |
| Simpson | 97    |

### Create Table

```sql
CREATE TABLE students_c (
    Name TEXT,
    Marks INTEGER
);
```

### Insert Data

```sql
INSERT INTO students_c (Name, Marks) VALUES ('Sahil', 95);
INSERT INTO students_c (Name, Marks) VALUES ('Kaushik', 97);
INSERT INTO students_c (Name, Marks) VALUES ('John', 95);
INSERT INTO students_c (Name, Marks) VALUES ('Kara', 87);
INSERT INTO students_c (Name, Marks) VALUES ('Simpson', 97);
```

### Delete All Data

```sql
DELETE FROM students_c;
```
