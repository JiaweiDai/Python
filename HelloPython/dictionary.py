# dictionary is a changable container data module, you can stored any datatype in a dictionary, no order.
# every key==>value are seprate by :, every pair seprate by ',', they are all in a {}.
# dict1 = {key1 : value1, key2 : value2}
# key must be uniq , values are not . If you store using a key that is already in use, the old value associated with that key is forgotten.
 
#dict0 = {1 : 'a', 2 : 'b', 3 : 'c', 1 : 'd'}
#print(dict0)

# get a value regarding a key.
# It is an error to extract a value using a non-existent key.
dict1 = {1 : 'a', 2 : 'b', 3 : 'c', 4 : 'd', 5 : [1, 2, 3, 4]}
print(dict1[3])

# change values in dictionary
# update key 3
dict1[3] = 'f'
print(dict1)
# add new key-value pair
dict1[6] = 'g'
print(dict1)
# delete one key-value pair
del dict1[1]
print(dict1)

# len(dict) how many keys are there.
print(len(dict1))
#print(len(dict0))
# str(dict) print dictionary as string.
print(str(dict1))
str1 = str(dict1)
print(type(str1))
print(str1)

# dict.copy() return a dictionary's copy (), shadow copy.
# By shadow copying it means the content of the dictionary is not copied by value, but just creating a new reference.
# by using = operator and dict.copy is different kind of shaow copy.
# by using = operator it just make a reference.
# by using dict.copy for father object , it is a deep copy and for son object , it still a reference.
dict2 = dict1.copy()
dict3 = dict1
print(dict1, '###', dict2, '###', dict3)
print("#############################################")
dict1[6] = 'x'
print(dict1, '###', dict2, '###', dict3)
print("#############################################")
dict1[5].append(5)
print(dict1, '###', dict2, '###', dict3)
print("#############################################")
dict3[2] = 'y'
print(dict1, '###', dict2, '###', dict3)
print("#############################################")
dict2[5].append(12)
print(dict1, '###', dict2, '###', dict3)

# dict.clear() delete all the values.
dict2.clear()
print(dict2)
print(dict1, '###', dict2, '###', dict3)

# dict.fromkeys(seq) use the values in seq as key to create a dictionary, but remember use dict.fromkeys() not varname.fromkeys
list0 = ["a", "b", "c", "d"]
dict4 = dict.fromkeys(list0)
print(dict4)

# dict.get(key, default=None) return the key's value , if there is nothing , return default
print(dict1.get(3))
print(dict1.get(10,"Hello"))

# dict.key in d to see if the key in this dictionary, return True/False.
print(2 in dict1)

# dict.items() return a new view object.!!!!!!!!!!!!!!!!!!!!!!
print(dict1.items())
dict5 = dict1.items()
print("type of dict5 is ", type(dict5))

# dict.keys() return all the keys in a dictionary
print(dict1.keys())

# dict.values() return all the values in a dictionary
print(dict1.values())

# dict.setdefault(key, default=None) if the key is not in this dictionary, will add the key and set value as default and return the value.
# If the key is there then return the value.
print(dict1.setdefault(2))
print(dict1.setdefault(1))
print(dict1.setdefault(10, "hello"))

# dict.update(dict2) it accept another dictionary object or something include a key-value pair(legth of two list/Tuple) iterable object.
dict1.update(dict4)
print(dict1) 
dict1.update(F = "Acumen", H = "Lacus")
print(dict1) 
list1 = [('f', "Jeremy"),('q', "Ramos")]
dict4.update(list1)
print(dict4)
tuple0 = ((1, "Nothing"),)
dict4.update(tuple0)
print(dict4)
# if dict2's key already in dict , then the dict2's value will overwrite exisitng keys
dict1.update(dict4)
print(dict1) 

# dict.pop(key[,defalut]) if key is in the dictionary, remove it and return its value, else return default. If default is not given
# then raise a key Error
#print(dict1.pop('y'))
print(dict1.pop('y', "Hey"))
print(dict1.pop('c'))

# dict.popitem() remove a key-value pair and return them. Pairs are returned in LIFO(Last in First out) order.
print(dict1.popitem())
print(dict1.popitem())
print(dict1)