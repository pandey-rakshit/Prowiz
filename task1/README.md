# Task 1 – Python Requests

## Objective

Use the **Python `requests` package** to fetch data from the following API:

https://jsonplaceholder.typicode.com/posts

You may use **pandas, numpy, or any other Python packages** to complete the analysis.

---

# Questions

### a) Fetch data from the API

Use the Python `requests` package to fetch data from the provided API endpoint.

### b) Fetch all posts and print them

### c) Count the distinct number of users

### d) Which user has the highest number of posts?

### e) What is the average word length of post titles?

---

# How to Run the Project

This project uses **uv** for dependency management and execution.

### 0. Main Directory
```bash
cd task1
```

### 1. Install Dependencies

```bash
uv sync
```

### 2. Run the Script

```bash
uv run python src/main.py
```

### 3. Output

The results will be printed directly in the **CLI / terminal**.

Example output:

```
Fetching posts from API...
Successfully fetched 100 posts.

================================================================================
c) DISTINCT NUMBER OF USERS
================================================================================
Total distinct users: 10

================================================================================
d) USER WITH HIGHEST NUMBER OF POSTS
================================================================================
User 1 has the highest number of posts: 10 posts

================================================================================
e) AVERAGE WORD LENGTH OF POST TITLES
================================================================================
Average word length in post titles: 5.60 characters
```

---

# Results

## a) API Fetch Status

```

Fetching posts from API...
Successfully fetched 100 posts.

```

---

## b) All Posts

| User ID | Post ID | Title | Body |
|-------|-------|------|------|
| 1 | 1 | sunt aut facere repellat provident occaecati excepturi optio reprehenderit | quia et suscipit suscipit recusandae consequuntur expedita et cum reprehenderit molestiae ut ut quas totam nostrum rerum est autem sunt rem eveniet architecto |
| 1 | 2 | qui est esse | est rerum tempore vitae sequi sint nihil reprehenderit dolor beatae ea dolores neque fugiat blanditiis voluptate porro vel nihil molestiae ut reiciendis |
| 1 | 3 | ea molestias quasi exercitationem repellat qui ipsa sit aut | et iusto sed quo iure voluptatem occaecati omnis eligendi aut ad voluptatem doloribus vel accusantium |
| ... | ... | ... | ... |
| 10 | 100 | at nam consequatur ea labore ea harum | cupiditate quo est a modi nesciunt soluta ipsa voluptas error itaque dicta |

*(Total posts fetched: 100)*

---

## c) Distinct Number of Users

**Total distinct users:**  

```

10

```

---

## d) User With Highest Number of Posts

| User ID | Post Count |
|-------|------------|
| 1 | 10 |
| 2 | 10 |
| 3 | 10 |
| 4 | 10 |
| 5 | 10 |
| 6 | 10 |
| 7 | 10 |
| 8 | 10 |
| 9 | 10 |
| 10 | 10 |

**Insight**

All users have posted **10 posts each**.

**User with highest posts:**  

```

User 1 → 10 posts

```

*(Tie between all users)*

---

## e) Average Word Length of Post Titles

```

Average word length in post titles: 5.60 characters

```

---

# Libraries Used

- `requests` – Fetch API data
- `pandas` – Data analysis

