name = input("What is your name?\n>")

# name set by input
print("Hello " + name)

# variable overwritten by new value
name = "Joe"

print("Hello " + name)

print("Length of name is: ")
print(len(name))

# how to replace variables
# lets assign values to "a" and "b"
# and then replace then by places

a = input("Provide value for 'a'")
b = input("Provide value for 'b'")

# now we have 2 variables
print("a: " + a)
print("b: " + b)

# lets replace then
temp = a
a = b
b = temp

#######
print("a: " + a)  # this time, to "a" we should have assigned value previously assigned to b
print("b: " + b)  # this time, to "b" we should have assigned value previously assigned to a
