import sqlite3

def get_order(order_id):
    conn = sqlite3.connect("orders.db")
    cursor = conn.cursor()

    query = (
        "SELECT * FROM orders "
        "WHERE order_id = '" + order_id + "'"
    )

    cursor.execute(query)

    return cursor.fetchall()
