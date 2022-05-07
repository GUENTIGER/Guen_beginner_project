#  “Friday Project: Creatinga Calculator.”
#  Step #1: Ask User for Calculation to Be Performed
from ast import operator
from tokenize import Double


operator = input("Would you like to add/subtract/multiply/divide? ").lower()
print("You chose {}".format(operator))
# step 2: ask for numbers, alert order matters for subtracting and dividing
if operator == "subtract" or operator == "divide":
    print("You choose{}".format(operator))
    print("Please keep in mind that the order matters")
num1 = int(input("Please enter the first number: "))
num2 = int(input("Please enter the second number: "))
print("First number: {}".format(num1))
print("Second number: {}".format(num2))
# step 3: setup try/except for mathematical operation
try:
  #step 3a: immediately try to cover the input convert float
  num1,num2 = float(num1),float(num2)
  #step3b: perfom the math operation
  if operator == "add":
    print("{} + {} = {}".format(num1,num2,num1+num2))
  elif operator == "subtract":
    print("{} - {} = {}".format(num1,num2,num1-num2))
  elif operator == "multiply":
    print("{} * {} = {}".format(num1,num2,num1*num2))
  elif operator == "divide":
    print("{} / {} = {}".format(num1,num2,num1/num2))
  else:
    print("Sorry, But{} is not option".format(operator))
except:
  # steb 3c: print error
 print("Error: Improper numbers used. Please try again.")

  
    