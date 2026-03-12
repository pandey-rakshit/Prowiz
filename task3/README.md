# Task 3 – FastAPI

## Objective

Create APIs using **FastAPI** for basic validation and processing tasks.

---

# APIs

## a) Sum of Two Numbers

### Description

Accept **two numbers** and return their **sum**.

### Validation Rules

* Strict type checking is implemented.
* Only **numeric values** are accepted.
* Strings such as `"0"` are treated as **strings**, not numbers.
* If a **string value** is passed instead of a number, the API returns a **validation error**.

### Example Request

```json
{
  "num1": 5,
  "num2": 6
}
```

### Example Response

```json
11
```

### Invalid Request

```json
{
  "num1": "5",
  "num2": 6
}
```

Response → **Validation Error**

---

## b) Lowercase String to Uppercase

### Description

Accept a **lowercase string** and return the **uppercase version**.

### Validation Rules

* Input must be **entirely lowercase**.
* If **any uppercase character** or **title case** exists → error.
* If input contains **only numbers** (e.g., `234`) → error.
* Strings containing **numbers + lowercase letters** are valid.

### Example Request

```json
{
  "text": "hello"
}
```

### Example Response

```json
"HELLO"
```

### Example Request (Valid)

```json
{
  "text": "hello123"
}
```

Response

```json
"HELLO123"
```

### Example Request (Invalid)

```json
{
  "text": "Hello"
}
```

Response → **Error: string is not lowercase**

---

# How to Run the Project

### 1. Navigate to the Task Directory

```bash
cd task3
```

### 2. Install Dependencies

```bash
uv sync
```

---

# Run the API

### Development Mode

```bash
uv run uvicorn app.main:app --reload
```

### Production Mode

```bash
uv run uvicorn app.main:app --host 0.0.0.0 --port 8000
```

---

# API Documentation

FastAPI automatically generates Swagger documentation.

Open in browser:

```
http://127.0.0.1:8000/docs
```

---

# Libraries Used

* **FastAPI** – API framework
* **Pydantic** – request validation
* **Uvicorn** – ASGI server
* **uv** – dependency management
