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

print(str[1:3] * 2)