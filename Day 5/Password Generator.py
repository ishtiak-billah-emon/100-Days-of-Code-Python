import string
import random

# Generate a list containing all lowercase and uppercase alphabets

lowercase_alphabets = list(string.ascii_lowercase)
uppercase_alphabets = list(string.ascii_uppercase)
all_alphabets = lowercase_alphabets + uppercase_alphabets

symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

password = ''

print('Welcome to the PyPassword Generator!')

num_letter = int(input('How many letters would you like in your password? '))

symbol = int(input('How many symbols would you like in your password? '))

number = int(input('How many numbers would you like in your password? '))

for i in range (1, num_letter + 1):
  password += all_alphabets[random.randint(0, 51)]


symbols_length = len(symbols)

for i in range (1, symbol + 1):
  password += symbols[random.randint(0, symbols_length - 1)]

numbers = list(range(10))
for i in range (1, number + 1):
  password += str(numbers[random.randint(0, len(numbers) - 1)])



characters = list(original_string)

random.shuffle(characters)

shuffled_string = ''.join(characters)

print(password)