arg = "Hello World!"
# something like slice.
print(arg[0])
print(arg[1:5])


#use + to concatenate strings.But not recommanded, because of this type will reassign memory.
print(arg[:6] + "Jeremy")

#you also could use join in a set or list.
list = ["a", "b", "c", "d"]
str = "".join(list)
print(str)

#recommand use %s to print.
print("user name: %s, password: %s" % ("daijwei","daijwei"))

#use format fuction.
print("My name is {name} and I'm {age} years old".format(name = "daijwei", age = 28))

# + concatenate strings 
# * repeat print strings 
# [] cut one letter in a string
# [:] cut part of the string
# in if the tring include spicfic letters return true.
# ont in : if the string not include spicfic letters return true.
# r/R original string.
# % format string , like sprintf in C. 
arg1 = "Hello"
arg2 = "Jeremy"

print(arg1 + " " + arg2)
print(arg1*2)
print(arg[1])
print(arg1[1:3])
print("lo" in arg1)
print("lo" not in arg1)
print("\n")
print(r"\n")
print(R"\n")
print("user name: %s, password: %s" % ("daijwei","daijwei"))

# ASCII . ord("A")  chr(number)
print(ord('a'))
print(chr(65))

