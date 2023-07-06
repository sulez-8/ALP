'''
Reference Link
https://docs.google.com/document/d/1Lf221krWqB0vv5zSaQDvzBi6you6AuKdfn5x1TETh7Q/edit?usp=sharing
'''
'''
## Task Instructions - Beat The Zombie

This task requires you to combine lots of skills from earlier lessons. Don't be afraid to look at your old code, google ideas and have fun with the dialogue.  Good luck!

Write a program that simulates an encounter with a zombie in an RPG

1- Create a list of possible weapons.
2- In a variable called ‘zombieWeakness’ store the name of one of the weapons from the list.
3- Output messages telling the user that they have encountered a zombie and should prepare to fight.
4- Output the list of weapons to the user.  Ask if they want to type 1 to use one from the list or 2 to pick their own.  
  4.1- If they type 1 then they should input the weapon name - store it to a new variable. 
  4.2- If they type 2 they should input the weapon name - add it to the list and save it to a new variable.
5- If the weapon picked matches the zombieWeakness, output a message telling the user that they have won the fight.  
  5.1- Otherwise output a message saying that they have lost.

'''
weapons = ["AR", "SMG", "pistol", "knive" ]
zombieweakness = weapons[1]
print("you have incountered a zombie! get ready to fight")
choice = int(input(str(weapons) + " type 1 to choose a weapon from this list or type 2 to choose a weapon of your choice: "))
if choice == 1:
  weapon1 = int(input("please choose a weapon from the list: " ))
if choice == 2:
  weapon2 = input("add your weapons name: " )
  weapons.append(weapon2)

if weapon1 == 1:
  print("you have won the fight")
else:
  print("you lost")
