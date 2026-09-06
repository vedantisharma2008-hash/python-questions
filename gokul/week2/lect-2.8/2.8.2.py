# take year of birth (YOB) as input,
# print the current age of the person and also print if the person is eligible to vote or not


# HINT : subtract current year from YOB
yob=int(input("Enter year of birth"))
a=2026-(yob)
print(a)
if a>=18:
    print("You are eligible to vote")
else:
    print("You are not eligible to vote")