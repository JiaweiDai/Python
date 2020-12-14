# access to the list
list0 = ["a", "b", "c", "d"]
print(list0)
print(list0[1])
print(list0[1:3])

# update a list
list0[1] = "g"
print(list0)

# delete a value in a list
del list0[1]
print(list0)

# len(list) return an int for how long is the list.
print(len(list0))

#list1 + list2 return a list to combine two lists.
list1 = ["x", "y", "z"]
list2 = list1 + list0 
print(list2)
print(list0 + list1)

# list * m return a list for looping a list.
list2 = list1 * 3
print(list2)
print(list0 * 3)

# x in list return True/False to check if x in list or not.
print("a" in list1)

# print as iteration, I don't quite understand what is iteration,
# I think it is just print in an order.
for x in list0:
    print(x)

#print the max in a list 
print(max(list0))

#print the min in a list
print(min(list0))

# by using list(seq) to convert a tuple to a list
tuple1 = ("a", "b", "c")
print(tuple1)
print(list(tuple1))

#list.append add new value into a list
print(list0)
list0.append("h")
print(list0)

# list.count(obj) count the value in the list
print(list0.count("a"))

# list.extend(seq) something like append , but this function is adding a list.
list0.extend(list0)
print(list0)

# list.index(obj) find the first obj's index
print(list0.index("h"))

# list.insert(index, obj) insert obj into the index
list0.insert(4, "f")
print(list0)

# list.pop(obj = list[-1]) remove a value ,by default it remove the last one and return this value
print(list0.pop())
print(list0)
print(list0.pop(4))
print(list0)

# list.remove(obj) remove the first obj in the list.
list0.remove("d")
print(list0)

# list.reverse() reverse the list, no return value
list0.reverse()
print(list0)

# list.sort([function]) sort the list. By default it is going up.
# There is a sorted() in Python, list.sort() only could use for list but sorted() could using on all iterable.
list0.sort()
print(list0)
list0.sort(reverse = True)
print(list0)
# something using function, if we have a list which valued by tuple
def take(val):
    return val[0]

list3 = [(2, 2), (3, 4), (4, 1), (1, 3)]
list3.sort(key = take)
print(list3)

# list.clear() clear a list
list3.clear()
print(list3)

# list.copy copy a list, return a new list
list4 = list2
print(list4)
list3.clear()
list5 = list2.copy()
print(list5)