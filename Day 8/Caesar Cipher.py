alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']


encoded_text = ''
decoded_text = ''
is_end = False

def encrypt(text, shift):
  global encoded_text
  for i in range (0, len(text)):
    encoded_text +=  (chr(ord(text[i]) + shift))
    
  print(f"Here's your encoded message:  {encoded_text}")
    
    
def decrypt(text, shift):
  global decoded_text
  for i in range (0, len(text)):
    decoded_text +=  (chr(ord(text[i]) - shift))
  print(f"Here's your decoded message:  {decoded_text}")

def take_input():
  direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
  text = input("Type your message:\n")
  shift = int(input("Type the shift number: \n"))

  
while is_end == False:
  
  take_input()
  
  if direction == 'encode':
    encrypt(text, shift)
  elif direction == 'decode':
    decrypt(text, shift)
  else:
    print("Invalid text!")
    take_input()
  
  continue_or_not = input("Type 'yes' if you want to go again. Otherwise type 'no':\n")
  if continue_or_not == 'no':
    is_end = True
  elif continue_or_not == 'yes':
    is_end = False
  else:
    print("Invalid Text !")
    is_end = True  
    



