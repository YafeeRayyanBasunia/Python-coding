a = float(input("Enter 1 no: "))
b = float(input("Enter 2 no: "))
c = float(input("Enter 3 no: "))

if a<b and a<c:
    print("A is small")
elif b<a and b<c:
    print("B is small")
elif a==b and a==c:
    print("All number are same") 
else:
    print("C is small")  

