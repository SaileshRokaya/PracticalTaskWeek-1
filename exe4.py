'''4. Python program to implement below mentioned expressions:
    a. Quadratic equation1 -b + sqrroot(b2-4ac)/2a
    b. Quadratic equation2 -b - sqrroot(b2-4ac)/2a'''

# Store input numbers
a = int(input("Enter the value of a: "))
b = int(input("Enter the value of b: "))
c = int(input("Enter the value of c: "))

#process
Quadratic_equation1 = (-b) + (((b**2 - 4*a*c)**0.5)/ (2*a))
Quadratic_equation2 = (-b) - (((b**2 - 4*a*c)**0.5)/ (2*a))

#Output
print("The output of equation1 is: ", Quadratic_equation1)
print("The output of equation2 is: ", Quadratic_equation2)

