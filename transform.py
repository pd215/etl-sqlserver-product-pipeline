import pyodbc
import random

conn = pyodbc.connect(
    "DRIVER={ODBC Driver 17 for SQL Server};"
    "SERVER=localhost;"
    "DATABASE=DataPipelineDB;"
    "Trusted_Connection=yes;"
)

cursor = conn.cursor()

# 1. Load dimension
cursor.execute("DELETE FROM dim_product")

cursor.execute("""
INSERT INTO dim_product (product_id, title, category)
SELECT id, title, category
FROM stg_products
""")

# 2. Simulate fact data
cursor.execute("DELETE FROM fact_product_sales")

cursor.execute("SELECT id, price FROM stg_products")
rows = cursor.fetchall()

for r in rows:
    product_id = r[0]
    price = r[1]

    quantity = random.randint(1, 5)

    cursor.execute("""
        INSERT INTO fact_product_sales (product_id, price, quantity)
        VALUES (?, ?, ?)
    """, product_id, price, quantity)

conn.commit()
conn.close()

print("Transformation completed")