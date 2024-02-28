print("Welcome to rollercoaster ride.")
height = int(input("Enter your height in CM "))

if height > 120:
  age = int(input("What is your age "))
  if age >= 18:
    print("You can ride the rollercoaster!")
  else:
    print("Sorry, you can not ride the rollercoaster.")
else:
  print("Sorry, you can not ride the rollercoaster.")