# python program to find the smallest of 3 numbers

number1 = int(input("Enter number1: "))
number2 = int(input("Enter number2: "))
number3 = int(input("Enter number3: "))

small = number1

if number2 < small:
    small = number2
if number3 < small:
    small = number3

print(f'{small} is the smallest number')


