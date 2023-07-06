# Starter Code

number = 5
print("I have thought of a number between 1 and 10")
guess = int(input("Can you guess what it is? "))
#chooses a random number and takes user input

if guess < number:
  print("Too Low!")
if guess > number:
  print("Too High!")
if guess == number:
  print("correct!")
#checks the user input with the three possible outcomes above
