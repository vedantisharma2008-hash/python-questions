# find the factorial of a number using while loop, take number n as input
n=int(input("Enter number here:"))
factorial=1
i=1
while i<=n:
    factorial*=i
    i+=1
print(factorial)