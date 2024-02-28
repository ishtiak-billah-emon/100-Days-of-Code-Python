import random

nameList = ["Akid", "Emon", "Faisal", "Rafsan", "Shajid"]

people = len(nameList)

pickNumber = random.randint(0, people - 1)

person = nameList[pickNumber]
# person = random.choice(nameList) # builtin to choose from list

#print(f"{person} is going to pay for everyone") 
print(person + " is going to buy the meal today!")

