# A dictionary example:

programming_dictionary = {
  "Bug": "An error in a program that prevents the program from running as expected.",
  "Loop" : "Doing something over and over"
  }

# Creating Empty dictionary
empty_dictionary = {} 

# adding new items:
programming_dictionary["Function"]  = "A piece of code that you can easily call over and over again."

# Retrive data from dictionary
#print(programming_dictionary["Loop"])

# Edit an item in dictionary
programming_dictionary["Bug"] = "Changed the value of bug"

# wipe-out data from dictionary
#programming_dictionary = {}


# Loop through a dictionary
for thing in programming_dictionary:
  print(thing) # returns the keys
  print(programming_dictionary[thing]) # use the key to retrive the value

#print(programming_dictionary)