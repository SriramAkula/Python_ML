def calculate_factorial(num):
    prod=1
    temp=num
    while(num!=0):
        prod=prod*num
        num=num-1
    print("Factorial of",temp,"is",prod)
    
num = int(input("Enter a num: "))
calculate_factorial(num)