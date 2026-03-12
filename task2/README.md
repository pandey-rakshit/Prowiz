# Task 2 – HTML Parser

## Objective

Parse a given HTML string and extract specific information using **BeautifulSoup** and a **custom recursive parser (without external libraries)**.

---

# Questions

### a) Read the following HTML text in Python as a string

```html
<html><head><title>The Dormouse's story</title></head><body>
<p class="title"><b>The Dormouse's story</b></p>
<p class="story">Once upon a time there were three little sisters; and their
names were
<a href="http://example.com/elsie" class="sister" id="link1">Elsie</a>,
<a href="http://example.com/lacie" class="sister" id="link2">Lacie</a> and
<a href="http://example.com/tillie" class="sister" id="link3">Tillie</a>;
and they lived at the bottom of a well.</p>
<p class="story">...</p>
```

---

### b) Use **BeautifulSoup** to print the following

1. All **href links** in the given HTML text
2. All **class values for `<a>` tags**

**Extra Points**

Write a **recursive Python parser** capable of parsing the HTML text and extracting the same information **without using BeautifulSoup or external dependencies**.

---

# How to Run the Project

### 1. Navigate to the Task Directory

```bash
cd task2
```

### 2. Install Dependencies

```bash
uv sync
```

### 3. Run the Script

```bash
python3 src/main.py
```

Results will be printed directly in the **CLI / terminal**.

---

# Output

```
======================================================================
                              HTML Parser                             
======================================================================

  BeautifulSoup Parser
======================================================================

  HREF Links
======================================================================
  1. http://example.com/elsie
  2. http://example.com/lacie
  3. http://example.com/tillie


  Classes in <a> tags
======================================================================
  1. sister
  2. sister
  3. sister


  Recursive Parser (No External Dependencies)
======================================================================

  HREF Links
======================================================================
  1. http://example.com/elsie
  2. http://example.com/lacie
  3. http://example.com/tillie


  Classes in <a> tags
======================================================================
  1. sister
  2. sister
  3. sister


======================================================================
  Results Comparison
======================================================================

  hrefs match: True
  classes match: True

======================================================================
Done
======================================================================
```

---

# Libraries Used

* `beautifulsoup4` – HTML parsing
* `uv` – dependency management and environment handling
