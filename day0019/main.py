# day0019 - None vs Exception

"""
# 결과가 없을 수 있을 때
def find_paid_total(order):
    total = 0
    found = False
    for o in orders:
        if o["status"] == "paid":
            total += o["price"]
            found = True
    if not found:
        return None
    return total


# 입력값을 받을 때 계산 자체가 안되는 경우
# 함수 계약을 깨는 입력, 타입이 완전 틀림, 필수 값 누락
def calculate_total(orders):
    if type(orders) != list:
        raise TypeError("orders must be a list")
    total = 0
    for o in orders:
        total += o["price"]
    return total
"""
"""
orders = [
    {"id": 1, "price": 1200, "status": "paid"},
    {"id": 2, "status": "paid"},  # price 없음
    {"id": 3, "price": "800", "status": "paid"},  # 타입 이상
    {"id": 4, "price": 3000, "status": "pending"},
    None,
    {"id": 5, "price": 1500, "status": "paid"},
]


# 검증 함수
def is_valid_order(order):
    if order is None:
        return False
    if not isinstance(order, dict):  # type(order) is not dict:
        raise TypeError("order must be dict")
    if not isinstance(order.get("price"), int):  # type(order.get("price")) is not int:
        raise KeyError("price missing")
    if order["price"] <= 0:
        return False
    if order["status"] not in ["paid", "pending"]:
        return False
    return True


# 비즈니스 함수
def calc_paid_total(orders):
    total = 0
    found = False
    for order in orders:
        if order["status"] == "paid":
            total += order["price"]
            found = True
    if not found:
        return None
    return total


# None 처리
result = calc_paid_total(orders)
if reuslt is None:
    print("No paid orders")

# Exception 처리
try:
    total = calc_paid_total(orders)
except TypeError as e:
    print("Input error: ", e)
"""

# test


def calc_avg_price(prices):
    if not isinstance(prices, list):
        raise TypeError("prices must be a list")

    if prices == []:
        return None

    total = 0
    i = 0
    # sum = 0 파이썬 내장 함수

    for p in prices:  # for p in prices[i]: 첫 번째 값 하나. 반복 안 함
        if not isinstance(p, int):
            raise TypeError("Please must contain only integers")
        total += p
        i += 1
    return total / i


avg = calc_avg_price([1000, 2000])
print(avg)
avg = calc_avg_price([])
print(avg)

avg = calc_avg_price([1000, "2000"])
print(avg)

avg = calc_avg_price("123")
print(avg)
