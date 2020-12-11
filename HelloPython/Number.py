# There are three type of number in Python.
# int : you can use it as Long cause thre is no limit
# float : 1.20
# comlemx : a + bj or complemx(a, b)

# divide always return a float ,if you want a int ,use //
# in interactive mode , the last result always assigned to _, and you can just consider _ as a readonly variable.

import random

# from 1 -- 10 get a random one.
print(random.choice(range(1, 10)))
# from 1 -- 100 get a odd one.
print(random.randrange(1, 100, 2))
# from 1 -- 100 get a random one.
print(random.randrange(100))
# get a random one.(0, 1)
print(random.random())
#there is a seed in random, you don't need to set one, because you don't know how seed works.
#random.seed(10)
print(random.random())

#use shuffle make some choas in a list.
list = [20, 30, 40, 50]
random.shuffle(list)
print(list)

# get a real number between 5 - 10
print(random.uniform(5, 10))



