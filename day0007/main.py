# Day 7: break

for i in range(1, 10):
    if i == 5:
        break  # 반복문 전체 종료
    print(i)

print("break test")

for i in range(1, 10):
    if i == 5:
        continue  # 해당 반복만 건너뜀
    print(i)

print("continue test")

# Ask until correct password

while True:
    password = input("Enter the password: ")
    if password == "python":
        print("Access granted.")
        break
    else:
        print("Incorrect password. Try again.")
