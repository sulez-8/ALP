'''
In these tasks you will be given one or more examples of code.

- Look at each example , study it carefully.
- Write a prediction of what it will do when it runs. Your prediction should be added to the code as comments. You should use the key terms list, item and index in your predictions.
- Run the code, compare what happens to your prediction.
- Add comments to note down and differences between your prediction and what actually happened.

'''

# Example Code 1

Sentence = ["Always", "look", "on", "the", "bright", "side", "of",]
#assigned a variable 
print(Sentence)
#prints the variable above 
print(Sentence[1])
#prints the second part of the variable 
Sentence.append("life")
#this will add a new part to the variable 
Sentence[4] = "sunny"
#this wil replace the 5th part of the variable
print(Sentence[4])
#this will print the now replaced 5th part of the variable
print(Sentence[0] + " " + Sentence[3])
#this will print the 1st and 4th part of the variable
print(Sentence)
#this will print the whole variable