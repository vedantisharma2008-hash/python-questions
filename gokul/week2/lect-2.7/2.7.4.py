
# write a python script for the below test case,
# Note the input will be of 5 characters long,


# testcase 1
'''
INPUT : 'gokul'
OUTPUT : 'hplvm'
'''

# testcase 2
'''
INPUT: 'abcde'
OUTPUT: 'bcdef'
'''

# solution:
x=input()
result=""
for ch in x:
    result+=chr(ord(ch)+1)
print(result)