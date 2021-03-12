print("Python program to print prime numbers")

start_limit = int(input("Enter start limit: "))
end_limit = int(input("Enter start limit: "))

for number in range(start_limit, end_limit+1):
    #7
    if number > 1:
        count = 0
        for i in range(2, number):
            if number % i == 0:
                count = count + 1 #0 + 1
        if count == 0:
            print(number)



