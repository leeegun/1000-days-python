# day0012 - dictionary + list

# dict 내부에 list가 포함된 형태
user = {"name": "Changsu", "age": 30, "hobbies": ["reading", "traveling", "swimming"]}

print(user["hobbies"])
print(user["hobbies"][0])  # 첫 번째 취미 출력
print("------------")
# dict list 추가하기
user["hobbies"].append("coding")
print(user["hobbies"])
print("------------")
# list 내부에 dict가 포함된 형태
orders = [{"id": 1, "price": 1200}, {"id": 2, "price": 2500}, {"id": 3, "price": 800}]
for order in orders:
    print(order["price"])
print("------------")
for order in orders:
    if order["price"] >= 1200:
        print(order["id"])
total_price = 0
for order in orders:
    total_price += order["price"]
print("Total Price:", total_price)
print("------------")
# dict list 추가하기
orders.append({"id": 4, "price": 3000})
print(orders[3])
