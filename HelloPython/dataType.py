import keyword

class Foo(object):
    pass

class Bar(Foo):
    pass

user = Bar()
print(type(Foo()) == Foo)
print(type(Bar()))

print(type(user))

print(isinstance(user,Bar))

print(keyword.kwlist)

str = "daijiawei"
#print(str[1:3] * 2)
#Acutally there is no duplicate value in a set and when you print it , you will find there is no sequence
set1 = {"dufu", "Lucas", "Andy", "Acumen", "Lucas", "dufu"}
set2 = set(["dufu","Andy"])
set3 = set("abcd")
print(set1)
print(set2)
print(set3)

#tuple use () and you can't change any of them .
tuple1= ("dufu", "Lucas", "Andy", "Acumen", "Lucas")

list1 = ["dufu", "Lucas", "Andy", "Acumen", "Lucas"]

if "Acumen" in set1:
    print("Acumen is here")
else:
    print("Acumen is not here")

#list user [] and you can change the value.
list1[0] = "daijiawei"

print(list1)

#dictionary is accept duplicate key ,but after print , you will find the the later one will replace the former one.
#dict ={'a': 1, 'b': 2, 'b': '3'}
dict ={'a': 1, 'b': '3'}
print(dict)


