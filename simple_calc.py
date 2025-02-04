# prompt user for 2 numbers
num1 = float(input("Enter first number:  "))
num2= float(input("Enter first number:  "))

# prompt user to enter operator
operator=input("Enter an operator(=,-,*,/):")
# perform calculation based on operator
if    operator =="+":
    result=num1+num2
elif operator == "-":
    result=num1-num2
elif operator == "*":
    result=num1*num2
elif operator == "/":
    if num1%num2==0:
                result=num1/num2
    else:
                result="Error , divisible by zero"
else:
        result="Invalid Opperator"
print(f"The answer is {result}")
