# Program to calculate the area of a rectangle

# Get input for height & width. Convert to integers and store in variables

# Calculate the area & store the result in the area variable

# Output the area variable (converted to string)

height = int(input("what is the height of  the rectangle "))

width = int(input("what is the width of the rectangle "))

area = height * width
 
print(str(height) + " multiplied by " + str(width) + " = " + str(area))



'''
Extra Challenges
Perimeter Calc
Create a program that allows the user to enter 2 numbers representing the width and length of a rectangle. The program calculates and displays the perimeter of the rectangle. 
Restaurant Tip Calculator 
Create a program that allows the user to enter the price of a meal at a restaurant. The program calculates the amount of the tip to be paid at 20%. The tip and total price are then displayed separately.
Volume and Surface Calc 
Create a program that allows the user to enter 3 numbers representing the height, width and length of a cuboid. The program calculates and displays the volume and total surface area of the cuboid. 
'''