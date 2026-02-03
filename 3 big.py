a = int(input("Enter 1  no:"))
b = int(input("Enter 2 no:"))
c = int(input("Enter 3 no:"))

if a>b and a>c:
    print("A is the biggest ")
elif b>a and b>c:
    print("B is the biggest") 
elif a==b and a==c:
    print("All num are same")  
else:
    print("C is biggest")    