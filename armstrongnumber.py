
print("python program to print armstrong number")

for i in range(1, 1001):
    number = i
    sum = 0
    no_of_digits = len(str(i))

    while(i != 0):
        digit = i % 10
        sum = sum + (digit**no_of_digits)
        i = i//10
    if sum == number:
        print(number)