m1 = int(input("Enter marks of first sub: "))
m2 = int(input("Enter marks of first sub: "))
m3 = int(input("Enter marks of first sub: "))

avg = (m1+m2+m3)/3
print("Average Marks: ",avg)

if avg>90:
    print("Grade A")
elif avg>80 and avg<=90:
    print("Grade B")
elif avg>60 and avg<=80:
    print("Grade C")
else:
    print("Grade D")
