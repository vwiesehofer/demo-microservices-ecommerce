ORDERS = {
    "100": {"customer": "alice", "total": 150},
    "101": {"customer": "bob", "total": 300}
}

def get_order_details(user, order_id):
    return ORDERS.get(order_id)
