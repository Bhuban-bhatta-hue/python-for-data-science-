#task:use list comprehension to find even number from 1 to 100 ,100 be inclusive
# list2=[1,2,3,4]
# list3=[x for x in range(1,101)]
# for y in list3:
#     if y%2==0:
#         print(y)
# # find the average of three number using lambda function
# average=lambda a,b,c:(a+b+c)/3
# print(average(2,3,4))

#make calculator using lambda function
# num1=int(input("enter the first number:"))
# num2=int(input("enter the second number:"))
# choice=input("Enter 1. for sum, 2. for subtraction, 3. for multiplication, 4 for division,\n 5 for modulo, 6 for power, 7 for exist:")
# match choice:
#     case "1":
#         sum=lambda a,b:(a+b)
#         print(sum(num1,num2))
#     case "2":
#         subtraction=lambda a,b:(a-b)
#         print(subtraction(num1,num2))
#     case "3":
#          multiplication=lambda a,b:(a*b)
#          print(multiplication(num1,num2))
#     case "4":
#          division=lambda a,b:(a/b)
#          print(division(num1,num2))   
#     case "5":
#           modulo=lambda a,b:(a%b)
#           print(modulo(num1,num2)) 
#     case "6":
#           power=lambda a,b:(a**b)
#           print(power(num1,num2)) 
#     case "7":
#           print("please enter valid data")
#     case _:
#           print("exist.......")

#make table count using lambda functiom
# num=int(input("enter the number whome table you want"))
# table=lambda num,i:(num ,'*' ,i,'=',num*i)
# for i in range(1,11):
#     print(table(num,i))

#Write a PHP program using a lambda function to square each number in an array.
#Input: [1, 2, 3, 4, 5] → Output: [1, 4, 9, 16, 25]
# num=[1,2,3,4,5]
# quare=list(map(lambda x:x**2,num))
# print(quare)

#Use a lambda function to convert an array of strings into uppercase.
#Input: ["php", "python", "java"] → Output: ["PHP", "PYTHON", "JAVA"]
# input=["php","python","java"]
# g=list(map(lambda x:x.upper(),input))
# print(g)

#Use array_filter() with a lambda to keep only even numbers from [1,2,3,4,5,6,7,8,9,10]
# num=[1,2,3,4,5,6,7,8,9,10]
# even=list(filter(lambda x:x%2==0,num))
# print(even)

#From an array of names ["Ram", "Sita", "Dipak", "Bhuban"], filter names that start with "D".
# name=["Ram", "Sita", "Dipak", "Bhuban"]
# start=list(filter(lambda x:x.startswith("D"),name))
# print(start)

#Use array_reduce() to calculate the sum of numbers [10, 20, 30, 40]
# from functools import reduce
# numbers=[10,20,30,40]
# sum_all=reduce(lambda x,y:x+y,numbers)
# print(sum_all)

#Use array_reduce() with a lambda to find the longest string in an array:
# Input: ["apple", "banana", "grapes", "watermelon"] → Output: "watermelon"
# from functools import reduce
# inputs=["apple", "banana", "grapes", "watermelon"]
# longes_str=reduce(lambda x,y:x if len(x)>len(y) else y,inputs)
# print(longes_str)

#Combine two arrays into pairs (like zip):
# Input: [1,2,3] and ["a","b","c"] → Output: [[1,"a"], [2,"b"], [3,"c"]]
# input1=[1,2,3]
# input2=["a","b","c"]
# output=[[x,y] for x,y in zip(input1,input2)]
# print(output)

# #Add two lists element-wise using array_map() (zip style):
# #Input: [1,2,3], [4,5,6] → Output: [5,7,9]
# num1=[1,2,3]
# num2=[4,5,6]
# sums=[a+b for a,b in zip(num1,num2)]
# print(sums)

# Given an array [1,2,3,4,5,6,7,8,9,10]:
# Use array_filter() to get even numbers. Then use array_map() with a lambda to square them.
# Then use array_reduce() to sum the squares. Final result should be: 220


# array =[1,2,3,4,5,6,7,8,9,10]
# even=list(filter(lambda x : x%2==0,array))
# print(even)
# square_even=list(map(lambda x:x**2,even))
# print(square_even)

# from functools import reduce
# sums=reduce(lambda x,y:x+y,square_even)
# print(sums)

# 1. Create a program to take a string input from the user and print its length.
# user=input("enter the string:")
# print(len(user))

# 2. Write a program to convert a list of strings into a list of integers.
# list1=["1","2","3"]
# print(type(list))
# list2=list(map(int,list1))
# print(list2)

# 3. Write a program to check if a given number is even or odd.

# num=int(input("enter the number:"))
# if num%2==0:
#     print(f"{num} is even number")
# else:
#     print(f"{num} is odd number:")



 
# 4. Write a program to find the largest of three numbers entered by the user.
# num1=int(input("enter the first number:"))
# num2=int(input("enter the second number:"))
# num3=int(input("enter the third number:"))
# if num1>num2 and num1>num3:
#     print(f"{num1}is the greater number is num1")
# elif num2>num1 and num2>num3:
#     print(f"{num2} is the greater number")
# else:
#     print(f"{num3} is the grater number:")

# 5. Write a program to print the multiplication table of a given number.
# num=int(input("enter the number"))
# for i in  range(1,11):
#     print(f"{num} * {i} = {num*i}")
# 6. Write a program to print all numbers from 1 to 50 that are divisible by 5.
# for i in range(1,51):
#     if i%5==0:
#         print(i)
# 7. Write a program to count how many vowels are present in a given string.

# def count_vowel(text):
#     vowels="aeiouAEIOU"
#     count=0
#     for char in text:
#         if char in vowels:
#             count +=1
#     return count
# string="bhuban bhatta"
# print("vowel:",count_vowel(string))

# 8. Write a program to print the factorial of a number using a while loop.
# def count_vowels(text):
#     vowels = "aeiouAEIOU"
#     count = 0
#     for char in text:
#         if char in vowels:
#             count += 1
#     return count
# string = input("Enter a string: ")
# print("Number of vowels:", count_vowels(string))

# 9. Write a function to check whether a given number is prime or not.
# def is_prime(num):
#     if num <= 1:
#         return False   # 0 and 1 are not prime
#     for i in range(2, int(num**0.5) + 1):  # check till sqrt(num)
#         if num % i == 0:
#             return False
#     return True
# n = int(input("Enter a number: "))
# if is_prime(n):
#     print(f"{n} is a Prime number")
# else:
#     print(f"{n} is Not a Prime number")

# 10. Write a function to reverse a string without using built-in functions like [::-1] or reversed().
def reverse_string(s):
    result = ""
    for char in s:
        result = char + result   # prepend each character
    return result

# Example usage
string = input("Enter a string: ")
print("Reversed string:", reverse_string(string))
