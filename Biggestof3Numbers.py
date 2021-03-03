# python program to find the biggest of 3 numbers

number1 = int(input("Enter number1: "))
number2 = int(input("Enter number2: "))
number3 = int(input("Enter number3: "))

big = number1

if number2 > big:
    big = number2
if number3 > big:
    big = number3

print(f'{big} is the biggest number')


