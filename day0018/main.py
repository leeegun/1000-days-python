# day0018 - return contract and None


orders = [
    {"id": 1, "price": 1200, "status": "pending"},
    {"id": 2, "price": 3000, "status": "paid"},
    {"id": 3, "price": 1500, "status": "pending"},
]


def is_valid_order(order):
    if order is None:
        return False
    if not isinstance(order, dict):  # type(order) is not dict:
        return False
    if not isinstance(order.get("price"), int):  # type(order.get("price")) is not int:
        return False
    if order["price"] <= 0:
        return False
    if order["status"] not in ["paid", "pending"]:
        return False
    return True


def calc_pending_total(orders):
    total = 0
    found = False
    for order in orders:
        if is_valid_order(order) and order["status"] == "pending":
            total += order["price"]
            found = True
    if not found:
        return None
    return total


result = calc_pending_total(orders)
print(result)
