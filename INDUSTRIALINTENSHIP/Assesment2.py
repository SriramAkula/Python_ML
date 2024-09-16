def factorial():
    N = int(input("Enter the Num: "))
    res = 1
    while N > 0:
        res *= N
        N -= 1
    print("The Factorial of Num: ", res)

factorial()
