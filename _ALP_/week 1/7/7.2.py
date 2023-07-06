'''
In the modify tasks, you are given some starter code. Use the instructions below to make changes to the code. Comment your changes to explain what you have done.

Run the program to see how it works.
Adapt the code to:

1. Get user input into the number variable.
2. Change the print statement so it outputs 'number' multiplied by 'counter' equals 'product'
3. Make the counter increase by 2 every loop
4. Add a line once the loop has finished to output 'The loop has finished' '''

number = int(input("give me a number"))
counter = 1
while counter < 13:
  product = number * counter 
  print(str(counter) + " multiplied by " +str(number) + " equals " + str(product))
  counter = counter + 1

print("the loop has finished")