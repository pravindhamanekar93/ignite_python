# ** means power 
x=2
y=5
print(x**y)
# // means floor division
a=15
b=2
print(a//b)

# Python has two division operators:

# / - Division (returns a float)
# // - Floor division (returns an integer)

# not operator 
a=True
b=False
print(not a)
print(not b)

# Identity Operators
# Identity operators are used to compare the objects, not if they are equal, but if they are actually the same object, with the same memory location:

# is operator returns true if both variables are the same objects
# is not operator return true if both vairables are not the same object

a = [1,2,3]
b = [1,2,3]
print(a is b)
print(a is not b)

# Membership operators are used to test if a sequence is presented in an object:
# in operator Returns True if a sequence with the specified value is present in the object
# not in operator Returns True if a sequence with the specified value is not present in the object

fruits = ["apple", "banana", "cherry"]

print("banana" in fruits)
# print("orannge ")
