import pandas as pd
from .database import get_connection

def load_table_b():

    data = {
        "Name": ["Sahil", "Kaushik", "John", "Kara", "Simpson"],
        "Marks": [95, 97, 89, 87, 97]
    }

    df = pd.DataFrame(data)

    conn = get_connection()

    df.to_sql("students_b", conn, if_exists="replace", index=False)

    result = pd.read_sql("SELECT * FROM students_b order by marks DESC", conn)

    print("\nTable B")
    print(result)
    print("="*80)

    # b) The second topper in class. If 2 candidates have same marks then the one with their name first in
    # alphabetical order is given the better(lower) rank

    print("SQL Query : Second Topper | If 2 candidates have same marks then the one with their name first in alphabetical order is given the better(lower) rank \n")
    query = """
    WITH temp AS (
    SELECT 
        name, 
        marks, 
        ROW_NUMBER() OVER(ORDER BY marks DESC, name ASC) as rnk
    FROM students_b
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