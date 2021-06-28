'''3. Write a python program to swap the values of 3 variables.'''

# Taking values from the user
x = input("Enter first number: ")
y = input("Enter second number: ")
z = input("Enter third number: ")

# Display the values
print('The value of x is: ', int(x))
print('The value of y is: ', int(y))
print('The value of z is: ', int(z))

# swapping the values
temp_var = x
x = y
y = z
z = temp_var
print('The value of x after swapping is: ', x)
print('The value of y after swapping is: ', y)
print('The value of z after swapping is: ', z)
