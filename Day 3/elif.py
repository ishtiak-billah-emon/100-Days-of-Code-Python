print("Welcome to rollercoaster ride.")
height = int(input("Enter your height in CM "))

if height > 120:
  age = int(input("What is your age "))
  if age <= 12:
    print("You have to pay $5")
  elif age > 12 and age <= 18 :
    print("You have to pay $7")
  else:
    print("You have to pay $12")
else:
  print("Sorry, you can not ride the rollercoaster.")