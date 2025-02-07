import sqlite3

def init_db():
    conn = sqlite3.connect('business_orders.db')
    cur = conn.cursor()
    cur.execute("""
    CREATE TABLE IF NOT EXISTS orders (
    id INTEGER PRIMARY KEY,
    customer_name TEXT NOT NULL,
    order_details TEXT NOT NULL,
    status TEXT NOT NULL)
    """)
    conn.commit()
    conn.close()

def add_order(customer_name, order_details):
    conn = sqlite3.connect('business_orders.db')
    cur = conn.cursor()
    cur.execute(
        "INSERT INTO orders (customer_name, order_details, status) VALUES (?, ?, 'Новый')",
        (customer_name, order_details))
    conn.commit()
    conn.close()

def get_orders():
    conn = sqlite3.connect('business_orders.db')
    cur = conn.cursor()
    cur.execute("SELECT * FROM orders")
    rows = cur.fetchall()
    conn.close()
    return rows

def complete_order(order_id):
    conn = sqlite3.connect('business_orders.db')
    cur = conn.cursor()
    cur.execute("UPDATE orders SET status='Завершён' WHERE id=?", (order_id,))
    conn.commit()
    conn.close()
