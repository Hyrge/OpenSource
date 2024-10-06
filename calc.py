# 계산기 프로그램

def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y 

print("1. 덧셈")
print("2. 뺄셈")
print("3. 곱셈")


choice = input("원하는 연산을 선택하세요 (1/2/3): ")

num1 = float(input("첫 번째 숫자를 입력하세요: "))
num2 = float(input("두 번째 숫자를 입력하세요: "))

if choice == '1':
    print(f"{num1} + {num2} = {add(num1, num2)}")
elif choice == '2':
    print(f"{num1} - {num2} = {subtract(num1, num2)}")
else :
    print(f"{num1} * {num2} = {multiply(num1, num2)}")


