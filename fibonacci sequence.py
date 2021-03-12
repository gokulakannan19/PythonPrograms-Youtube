print("Python program to print fibonacci sequence")
#    a  b  c
# a  b  c
# 0, 1, 1, 2, 3, 5, 8.....

a = 0
b = 1

number = int(input("Enter a number: "))

if number == 1:
    print(a)
elif number == 2:
    print(a)
    print(b)
elif number <= 0:
    print("Enter a valid number")
else:
    for i in range(2, number):
        c = a + b
        print(c)
        a = b
        b = c
