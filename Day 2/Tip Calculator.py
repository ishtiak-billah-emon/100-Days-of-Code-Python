print("Welcome to the tip calculator.")
bill = float(input("What was the total bill? $"))
tip_percentage = int(input("What percentage tip would you like to give? 10, 12 or 15? "))
split = int(input("How many people to split the bill? "))

total_bill = bill + (bill * (tip_percentage / 100))
bills_of_each = round(total_bill / split, 2)
print("Each person should pay: $", bills_of_each)