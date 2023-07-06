'''
Task - Which Room?
----------------------

Write a program that asks the user for their name and which subject they are studying.
The program should output a message telling the student by name which room to go to for that class (make up the room numbers if you need to).  You should include at least 3 subjects and have a message such as 'I don't know which room that class is in' for any you don't include.
 Example - an input of 'Ben' and 'Computing' might get an output of 'Hi Ben, go to room 401 for Computing'


You may use any method taught in class that is appropriate for this task. There is room for interpretation.

'''
#Start coding below
name = input("what is your name? ")
subject = input("What subject are you studying? ")

if subject == "PE":
  print(f"Hello " + name + " go to room 57 for PE")
elif subject  == "Biology":
  print(f"Hello " + name + " go to room 56 for Biology")  
elif subject == "History":
  print(f"Hello " + name + " go to room 58 for History")
else: 
  print("I don't know which room that class is in")