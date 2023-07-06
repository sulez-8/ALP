grade = int(input("what was your grade from 0 to 100? "))

if grade > 100:
  print("the value you entered was too high!")
  
if grade < 0:
  print("the grade you entered was too low!")
  
fail = grade < 40

if fail:
  print("retake required")
else:
  print("you have passed")

if grade < 40:
  print("U grade")
  
if grade <= 68:
  print("C grade")

if grade <= 79:
  print("B grade")

if grade >= 80:
  print("A grade")