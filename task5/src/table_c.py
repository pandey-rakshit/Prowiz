import pandas as pd
from .database import get_connection

def load_table_c():

    data = {
        "Name": ["Sahil", "Kaushik", "John", "Kara", "Simpson"],
        "Marks": [95, 97, 95, 87, 97]
    }

    df = pd.DataFrame(data)

    conn = get_connection()

    df.to_sql("students_c", conn, if_exists="replace", index=False)

    result = pd.read_sql("SELECT * FROM students_c order by marks DESC", conn)


    print("\nTable C")
    print("="*80)
    print(result)
    print("="*80)
    # c) The second topper(s) in class. If multiple candidates have same marks, they are given the same rank, so multiple individuals can have rank 1.

    print("SQL Query : Second Topper |  If multiple candidates have same marks, they are given the same rank, so multiple individuals can have rank 1 \n")
    query = """
    WITH temp AS (
    SELECT 
        name, 
        marks, 
        DENSE_RANK() OVER(ORDER BY marks desc) as rnk
    FROM students_c
    )

    SELECT
        name,
        marks
    FROM temp
    where rnk = 2
    """

    print(query)
    print("="*80)
    result = pd.read_sql(query, conn)
    print("Second Topper:")
    print(result)
    print("="*80)


    conn.close()