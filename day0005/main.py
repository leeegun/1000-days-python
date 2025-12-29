# Day 5 : if/else condition

try:
    # age = int(input("How old are you? ")) # input과 int가 동시에 처리되어 어디서 실패하는지 알 수 없음
    age_input = input("How old are you? ")
    age = int(age_input)    
    if age >= 18:
        print("You are an adult.")
    else:
        print("You are a minor.")
except ValueError: # 숫자가 아닌 값을 입력했을 때 발생하는 예외 처리  
    print("Please enter a valid number.")
