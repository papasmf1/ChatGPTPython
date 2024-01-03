#Chap03_ChatGPT_사칙연산하는함수.py

def calculator(a, b, operator):
    if operator == '+':
        return a + b
    elif operator == '-':
        return a - b
    elif operator == '*':
        return a * b
    elif operator == '/':
        if b != 0:
            return a / b
        else:
            return "Error: Division by zero!"
    else:
        return "Error: Invalid operator!"

# 사용 예시
result = calculator(4, 2, '+')  # 덧셈
print(result)  # 출력: 6

result = calculator(4, 2, '-')  # 뺄셈
print(result)  # 출력: 2

result = calculator(4, 2, '*')  # 곱셈
print(result)  # 출력: 8

result = calculator(4, 2, '/')  # 나눗셈
print(result)  # 출력: 2.0

result = calculator(4, 0, '/')  # 0으로 나누기
print(result)  # 출력: Error: Division by zero!

result = calculator(4, 2, '%')  # 잘못된 연산자
print(result)  # 출력: Error: Invalid operator!
