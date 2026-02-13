# list 

# list are mutable

# list are ordered

# list allow duplicate values

# list are indexed

# list are heterogeneous

# list are dynamic

# List items are indexed, the first item has index [0], the second item has index [1] etc.

thislist = ["apple", "banana", "cherry", "apple", "cherry"]
print(thislist)

# len function
print(len(thislist))

list1 = ["apple", "banana", "cherry"]
list2 = [1, 5, 7, 9, 3]
list3 = [True, False, False]

print(list1)
print(list2)
print(list3)

list1 = ["abc", 34, True, 40, "male"]
print(list1)

thislist = list(("apple", "banana", "cherry")) # note the double round-brackets
print(thislist)
# The l
thislist = ["apple", "banana", "cherry"]
print(thislist[1])

thislist = ["apple", "banana", "cherry"]
print(thislist[-1])


thislist = ["apple", "banana", "cherry"]
if "apple" in thislist:
  print("Yes, 'apple' is in the fruits list")


thislist = ["apple", "banana", "cherry"]
thislist[1] = "blackcurrant"
print(thislist)

# The insert() method inserts an item at the specified index:
thislist = ["apple", "banana", "cherry"]
thislist.insert(2, "watermelon")
print(thislist)

# Using the append() method to append an item:

thislist = ["apple", "banana", "cherry"]
thislist.append("orange")
print(thislist)

# To append elements from another list to the current list, use the extend() method.

thislist = ["apple", "banana", "cherry"]
tropical = ["mango", "pineapple", "papaya"]
thislist.extend(tropical)
print(thislist)


thislist = ["apple", "banana", "cherry"]
thislist.remove("banana")
print(thislist)

# The pop() method removes the specified index.
thislist = ["apple", "banana", "cherry"]
thislist.pop(1)
print(thislist)

# Delete the entire list:

thislist = ["apple", "banana", "cherry"]
del thislist

# The clear() method empties the list.

# The list still remains, but it has no content.

# Example
# Clear the list content:

thislist = ["apple", "banana", "cherry"]
thislist.clear()
print(thislist)

fruits = ["apple", "banana", "cherry", "kiwi", "mango"]
newlist = []

for x in fruits:
  if "a" in x:
    newlist.append(x)

print(newlist)

thislist = ["orange", "mango", "kiwi", "pineapple", "banana"]
thislist.sort()
print(thislist)

thislist = ["orange", "mango", "kiwi", "pineapple", "banana"]
thislist.sort(reverse = True)
print(thislist)

thislist = ["apple", "banana", "cherry"]
mylist = thislist.copy()
print(mylist)
print(thislist)