w = float(input("Enter your KG: "))
h =  float(input("Enter your m: "))

bmi = w/h **2


print("your BMI", bmi)

if bmi < 18.5:
    print("You are underweight!You need to gain more weight")
elif 18.5 <= bmi <= 24.9:
    print("You are normal, Keep it up") 
elif 25 <= bmi <= 29.9: 
    print("You are overweight please loose some weight")
elif 30 <= bmi <= 34.5:
    print("You are obease")
else:
    print("You are extremly obease please visit the doctor as soon as posible")    


    