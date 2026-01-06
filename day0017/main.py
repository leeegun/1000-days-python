# day0017 - validation and function boundaries

orders = [
    {"id": 1, "price": 1200, "status": "paid"},
    {"id": 2, "status": "paid"},  # price 없음
    {"id": 3, "price": "800", "status": "paid"},  # 타입 이상
    {"id": 4, "price": 3000, "status": "pending"},
    None,
    {"id": 5, "price": 1500, "status": "paid"},
]


# 딕셔너리 유효성 검증
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


# is_valid_order 테스트
for order in orders:
    print(order, "->", is_valid_order(order))


# 합산
def calculate_total(orders):
    total = 0
    for order in orders:
        total += order["price"]
    return total


# 유효한 주문 총합
def valid_order_total(orders):
    valid = []
    for order in orders:
        if is_valid_order(order) and order["status"] == "paid":
            valid.append(order)
    return calculate_total(valid)


print("Valid order total:", valid_order_total(orders))
