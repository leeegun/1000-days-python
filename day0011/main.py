# day0011 - dictionary

# 딕셔너리 만들기
user = {"name": "Changsu", "age": 30, "city": "Seoul"}
print(user["name"])
print(user["age"])
print(user["city"])
print("-----")

# 딕셔너리에 새로운 키-값 쌍 추가/수정 하기
user["job"] = "Engineer"
user["age"] = 45
print(user)
print("-----")

# 딕셔너리 키 삭제하기
del user["city"]  # 키값 삭제
print(user)
old_job = user.pop("job")  # 키값 꺼내면서 삭제
print("Old job:", old_job)
print(user)
print("-----")

# 사용자로부터 입력 받아 딕셔너리 만들기
name = input("Enter your name: ")
age = int(input("Enter your age: "))
user = {"name": name, "age": age}
for k, v in user.items():
    print(k, ":", v)
