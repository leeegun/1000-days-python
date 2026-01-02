# day0013 - fuction basics

# 함수가 없을 때
total = 0
orders = [1200, 4500, 800]

for price in orders:
    total += price
print("Total sales:", total)
print("----------------")


# 함수로 분리
def calculate_total(prices):
    total = 0
    for price in prices:
        total += price
    return total  # return은 값을 함수 밖으로 돌려준다. return 이후 코드는 실행되지 않음


orders = [1200, 4500, 800]
print("Total sales:", calculate_total(orders))
print("----------------")


# print와 return의 차이
def add(a, b):
    print(a + b)


result = add(
    3, 5
)  # 함수 내부에서 print는 값을 출력할 뿐, 함수 밖으로 값을 돌려주지 않는다.
print(result)  # None이 출력된다. return이 없으면 함수는 None을 반환한다.
print("----------------")

"""
Test - 조건에 맞는 주문 총액 계산하기
함수이름 : calculate_paid_total
입력값 : 주문 리스트 (odrders)
출력값 : 결제 완료 주문의 총 price
"""
orders = [
    {"id": 1, "price": 1200, "status": "paid"},
    {"id": 2, "price": 4500, "status": "pending"},
    {"id": 3, "price": 800, "status": "paid"},
    {"id": 4, "price": 3000, "status": "paid"},
]


# order key와 value가 정확할 때 사용 가능. 값이 깨지면 KeyError 발생
""" def calculate_paid_total(orders):
    total = 0
    for order in orders:
        if order["status"] == "paid":
            total += order["price"]
    return total """


# order.get()을 사용하면 KeyError를 피할 수 있다.
def calculate_paid_total(orders):
    total = 0
    for order in orders:
        if order.get("status") == "paid":
            total += order.get("price", 0)
    return total


result = calculate_paid_total(orders)  # 5000
print(result)

# 데이터가 틀려도 프로그램은 멈추지 않는다.
