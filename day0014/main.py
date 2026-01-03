# day0014 - fuction parameters and default values


def add(a, b):
    return a + b


print(add(3, 5))
print("-----")


def calculate_price(price, quantity):
    return price * quantity


print(calculate_price(1200, 3))
print("-----")


# default parameters
def greet(
    first_name, last_name="John"
):  # 기본값이 있는 매개변수는 항상 마지막에 위치해야 한다.
    return "Hello," + first_name + last_name


print(greet("Smith "))
print(greet("smith", " weelson"))
print("-----")

# day0013 개선
orders = [
    {"id": 1, "price": 1200, "status": "paid"},
    {"id": 2, "price": 4500, "status": "pending"},
    {"id": 3, "price": 800, "status": "paid"},
    {"id": 4, "price": 3000, "status": "paid"},
]


def calculate_paid_total(orders, status="paid"):
    total = 0
    for order in orders:
        if order.get("status") == status:
            total += order.get("price", 0)  # price key가 없으면 0을 반환
    return total


print("Total paid orders:", calculate_paid_total(orders), "pending")

"""
function name : calculate_final_price
parameters : price, shipping_fee(기본값: 3000)
최종 금액 : price + shipping fee
"""


def calculate_final_price(price, shipping_fee=3000):
    return price + shipping_fee


print(calculate_final_price(20000))  # shipping_fee 기본값 사용
print(calculate_final_price(20000, 0))  # shipping_fee 0으로 지정
