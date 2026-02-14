# from list_pgms.pgm import thislist


mytuple = ("apple", "banana", "cherry")

print(mytuple)

#  ----------------------------------
# # Tuple
# # Tuples are used to store multiple items in a single variable.

# # Tuple is one of 4 built-in data types in Python used to store collections of data, the other 3 are List, Set, and Dictionary, all with different qualities and usage.

# # A tuple is a collection which is ordered and unchangeable.

# # Tuples are written with round brackets.

# -------------------------------

# Tuple Items
# Tuple items are ordered, unchangeable, and allow duplicate values.

# Tuple items are indexed, the first item has index [0], the second item has index [1] etc.

# Ordered
# When we say that tuples are ordered, it means that the items have a defined order, and that order will not change.

# Unchangeable
# Tuples are unchangeable, meaning that we cannot change, add or remove items after the tuple has been created.

# Allow Duplicates
# Since tuples are indexed, they can have items with the same value:

# --------------------------------------------------

# Check if Item Exists
# To determine if a specified item is present in a tuple use the in keyword:

# Example
# Check if "apple" is present in the tuple:

thistuple = ("apple", "banana", "cherry")
if "apple" in thistuple:
  print("Yes, 'apple' is in the fruits tuple")

# ------------------------------


# Change Tuple Values
# Once a tuple is created, you cannot change its values. Tuples are unchangeable, or immutable as it also is called.

# But there is a workaround. You can convert the tuple into a list, change the list, and convert the list back into a tuple.

# ExampleGet your own Python Server
# Convert the tuple into a list to be able to change it:

x = ("apple", "banana", "cherry")
y = list(x)
y[1] = "kiwi"
x = tuple(y)

print(x)

# ------------------------

# Add Items
# Since tuples are immutable, they do not have a built-in append() method, but there are other ways to add items to a tuple.

# 1. Convert into a list: Just like the workaround for changing a tuple, you can convert it into a list, add your item(s), and convert it back into a tuple.

# Example
# Convert the tuple into a list, add "orange", and convert it back into a tuple:

thistuple = ("apple", "banana", "cherry")
y = list(thistuple)
y.append("orange")
thistuple1 = tuple(y)
print(thistuple1)

# ---------------------------------

# 2. Add tuple to a tuple. You are allowed to add tuples to tuples, so if you want to add one item, (or many), create a new tuple with the item(s), and add it to the existing tuple:

# Example
# Create a new tuple with the value "orange", and add that tuple:

thistuple = ("apple", "banana", "cherry")
y = ("orange",)
thistuple += y

print(thistuple)

# --------------------------

# Remove Items
# Note: You cannot remove items in a tuple.

# Tuples are unchangeable, so you cannot remove items from it, but you can use the same workaround as we used for changing and adding tuple items:

# Example
# Convert the tuple into a list, remove "apple", and convert it back into a tuple:

# thistuple = ("apple", "banana", "cherry")
# y = list(thistuple)
# y.remove("apple")
# thistuple = tuple(y)

# Or you can delete the tuple completely:

# Example
# The del keyword can delete the tuple completely:

# thistuple = ("apple", "banana", "cherry")
# del thistuple
# print(thistuple) #this will raise an error because the tuple no longer exists

# -------------------------------

# But, in Python, we are also allowed to extract the values back into variables. This is called "unpacking":

# Example
# Unpacking a tuple:

fruits = ("apple", "banana", "cherry")

(green, yellow, red) = fruits

print(green)
print(yellow)
print(red)

# --------------------------


# Loop Through the Index Numbers
# You can also loop through the tuple items by referring to their index number.

# Use the range() and len() functions to create a suitable iterable.

# Example
# Print all items by referring to their index number:

thistuple = ("apple", "banana", "cherry")
for i in range(len(thistuple)):
  print(thistuple[i],end=" ")


# ------------------------

# Python Tuple count() Method

# ExampleGet your own Python Server
# Return the number of times the value 5 appears in the tuple:

# thistuple = (1, 3, 7, 8, 7, 5, 4, 6, 8, 5)

x = thistuple.count(5)

print(x)

