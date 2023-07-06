def add(num1, num2):
  return num1+num2
def subtract(num1, num2):
  return num1-num2  
def multiply(num1, num2):
  return num1*num2
def divide(num1, num2):
  return num1/num2  

num1 = int(input("Give me a number "))
num2 = int(input("give me another number "))

print("1, add")
print("2. subtract")
print("3. multiply")
print("4. divide")

user= input("choose the number of the operation ")
if user == "1":
  answer=add(num1, num2)
  print(answer)
elif user == "2":
  answer = subtract(num1, num2)
  print(answer)
elif user == "3":
   answer =multiply(num1, num2)
   print(answer)
elif user == "4":
  answer = divide(num1, num2)
  print(answer)
else:
  print("error")