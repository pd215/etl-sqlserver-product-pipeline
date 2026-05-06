import json
import pyodbc

conn = pyodbc.connect(
    "DRIVER={ODBC Driver 17 for SQL Server};"
    "SERVER=localhost;"
    "DATABASE=DataPipelineDB;"
    "Trusted_Connection=yes;"
)

cursor = conn.cursor()

def create_table():
    cursor.execute("""
    IF OBJECT_ID('stg_products', 'U') IS NOT NULL
        DROP TABLE stg_products;

    CREATE TABLE stg_products (
        id INT,
        title NVARCHAR(255),
        price FLOAT,
        category NVARCHAR(100)
    )
    """)
    conn.commit()

def load_data():
    with open("products_latest.json", "r", encoding="utf-8") as f:
        data = json.load(f)

    products = data["products"]

    for p in products:
       cursor.execute("""
		INSERT INTO stg_products (id, title, price, category)
		SELECT ?, ?, ?, ?
		WHERE NOT EXISTS (
    		SELECT 1 FROM stg_products WHERE id = ?
		)
		""", p["id"], p["title"], p["price"], p["category"], p["id"])

    conn.commit()
    print("Data loaded!")

if __name__ == "__main__":
    create_table()
    load_data()
    conn.close()