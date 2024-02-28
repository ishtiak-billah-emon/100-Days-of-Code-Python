import math

def prime_checker(number):
  is_prime = True
  for i in range (2 , int(math.sqrt(number) + 1)):
    if number % i == 0:
      is_prime = False
      break
  
  if is_prime == True:
    print("It's a prime number.")
  else:
    print("It's not a prime number.")


n = int(input("Enter a number: "))
prime_checker(number = n)