# Example code 1

# Add comments to each line to say whehter it is inside or outside the loop and what it does.

# Explain the circumstances in which the loop will run.

print("What is the capital of France?")
answer = input() 
#asks the user for input 
while answer != "Paris":
  print("Incorrect! Try again.")
  answer = input("What is the capital of France?")

print("Correct!")
#starts a loop with "while" from line 10 to 12
# Example code 2

counter = 1
#counter starts at one 
while counter < 5:
  print("This code is inside the loop")
  counter += 1
  #while the counter is less then 5 it will print the 21st line and add 1 to the counter until it is equal to 5