# #strip()-trim the string means 

# string= "       bhuban bhatta      "
# print(string.strip())

# #split-return the list of string and we use seperatorlike (, used in below example) in split that unique that another character to seperate string (use in authentication)

# string= "vollyball,football,cricket,kabidi"
# print(string.split(","))


# #toples:Tuple is a immutable data type in python  in python wraps element in()
# tup=(1,2,3,4,5,6,7)
# print(type(tup))
# print(tup[1])
# print(tup[-1])
# print(tup[::2])
# print(tup[0:6:2])
# print(tup[-1:-6:-3])
# print(tup[::-2])
# #todo-perform indexing and slicing 
# y=list(tup)
# y[1]=9
# x=tuple(y)
# print(x)

# #Boolean datatype-this data type is either true or false
# print(5>2)
# print(10<2)

# #set()-set data type is also a mutable data type enclosed with{}but the index in set is not fix.
# b={1,2,3,4,5,"bhuban",6,7,8,"bhatta","bhat"}
# c={3,4,5,6}
# print(b.union(c))
# print(b.intersection(c))
# print(b.difference(c))
# print(c.difference(b))
#task- ADD COPY ADD POP REMOVE UPDATE OF  ALL SET METHOD
#add
# b.add("kabir")
# print(b)
# print(b.copy())
# b.discard("bhat")
# print(b)
#difference_update()remove the item that exist in both sets
# b.difference_update(c)
# print(b)
# print(b.clear())

#discard:remove the specific element
# c.discard("bhawana")
# print(c)

# #isdisjoint: return true if no item in set b is present in set c
# d=b.isdisjoint(c)
# print(d)

# #issubset: return true if all item of b sets is present in c set
# e=c.issubset(b)
# print(e)
# #issuperset:just opposite of issubset
# print(b.issuperset(c))

# #remove: remove specified element from the set
# b.remove("bhat")
# print(b)

# #symmetric_difference : return all difference element from both set expect common element of both set
# print(b.symmetric_difference(c))

#update(): insert the element from set c into set b

# b.update(c)
# print(b)

# # ##pop():remove all the element from the set
# print(b.pop())

#dictionary: to store data value in key:value pairs.
#we used corly bracket {} to define the dictionary
dictionary ={ "username":"bhuban123",
             "hobby":"coding",
             "age":23
             }
# print(dictionary)
# print(dictionary.keys())
# print(dictionary.values())
#copy():return copy of a dictionary
# print(dictionary.copy())
# #get():get the specified value
# print(dictionary.get("hobby"))

# #key():return key of dictionary
# print(dictionary.keys())

#pop():remove thr element eith specified key
# dictionary.pop("age")
# print(dictionary)

#popitem():remove last item from dictionary

# dictionary.popitem()
# print(dictionary)

##update(): insert an item to the dictionary
dictionary.update({"roll_no":7})
print(dictionary)

#value():return the value of dict
print(dictionary.values())
# #we used dict() to cast value in dictionary
# name="bhuban"
# caste="bhatta"
# dict_cast={name:caste}
# print(dict_cast)
# print(dictionary.get("hobby"))
# print(type(dict_cast)) 

