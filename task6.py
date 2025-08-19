# #make a complete register and login system using dictionary using update method method
credentials={
     "bhuban":"bhu123"
}
choice=input("enter your choice 1.register,2.login")
match choice:
    case'register':
        username=input("enter user name")
        password=input("enter a password")
        credentials.update({username:password})
        print("register successfully")

    case'login':
        username=input("enter the username")
        password=input("enter the password")
        if username in credentials and credentials.get(username)==password:
            print("login successfully")
        else:print("login failed")
    case _:
        print("input id invalid")


#Create a list of usernames Input a username from the user Check if the username is present in the list or not

# lists=["bhuban","ram","hari",'shyam']
# user=(input("enter the username"))
# if user in lists:
#     print("username is present in lists")
# else:
#     print("username is not present in list")


# Create a dictionary of usernames and passwords, extract all the usernames from 
# #the dictionary and 	input username from the user and check if the 	username is present in the extracted list of 	usernames
# dictionary={
#     "bhuban":"bhuban123",
#     "hari":"hari88",
#     "shyam":"shy221",
#     "krishna":"krishna"
# }
# a=dictionary.keys()
# user=input("enter the username")
# if user in a :
#     print("a is present in extract list")
# else:
#     print("a is not present is extract list")

# Task: Create a simple calculator system
num1=float(int(input("enter the first number")))
num2=float(int(input("enter the second number")))
operators=input("choose a operator among + , - , / , * , ** , % ")
if operators is "+":
    print("sum of two number is:",num1+num2)
elif operators is "-":
    print("subtraction of two number is:",num1-num2)
elif operators is "*":
    print("multiplication of two number is:",num1*num2)
elif operators is "/":
    print("subtraction of two number is:",num1/num2)
elif operators is "%":
    print("subtraction of two number is:",num1%num2)
elif operators is "**":
    print("subtraction of two number is:",num1**num2)

#WAP to find the greatest number among three number, number is given by user
no1=float(input("enter the first number"))
no2=float(input("enter the second number"))
no3=float(input("enter the third number"))
if no1>no2 and no1>no3:
    print(f"number1 {no1} is the greater number")
elif no2>no1 and no2>no3:
    print(f"number2 {no2} is the greater number")
if no2>no1 and no3>no2:
    print(f"number3 {no3} is the greater number")

