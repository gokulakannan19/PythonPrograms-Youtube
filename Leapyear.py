
print("Program to find whether the given year is leap year or not")

year = int(input("Enter a year: "))

if year % 4 == 0:
    print(f'{year} is a leap year')
else:
    print(f'{year} is not a leap year')
