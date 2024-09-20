# n=int(input("Enter num: "))
# if(n%2==0):
#     try:
#         m=1/n
#         print(" 1 /",n)
#     except:
#         print("Zero division error")

try:
    num=int(input("Enter num: "))
    assert num%2==0

except:
    print("Not an even number")
else:
    try:
        reciprocal=1/num
        print(reciprocal)
    except ZeroDivisionError:
        print("Can not reciprocal Zero")
finally:
    print("This is finally block")