cp=int(input("Enter Cost Price of bike: "))
tax=0
if cp>100000:
    tax=(15*cp)/100
elif cp>50000 and cp<=100000:
    tax=(10*cp)/100
else:
    tax=(5*cp)/100
print("Tax: ",tax)