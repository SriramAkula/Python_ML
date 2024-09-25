def table(num):
    prod=1
    temp=num
    while(prod<=20):
        res=num*prod
        print(num,"*",prod,"=",res)
        prod=prod+1
    
num = int(input("Enter a num: "))
table(num)