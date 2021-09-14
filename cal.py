
num1= int (input("Enter your first number: "))
num2= int (input("Enter your second number: "))

print("Enter your choose ")

print("Addition +")
print("multiplication *")
print("subtraction -")
print("division /")
print("reminder %")
print("power **")

choose= input("select you choose for calulation: ")



if choose=="+":
    print("Sum of these number is", num1+num2)

elif choose=="*":
    print("multiplication of these number is", num1*num2)

elif choose=="-":
    print("subtraction of these number is", num1-num2)

elif choose=="/":
    print("division of these number is", num1/num2)

elif choose=="%":
    print("reminder of these number is", num1%num2)

elif choose=="**":
    print("power of this number is", num1**num2)

else:
    print("you entered invaild number")
