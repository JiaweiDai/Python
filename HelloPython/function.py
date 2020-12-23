# function code block start with def then function name and ()
# any parameter and self variable should in () and () could use on define parameter.
# in the first line of a function you can choice if you want to put some statement there.
# function inside start with :
# return[] end a function , if you just put a return there , means return None.

# in python, String, tuples and bumbers are imutable object, list and dict are mutable object.
# imutable: first a = 5 then a = 10, actually there is a new object 10 then we make a point to it and 5 has been abandon,
# not we change a's value. we can consider there is a new a.
# mutable: list = [1, 2, 3, 4] then list[2] = 5 is we change the second value of the list but list is not changed.

# parameter passing in Python.
# 1. imutable: samilar as C, we can pass int, string, tuple; such as fun(a), what we pass is a's value, not object a;
# when we change the a's value in fun(a), it changed another copy of a, not change a.
# 2. mutable: similar as C, if we use func(list), we pass the real list, we change list in func(list) out side of the list also change.
# In python everything is object, we just could say we pass mutable object or imutable object.

# anonymous function is a very important part of Python, normally we use it on simply logic, key word is lamba.

sum = lambda x, y : x + y
print(sum(2, 3))

# we also could make a simple sort. We usually use lambda as a paremeter as a sort function.
students = [{"name": "Andy", "age": 26}, {"name": "Acumen", "age": 30}, {"name": "Ramos", "age": 27}, {"name": "Lucas", "age": 25}]
students.sort(key = lambda student : student["age"])
print(students)

# python is dynamic lauguage, function can use as mothod's paremeter.
def test(a, b, methodx):
    return methodx(a, b)
methodx = input("Please enter something: ")
methodx = eval(methodx)
print(test(30, 20, methodx))
