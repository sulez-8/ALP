'''
Task - Investigate
Use comments to answer the investigate questions on the example code.

'''
# Example Code

number = 5
print("I have thought of a number between 1 and 10")
guess = int(input("Can you guess what it is?"))

if guess == number:
  print("Correct!")
if guess < number:
  print("Too Low!")
if guess > number:
  print("Too High!")

# What happens if you input the guess '2'?
  # Answer 2 is lower than 5 so you will get the 15th line output

# What happens if you input the guess '6'?
  # Answer 6 is bigger than 5 so you will get the 17th line output

# What happens if you input the guess '5'?
  # Answer 5 is equal to 5 so you will get the 13th line output

# What happens if you input the guess '-5'?
  # Answer -5 is lower than 5 so you will get the 15th line output

# What happens if you input the guess '0'?
  # Answer 0 is lower than 5 so you will get the 15th line output

# What do the symbols '<' and '>' mean on lines 9 and 11?
  # Answer > means bigger than and < means less than

# What happens if you change line 5 to if guess = number: ?
  # Answer it would not work because the variable line is at line 8

# What do you notice about each line that FOLLOWS each IF statement?
  # Answer a print line


