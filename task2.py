print("Welcome to our simple Calculator")
print("--------------------------------")

print("1. Add")
print("2. Subtract")
print("3. Multiply")
print("4. Divide")
choice= int(input("Choose an operation between 1 to 4 :-"))
result=0

if(choice in [1,2,3,4]):
    num1=float(input("Enter first number:"))
    num2=float(input("Enter second number:"))

    if(choice==1):
        result=num1+num2

    elif(choice==2):
        result=num1-num2

    elif(choice==3):
        result=num1*num2

    elif(choice==4):
        result=num1//num2

    
else:
    print("Invalid operation entered. Please try again...")

print("The result of the operation is {}".format(result))