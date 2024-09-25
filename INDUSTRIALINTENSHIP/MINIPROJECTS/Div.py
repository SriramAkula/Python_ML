a=int(input("Enter num1: "))
b=int(input("Enter num2: "))

try:
    div=a/b
    print(div)
except ZeroDivisionError:
    print("Division by Zero is not possible")