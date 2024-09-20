try:
    even_num=[2,4,6,8]
    print(even_num[4])
except IndexError:
    print("Index Out of Bounds")
except ZeroDivisionError:
    print("Denominator cant be zero")