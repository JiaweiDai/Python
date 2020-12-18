# tuple is alike to list, but you can't change the value in a tuple, you also could consider a string as a tuple
tuple1 = ('a', 'b', 'c', 'd')
tuple2 = ('a',) # create a tuple with only one value
tuple3 = () # empty tuple

# notice : when a tuple only has one value , you need to add a ',' or the '()' will be consider as a operator
tuple4 = ('a')
print(type(tuple1))
print(type(tuple4))

# access to the value via index
print(tuple1[1])

# Tuple is not allow to change any of the value. but you can connect them into one.
tuple5 = (1, 2, 3, 4)
tuple6 = tuple1 + tuple5
print(tuple6)

# You can't change or delete a value in a tuple , but you can delete a tuple, I mean delete it in memory.
del tuple6
#print(tuple6)

# len(tuple) return a int ,shows how many values in a tuple.
print(len(tuple1))

# tuple1 + tuple2 return a tuple, make a connection. Shows above.
# tuple * m return a tuple .Copy tuple for m times
print(tuple1 * 2)

# x in tuple return True/False to see if x in tuple or not.
print('f' in tuple1)

# for x in tuple, print the values in the tuple by iteration.
for x in tuple1:
    print(x)

# len(tuple) show how many values there.
# max(tuple) return the maximum value.
# min(tuple) return the minimum value.
# tuple(list) turn a list into a tuple.