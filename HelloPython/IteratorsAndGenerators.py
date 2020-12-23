import sys
# Iterator is an object which could memries all the iterations' position. Iterator object read the value at first place and end with 
# the last one and it never goes back.
list1 = [1, 2, 3, 4, 5]
it = iter(list1)
print(next(it))
print(next(it))

it2 = iter(list1)
for x in it2:
    print(x)

it3 = iter(list1)
while True:
    try:
        print(next(it3))
    except StopIteration:
        print("No values there")
#        sys.exit()
        break
print("#############################################")
# Generators are a simple and powerful tool for creating iterators. They are written like regular functions but use the yield statement 
# whenever they want to return data. Each time next() is called on it, the generator resumes where it left off 
# (it remembers all the data values and which statement was last executed).
# To see how yeild work , let's use some codes to test.
# Version 1.
def FabV1(max):
    n, a, b = 0, 0, 1
    while n < max:
        print(b)
        a, b = b, a + b
        n = n + 1
FabV1(5)
print("#############################################")
# Version 2. As we can see, the version 1 we use print() to print the result, that makes the FabV1 function can't be reused,
# because of there is no reuturn other functions can't get the list which this function out put. Then we have Version 2.
def FabV2(max):
    n, a, b = 0, 0, 1
    L = []
    while n < max:
        L.append(b)
        a, b = b, a + b
        n = n + 1
    return L
for n in FabV2(5):
    print(n)
print("#############################################")
# Version 3. Ver 2 we can reuse the fuction, but the expert will say when max is a large number that makes the fuction use lots of memory
# if we want to control the memory use, we beter use iterable object to make some iteration.
class FabV3(object):
    def __init__(self, max):
        self.max = max
        self.n, self.a, self.b = 0, 0, 1
    
    def __iter__(self):
        return self
    
    def __next__(self):
        if self.n < self.max:
            res = self.b
            self.a, self.b = self.b, self.a + self.b
            self.n = self.n + 1
            return res
        raise StopIteration()

for n in FabV3(5):
    print(n)
print("#############################################")
# Version 4.
def FabV4(max):
    n, a, b = 0, 0, 1
    while n < max:
        yield b
        a, b = b, a + b
        n = n + 1
for n in FabV4(5):
    print(n)

# or you can just consider yield as a iterator, every time we met yield fuctions stop and save all the running data
# and return the value of yield, when next time we run next() we start at this position.
def fun(n):
    """Here is an instrument of this function.
    This function works with yield"""
    while n> 0:
        n -= 1
        yield n
f = fun(10)
print(type(f))
while True:
    try:
        print(next(f), end = ',')
    except StopIteration:
        sys.exit()