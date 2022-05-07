

ins = input("Enter your age to calculator: ")

if ins <= 12:
  print("You're a child")
elif ins <= 19:
  print("You're a teenager")
elif ins <= 30:
  print("You're an young adult")
elif ins <= 64:
  print("You're an adult")
elif ins > 65:
  print("You're an old person")
else:
  print("please enter a number!!")