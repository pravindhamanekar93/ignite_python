s="python is very popular"

# 1.upper()
print(s.upper())
print(s.lower())

# capitalise - means first letter will be capital
print(s.capitalize())
print(s.title())

# swapcase - means swap the .casefold()
s1="PyThOn"
print(s1.swapcase())

# find means find the index of the string
print(s.find("is"))

# index means find the index of the string if not found the return -1 or gives an error
print(s.index("is"))
print("python" in s)


# startwith means check the string is starting with the given string or not
print(s.startswith("python"))
print(s.endswith("popular"))

# isalpa means check the string is alpha or not means only letters 
print(s.isalpha())

# print s.isdigit()
# s.isupper()
# s.islower()

# strip means remove the leading and trailing spaces from the string
s2=" python is unique    "
print(s2.strip())
print(s2.lstrip()) # remove left spaces
print(s2.rstrip()) # remove right spaces



s3 = "I like Java"
print(s3.replace("Java", "Python"))

# split means split the string into list
print(s3.split())


# join means join the list into string
s4= ["i","like","python"]
print(" ".join(s4))

print(s3.count("a"))

# center means center the string
print(s3.center(20))

# formating string
# format() means formating the string 
print("my name is {}".format("pravin"))


#f-string means formating the string using f-string 
name='pravin'

print(f"my name is {name}")

# encode() means ecode the string
# print(s.encode())
# print(s.decode())

print("I-love-Python".partition("-"))


# s="python is very popular"
# slicing
print(s[2:5])
print(s[:5]) # slice from the start to end
print(s[0:]) # slice from end to start
print(s[-5:-2]) # slice from end to start

a="hello"
b="world"
print(a+b)
print(a*3 +" ")


# F-Strings
# F-String was introduced in Python 3.6, and is now the preferred way of formatting strings.

# To specify a string as an f-string, simply put an f in front of the string literal, and add curly brackets {} as placeholders for variables and other operations.

# age = 36
# #This will produce an error:
# txt = "My name is John, I am " + age
# print(txt) - this will give error

age = 21
print(f"my age is {age}")

print(f"my age is {age*2}")

txt = f"The price is {20 * 59} dollars"
print(txt)


# escape characters
# \' means single qoute
txt = 'It\'s alright.'
print(txt) 
# output - It's alright.

# The escape character allows you to use double quotes when you normally would not be allowed:
txt = "we are learning \"python\""
print(txt) #we are learning "python"

# String methods
# 1.zfill() means fill the strinsg with zeros at the beginningg at the number or string
print("500".zfill(5)) # 00500

# 2.ljust means left justify the string
print("python".ljust(10,'*')) #output - python****



