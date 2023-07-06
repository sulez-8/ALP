# Example code 1

number = 7
print("I have thought of a number between 1 and 10")
guess = int(input("Can you guess what it is?"))
#random number and takes user input 
if guess == number:
  print("Correct!")
elif guess < number:
  print("Too Low!")
else:
  print("Too High!")
#uses if elif and else statments to check the users inout with the three possibilty
# Example code 2

number1 = int(input("Please enter a number"))
number2 = int(input("Please enter another number"))
#asks the user for 2 numbers
if number1 > number2:
  print("Number 1 is bigger than number 2")
elif number2 > number1: 
  print("Number 2 is bigger than number 1")
else:
  print("Both numbers are the same")

#checks which number is bigger or if theyre equal by using if elif and else 