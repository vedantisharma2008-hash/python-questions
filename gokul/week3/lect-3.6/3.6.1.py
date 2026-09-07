# take a number as input and find the sum of numbers from 1 to that number
n=int(input())
total_sum=0 
for i in range(1,n+1):
    total_sum+=i
print(f"The sum of numbers from 1 to {n} is {total_sum}")

i=1
count=1
while i<=10:
    print("sum of 1 to",i,"is",count)
    i+=1
    count+=i