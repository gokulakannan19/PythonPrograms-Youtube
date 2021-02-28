

number1 = input("Enter first number: ")
number2 = input("Enter second number: ")

number1 = int(number1)
number2 = int(number2)

# for multiplication
product = number1 * number2

# to calculate the quotient we use '/' operator
# to calculate the quotient without decimal value we use '//' operator
# to calculate the remainder we use '%' operator

quotient = number1 / number2

remainder = number1 % number2

print(f'{number1} * {number2} = {product}')
print(f'{number1} / {number2} = {quotient}')
print(f'{number1} % {number2} = {remainder}')

# let's check