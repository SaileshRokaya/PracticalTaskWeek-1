''' 5. Input the values of radius, length and width from a user in a python program and calculate the following:
		a. Area of a circle
		b. Area of a rectangle
		c. Area of a square '''

# Store input numbers
radius = float(input("Enter the value of radius: "))
length = float(input("Enter the value of length: "))
width = float(input("Enter the value of width: "))

#Calcuate area of circle, rectangle and square.
Area_of_circle = 3.14*(radius**2)
Area_of_rectangle = length * width
Area_of_square = length**2

#Output
print("Area of a circle is: ", Area_of_circle)
print("Area of a rectangle is: ", Area_of_rectangle)
print("Area of a square is: ", Area_of_square)

