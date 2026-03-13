import pandas as pd
from .database import get_connection

def load_table_a():

    data = {
        "Name": ["Sahil", "Kaushik", "John", "Kara", "Simpson"],
        "Marks": [95, 90, 89, 87, 97]
    }

    df = pd.DataFrame(data)

    conn = get_connection()

    df.to_sql("students_a", conn, if_exists="replace", index=False)

    result = pd.read_sql("SELECT * FROM students_a order by marks DESC", conn)

    print("\nTable A")
    print(result)
    print("="*80)

    # Write a sql code to identify the following
    # a) The second topper in class
    print("SQL Query : Second Topper \n")
    query = """
    WITH temp AS (
    SELECT 
        name, 
        marks, 
        ROW_NUMBER() OVER(ORDER BY marks DESC) as rnk
    FROM students_a
    )

    SELECT
        name,
        marks
    FROM temp
    WHERE rnk = 2
    """
    print(query)
    print("="*80)
    result = pd.read_sql(query, conn)
    print("Second Topper:")
    print(result)
    print("="*80)
    conn.close()