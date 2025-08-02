import psycopg2
from dotenv import load_dotenv
import os

load_dotenv()

conn = psycopg2.connect(
    host=os.getenv("PG_HOST"),
    port=os.getenv("PG_PORT"),
    user=os.getenv("PG_USER"),
    password=os.getenv("PG_PASSWORD"),
    database=os.getenv("PG_DATABASE"),
)
cursor = conn.cursor()

# Drop and recreate table
cursor.execute("DROP TABLE IF EXISTS orders CASCADE;")
cursor.execute("""
CREATE TABLE orders (
    id SERIAL PRIMARY KEY,
    order_id TEXT UNIQUE,
    customer_name TEXT,
    product TEXT,
    status TEXT,
    refund_status TEXT
)
""")

# Insert seed data
cursor.execute("""
INSERT INTO orders (order_id, customer_name, product, status, refund_status) VALUES
('ORD001', 'Alice', 'Headphones', 'shipped', 'not_requested'),
('ORD002', 'Bob', 'Keyboard', 'delivered', 'processed'),
('ORD003', 'Charlie', 'Mouse', 'processing', 'not_requested')
""")

conn.commit()
cursor.close()
conn.close()
print("✅ DB recreated and seeded.")
