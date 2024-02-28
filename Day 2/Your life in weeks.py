age = int(input("Enter your age: "))

years_remaining = 90 - age
days_left = years_remaining * 365
weeks_left = years_remaining * 52
months_left = years_remaining * 12

print(f"You have {days_left} days, {weeks_left} weeks, {months_left} months left.")