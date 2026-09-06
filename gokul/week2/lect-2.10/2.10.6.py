# find the difference between

import math

print(math.pow(10,0.5))
print(10**0.5)

# why to use math.pow and 10**0.5
#  is there any difference in speed between pow and 10**0.5
# check this out : https://stackoverflow.com/questions/20969773/exponentials-in-python-xy-vs-math-powx-y

# 
# Feature	      math.pow(x, y)     	          x ** y
# Return type	   Always a float	            Can be int or float depending on input
# Flexibility	   Only works with numbers    	Works with numbers, complex numbers, and even custom objects
# Speed	           Slightly slower            	Faster (built-in operator)
# Error handling   Converts inputs to float   	Keeps integers exact when possible