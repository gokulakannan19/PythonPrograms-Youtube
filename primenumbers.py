print("Python program to print prime numbers")

start_limit = int(input("Enter the start limit: "))
end_limit = int(input("Enter the end limit: "))

for number in range(start_limit, end_limit+1):
    # 1, 2, 3,4
    if number > 1:
        count = 0
        for i in range(2, number):
            if (number % i) == 0:
                count = count+1
        if count == 0:
            print(number)



