num1=int(input("enter first number:"))
num2=int(input("enter second number:"))
print(num1+num2)


name=input("enter tne name:")
if "B"in name:
    print("b is present:")
else:
    print("b is not present:")


#LIST: List is a data type  that can hold different data type valuee -even we store multiple list in main list called nested list
# used [] to define a list
z=[1,2,3,4.5,6.5,"bhuban",[1,2,3,4]]
print(z)
print(type(z))
#3append method:add the element end of the list
z.append(9)
print(z)

#count:count the elements of the list
print(z.count("bhuban"))

#index:return the index of the element
print(z.index(3))
#index always starts from 0
print(z[0])
print(z[5])

# #list slicing:creating a new list from orginal list :in slicing list element must be in oginal list

b=z[0:6]
print(b)

# #Task:end sling 
c=b[:5]
print(c)
d=z[:5]
print(d)
#starting slicing
e=z[4:]
print(e)

# #positive index with step
# #step:it jump from 0 index to 3 ,3 index to 5 because we use step to 
# f=a[::2]
# print(f)
#negative 
g=z[-1:-5:-1]
print(g)
h=z[-5:-1:2]
print(h)

# # #list

# #we also have same indexing and slicing in python string
# #implementing all the indexing and slicing in sring
string="Bhuban bhatta"
k=string[2]
print(k)


thislist=["baba","aama","aama","dada","did","bhai"]
#append()method
thislist.append("aunty")
print(thislist)

#copy()method
thislist.copy()
print(thislist)

#count()method
a=thislist.count("aama")
print(a)

#extend()method
b=["bhuban","biraj","premraj"]
thislist.extend(b)
print(thislist)

#index()method
c=thislist.index("bhuban")
print(c)

#insert()method
thislist.insert(3,"bhatta")
print(thislist)

#pop method
thislist.pop(3)
print(thislist)

#remove()method
thislist.remove("baba")
print(thislist)

#reverse() method
thislist.reverse()
print(thislist)

#sort() method
thislist.sort()
print(thislist)

#reverse sorting method in list 
print(thislist[-1:-5:-1])
print(thislist[-2:-4:-2])
if "baba"in thislist:
    print(True)
else:
    print(False)
thislist.insert(2,"uncle")
print(thislist)

#clear()method
thislist.clear()
print(thislist)

#task: implement all sorting method in string
string=("this is our DATA SCIENCE 5th class")
e=string[2:5]
print(e)

#slice from start
print(string[:6])

#slice from end
print(string[2:])

#slice with index
print(string[::2])

#negative slice

#slice from start
print(string[0:-1])

#slice from  end
print(string[-1:0:-1])

#-ve slice with index
print(string[::-2])