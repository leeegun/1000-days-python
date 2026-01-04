# day0015 - function responsibility

orders = [
    {"id": 1, "price": 1200, "status": "paid"},
    {"id": 2, "price": 4500, "status": "pending"},
    {"id": 3, "price": 800, "status": "paid"},
    {"id": 4, "price": 3000, "status": "paid"},
]


# 나쁜 예 - 여러 기능이 들어있는 함수
def process_order(orders):
    total = 0
    for order in orders:
        if order["status"] == "paid":  # 기능1 - 주문 필터링
            total += order["price"]  # 기능2 - 합계 계산

    print("Total:", total)  # 기능3 - 출력
    return total


process_order(orders)
print("----------------")

"""
기능이 2개 이상일 때 함수를 쪼개기
1. if가 많다
2. for문이 여러 개 있다.
3. print가 섞여 있따.
4. 이름에 and, process, handle 같은 단어가 들어간다.
5. "이 함수 기능이 뭐지?" 라는 설명이 길다.
"""


# 결제 완료 주문만 필터링
def get_paid_orders(orders):
    paid_orders = []
    for order in orders:
        if order["status"] == "paid":
            paid_orders.append(order)
    return paid_orders


# 주문 합계 계산
def calculate_total(orders):
    total = 0
    for order in orders:
        total += order["price"]
    return total


# 조합해서 사용
paid_orders = get_paid_orders(orders)
total = calculate_total(paid_orders)
print("Total:", total)
