'''
Chat-Bot Challenge

Lots of websites use chat bots to interact with their customers.  These chat bots are often very sophisticated and use AI to learn and adapt to the user.  Our chat bot is going to be a bit simpler.

The chat bot should work like this:

1.Ask the user their name and store it in a variable.
2. Greet the user by name.
3. Ask the user three(or four) questions about themselves and store their responses in three(or four) different suitably named variables.
4. Respond to each of the questions one by one, using the 5. user’s name in the response.
5. Output a summary of all of the user’s answers in a single sentence.

'''
name = input("Hello there! what is your name? ")
mood = input("Welcome " + name + " how are you feeling today! ")
song = input("Do you want a song to cheer you up " + name + "? " + "What is your favorite song? ")
food = input("Nice choice! want some food to go with the music " + name + "?" + " what do you want to order " )
print("sure thing " + name + " Thank you for chatting with me!" + "here is a summary of the information you gave me ")
print( name + " You were feeling " + mood )
print("you told that your favorite song was " + song)
print("and you also like " + food)