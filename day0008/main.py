# Day 8 : List

numbers = [10, 20, 30, 40, 50]

print(numbers)
print(numbers[0])
print(numbers[2])

fruits = ["apple", "banana", "cherry"]
for fruit in fruits:
    print("I like", fruit)

print(len(fruits))

fruits.append("grape")
for fruit in fruits:
    print("I like", fruit)

print(len(fruits))

fruits.insert(3, "orange")
print(fruits)
fruits.remove("banana")
print(fruits)

# append - 리스트 맨 끝에 요소 추가
# insert - 특정 위치에 요소 추가
# remove - 특정 요소 제거
# pop - 특정 위치의 요소 제거 및 반환
# clear - 리스트의 모든 요소 제거
# sort - 리스트 정렬
# reverse - 리스트 역순 정렬
# count - 특정 요소의 개수 세기
# index - 특정 요소의 인덱스 반환
