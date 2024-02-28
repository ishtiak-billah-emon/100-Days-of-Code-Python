import random

rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)

'''
scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)

'''
game_image = [rock, paper, scissors]

gameOn = True
while gameOn == True:
  userInput = int(input("What do you want to Choose ? --> Type 0 for Rock, 1 for Paper, 2 for Scissors. "))
  pc = random.randint(0,2)

  if userInput > 2 or userInput < 0:
    print("Invalid input")
  elif userInput == 0 and pc == 2:
    print(f"You won. \nComputer played  {scissors} \nYou played  {rock}")
  elif userInput == 1 and pc == 0:
    print(f"You won. \nComputer played  {rock} \nYou played  {paper}")
  elif userInput == 2 and pc == 1:
    print(f"You won. \nComputer played  {paper} \nYou played  {scissors}")
  elif userInput == pc:
    print(f"Draw. \nComputer played  {game_image[pc]} \nYou played  {game_image[userInput]}")
  else:
    print(f"You lose. \nComputer played  {game_image[pc]} \nYou played  {game_image[userInput]}")
  
  
  ch = str(input("Do you want to play another game ? type 'y' for Yes and 'n' for No "))
  if ch == "n":
    gameOn = False
  else:
    print('Lets play mate.')
