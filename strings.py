string = "This is a sample string for learning string operations." 
string2 = "It is so easy to learn string operations."

# concatenation
print(string + " " + string2)

# repetition
# print(string * 3)

# checking length of a string
print(len(string))
print(string2)

# other string methods
string3 = "Hello"
print(string3.upper())
print(string3.title())

print(string3.replace("Hello", "Hi"))
print(string3.strip())

# substrings
string4 = "Email messages can be very informative."
print("email" in string4)
print("home" not in string4)