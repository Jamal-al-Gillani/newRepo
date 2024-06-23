a1 = int(input("Enter  number 1 : "))
a2 = int(input("Enter  number 2 : "))
a3 = int(input("Enter  number 3 : "))
a4 = int(input("Enter  number 4 : "))

if (a1>a2 and a1>a3 and a1>a4):
    print(f"Number {a1} is greater! ")
elif (a2>a1 and a2>a3 and a2>a4):
    print(f"Number {a2} is greater! ")
elif (a3>a2 and a3>a1 and a3>a4):
    print(f"Number {a3} is greater! ")
elif (a4>a2 and a4>a3 and a4>a1):
    print(f"Number {a4} is greater! ")
else:
    print("Enter valid number")