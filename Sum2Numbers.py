# Hi In this tutorial I am going to show you how to add two numbers in Python

# first we want to get input from the user
# In order to get input we will use the input method
# we create two variables to store number1 and number2 respectively
# int method will change the string type to integer type

number1 = int(input("Enter first number: "))
number2 = int(input("Enter second number: "))

# now we add the two numbers using + operator
# lets create another variable sum to store the added value

sum = number1 + number2

# Lets print the result

print(f'{number1} + {number2} = {sum}')

# formatted string is executed during runtime and we can view our results clearly
# lets check the answer