s = {1, 2, 3}
s.add(4)
print(s)

# 4️⃣ Remove Element (Safe Way)

s = {1, 2, 3}
s.discard(2)
print(s)


# 6️⃣ Union of Two Sets
a = {1, 2, 3}
b = {3, 4, 5}
print(a | b)

# intersection

print(a&b)

# 8️⃣ Difference
print(a - b)

# 9️⃣ Symmetric Difference
print(a ^ b)

# 🔟 Check Subset
a = {1, 2}
b = {1, 2, 3}
print(a.issubset(b))

# 12️⃣ Find Common Elements in Two Lists
l1 = [1,2,3,4]
l2 = [3,4,5,6]

common = set(l1) & set(l2)
print(common)

# 14️⃣ Check If Two Lists Have Same Elements
l1 = [1,2,3]
l2 = [3,2,1]

print(set(l1) == set(l2))