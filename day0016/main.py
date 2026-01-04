# day0016 - function composition

orders = [
    {"id": 1, "price": 1200, "status": "paid"},
    {"id": 2, "price": 4500, "status": "pending"},
    {"id": 3, "price": 800, "status": "paid"},
    {"id": 4, "price": 3000, "status": "paid"},
]

"""
# 이전 방식의 결제 완료 주문 필터링 - 기능별로 나누지 않음
def get_paid_orders(orders):
    return [order for order in orders if order.get("status") == "paid"]

# 메인 함수
def clacualte_paid_orders_total(orders):
    paid_orders = get_paid_orders(orders)
    return calculate_total(paid_orders)
"""

# 실무


# paid 여부 판단
def is_paid(order):
    return order.get("status") == "paid"


# paid된 오더 필터링
def get_paid_orders(orders):
    return [order for order in orders if is_paid(order)]


# 총합 계산
def calculate_total(orders):
    total = 0
    for order in orders:
        total += order.get("price", 0)
    return total


# 필터링된 오더의 총합 계산
def calculate_paid_orders_total(orders):
    paid_orders = get_paid_orders(orders)
    return calculate_total(paid_orders)


print("Total:", calculate_paid_orders_total(orders))
