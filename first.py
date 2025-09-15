import numpy as np
# list1=[1,2,3,4,5,6,7,8,9,10,11,22,33,44,55,66,77,88,99,90]
# list2=[21,22,23,3,44,54,65,67,87,8,86,43,34,67,87,87,34,23,13,23]

# def addition():
#     list3=[x+y for x,y in zip(list1,list2)]
#     list_1=np.array(list3)
#     print(list_1)
# def subtraction():
#     list4=[x-y for x,y in zip(list1,list2)]
#     list_2=np.array(list4)
#     print(list_2)
# def multiplication():
#     list5=[x*y for x,y in zip(list1,list2)]
#     list_5=np.array(list5)
#     print(list_5)
# def division():
#     list6=[x/y for x,y in zip(list1,list2)]
#     list_6=np.array(list6)
#     print(list_6)

# def modulo():
#     list7=[x%y for x,y in zip(list1,list2)]
#     list_7=np.array(list7)
#     print(list_7)

# def power():
#     list8=[x**y for x,y in zip(list1,list2)]
#     list_8=np.array(list8)
#     print(list_8)

# while True:
#     choice=input("Enter a for sum,\n s for subtraction,\n m for multiplication,\n d for division,\n mo for modulo, \n p for power,\n e for exist")
#     if choice=="a":
#         addition()
#     elif choice=="s":
#         subtraction()
#     elif choice=="m":
#         multiplication()
#     elif choice=="d":
#         division()
#     elif choice=="mo":
#         modulo()
#     elif choice=="p":
#         power()
#     elif choice=="e":
#         break
    

array1=np.array([1,2,3,4,5,6,7,8,9,10])
number_copy=array1.copy()

bolean=number_copy%2==0
print(number_copy[bolean])