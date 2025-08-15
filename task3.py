#TASK:make a simple calculator using if elif operator 
num1=int(input("enter a first number:"))
num2=int(input("enter second number:"))
operator=input("enter the required operator")
if operator== "+":
    sum= num1+num2 
    print("sum of ",num1,"and",num2,"is :",sum)
elif(operator=="-"):
     subtraction=num1-num2
     print("subtraction of ",num1,"and",num2,"is :",subtraction)
elif(operator=="*"):
     mul=num1*num2
     print("multiply of ",num1,"and",num2,"is :",mul)
elif(operator=="/"):
     division=num1/num2
     print("Division of ",num1,"and",num2,"is :",division)
elif(operator=="%"):
     modulo=num1%num2
     print("modulo of ",num1,"and",num2,"is :",modulo)
elif(operator=="**"):
     power=num1**num2
     print("power of ",num1,"and",num2,"is :",power)
else:
     print("please enter valid operator")


