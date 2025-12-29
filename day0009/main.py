# Day 9 : list filtering

numbers = [3, 7, 10, 15, 20, 25]

for num in numbers:
    if num >= 10:
        print(num)
# 리스트에서 10 이상인 숫자만 출력하기
print("----")

for num in numbers:
    if num < 10:
        continue
    print(num)
# continue 문을 사용하여 10 미만인 숫자는 건너뛰기
print("----")

filtered = []

for num in numbers:
    if num >= 10:
        filtered.append(num)
print(filtered)
# 10 이상인 숫자만 새로운 리스트에 추가하기
print("----")

words = ["apple", "banana", "cherry", "date", "fig", "grape"]
long_words = []

for word in words:
    if len(word) > 3:
        long_words.append(word)
print(long_words)
# 길이가 3보다 큰 단어만 새로운 리스트에 추가하기
print("----")

logs = [
    "INFO system start",
    "WARNING low memory",
    "ERROR disk failure",
    "INFO shutdown",
]
errors = []

for log in logs:
    if "ERROR" in log:
        errors.append(log)
print(errors)
# "ERROR"가 포함된 로그 메시지만 새로운 리스트에 추가하기
print("----")

orders = [1200, 0, -300, 4500, "error", 2300, None, 800]
valid_orders = []

for order in orders:
    if type(order) == int and order > 0: # 조건문 순서를 신경써야 함
        valid_orders.append(order)
print(valid_orders)
