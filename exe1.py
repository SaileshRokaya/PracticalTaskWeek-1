'''1. Create a python program with below mentioned specification.

	- Input the name of the user
	- Input 2 numbers from the user
	- Calculate the following: Addition, Substraction, Multiplication, Division, Factorial
	- Print the output by greeting Hello to the user followed by the results of calculation.
	
	Output Sample:
	
	Hello Deepak, Please find below your calculations.
	Addition: 
	Substraction:
	Multiplication:
	Division:
	Factorial:
	
	Bye, see you next time '''

import math #importing math class

# Taking values from the user
print("Enter your name: ")
name = input()

# Store input numbers
a = input('Enter first number: ')
b = input('Enter second number: ')

# Operation
add = float(a) + float(b)
sub = float(a) - float(b)
mul = float(a) * float(b)
div = float(a) / float(b)

# Display output
print("Hello ", name, ",Please find below your calculations.")
print("Addition: ", add)
print("Substraction: ", sub)
print("Multiplication: ", mul)
print("Division: ", div)
print("Factorial: ", math.factorial(int(a)))
print("Bye, see you next time")
