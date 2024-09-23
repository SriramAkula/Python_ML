# arbitary arguments in python
# Program to find the sum of multiple numbers

def find_sum(*numbers):
    result=0
    for num in numbers:
        result=result+num
    print("Sum = ",result)
find_sum(2,3,3)
find_sum(1,2,3,4,5,6,7,8)