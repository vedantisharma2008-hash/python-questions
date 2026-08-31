# predict the output

x="10.5"
a="21"
b=int(a)
y=int(x)
print(a)
print(type(x))
print(type(y))

# a = "21" → still a string.

# b = int(a) → works fine, because "21" is a whole number string.

# y = int(x) → error here! "10.5" cannot be directly converted to an integer, since it has a decimal point. Python raises a ValueError.