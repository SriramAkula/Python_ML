# greet = lambda:print("Hello World")
# greet = lambda name : print("Hello",name)
# greet("rohan")

# list1=[1,5,2,6,8,11,3,12]
# list2=list(filter(lambda x:(x%2==0),list1))

# print(list2)

list1=[1,5,2,6,8,11,3,12]
list2=list(map(lambda x: x*2,list1))
print(list2)