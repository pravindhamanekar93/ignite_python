# Python Indentation
# Indentation refers to the spaces at the beginning of a code line.

if 5>2:
    print("five is greter than two")

# Semicolons (Optional, Rarely Used)
# Semicolons are optional in Python. 
# You can write multiple statements on one line by separating them with ; but this is rarely used because it makes it hard to read:

print("Hello"); print("How are you?"); print("Bye bye!")


# Print Without a New Line
# By default, the print() function ends with a new line.

# If you want to print multiple words on the same line, you can use the end parameter:

print("Hello", end="")
print("world")


# Casting
# If you want to specify the data type of a variable, this can be done with casting.

x = str(3)
y = int (3)
z = float(3)

# x = str(3)    # x will be '3'
# y = int(3)    # y will be 3
# z = float(3)  # z will be 3.0

# Case-Sensitive
# Variable names are case-sensitive.


# Multi Words Variable Names
# Variable names with more than one word can be difficult to read.

# There are several techniques you can use to make them more readable:

# Camel Case
# Each word, except the first, starts with a capital letter:

# myVariableName = "John"

# Pascal Case
# Each word starts with a capital letter:

# MyVariableName = "John"
# Snake Case
# Each word is separated by an underscore character:

# my_variable_name = "John"

#-----------------------------------------------

# Unpack a Collection
# If you have a collection of values in a list, tuple etc. Python allows you to extract the values into variables. This is called unpacking.

# Example
# Unpack a list:

fruits = ["apple", "banana", "cherry"]
x, y, z = fruits
print(x)
print(y)
print(z)
print(x,y,z)

# In the print() function, when you try to combine a string and a number with the + operator, Python will give you an error:

# Example
# x = 5
# y = "John"
# print(x + y) - this will raise an error because you cant combine a string and a number with the + operator


x = 5
y = "John"
print(x, y) # this will not raise an error because you can combine a string and number


