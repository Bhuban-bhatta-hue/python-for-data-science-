#task update the calculator using function and keyword of positional argument  and use loop
def sum(a,b):
    print(f"sum of two number {a} and  {b} is: " ,a+b)

def subtraction(a,b):
    print(f"subtraction of two number {a} and {b} is: " ,a-b)

def division(a,b):
    if b!=0:
         print(f"division of two number {a} and  {b} is: " ,a/b)
    else:
         print("error")


def multiplication(a,b):
    print(f"multiplication of two number {a} and  {b} is: " ,a*b)

def modulo(a,b):
     if b!=0:
          print(f"modulo of two number {a} and  {b} is: " ,a%b)
     else:
          print("error")

def power(a,b):
     print(f" power of two number {a} and  {b} is: " ,a**b)
    
while True:
     choice=input(" enter 1 for addition,2 for subtraction,3 for division, 4 for multiplication,\n 5 for modulo,6 for power, 7. for exist :")
     num1=int(input("enter the first number:"))
     num2=int(input("enter the second number:")) 
     match choice:
          case "1":
               sum(num1,num2)#positional argument take argumwnt according position(args)
          case "2":
               subtraction(a=num1,b=num2)#keyword argument-key value pair (kwargs)
          case "3":
                division(num1,num2)
               
          case "4":
               multiplication(num1,num2)
          case "5":
               modulo(num1,num2)
          
          case "6":
               power(num1,num2)
          case "7":
               print("exist.........")
               break




#TASK:update login register program using loops and function
user={
     "bhuban":"bhub123",
     "dipak":"dipak123"
}
def register():
     username=input("enter the username")
     if username in user:
          print("username is already exist:")
     else:
          password=input("enter the password")
          user[username]=password
          print(f"user '{username}' register successfully")
def login():
      
      username=input("enter the username")
      password=input("enter the password")
      if username in user and user[username]==password:
           print(f" user '{username}'login successfully")
           return username
      else:
           print("login failed")
           return None

def update():
     username=login()
     if username:
          choice=input("enter 1 for username update \n 2. for password update")
          if choice =="1":
               new_username=input("enter new username")
               if new_username in user:
                    print("username is already exist please enter another name")
               else:
                    user[new_username]=user.pop(username)
                    print(f"username update to '{new_username}'")
          elif choice =="2":
               new_password=input("enter the new password")
               user[username]=new_password
               print("password is update")
          else:
               print("invalid choice")

while True:
     choice=input("enter 1. for register, 2.for login, 3. for update, 4. for exist:")
     match choice:
          case "1":
               register()
          case "2":
               login()
          case "3":
               update()
          case "4":
               print("exist.....")
               break

