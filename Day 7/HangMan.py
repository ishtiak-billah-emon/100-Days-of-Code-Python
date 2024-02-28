import random
from  HangManArt import logo
from HangManArt import stages

# Make a word list module with more word #TODO 

wordList = ['australia', 'england', 'nepal', 'russia', 'mexico']
chosen_word = random.choice(wordList)
word_length = len(chosen_word)

# Making  blank spaces for the word.  
blank_spaces = []
for i in range (word_length):
  blank_spaces.append("_")
 

# variables 

health =  6
game_Continue = True

def checkWord(ch):
  global health
  global game_Continue
  found = False
  for i in range (word_length):
    if chosen_word[i] == ch:
      blank_spaces[i] = ch
      found = True

      if "_" not in blank_spaces: # checking if matches
        print("Congratulation! You Won !")
        game_Continue = False
   
  if found == False:
    print(f"You guessed {guess_letter}, thats not in the world. You lose a life ")
    health -= 1
    print(stages[health])
    if health == 0:
      print("Game Over")
      game_Continue = False
       
  print(f"{' '.join(blank_spaces)}") # join all the elements in the list and turned it into a string. #NOTE 


#NOTE  Display
print(logo)
while game_Continue == True:
  guess_letter = input("Guess a letter: ").lower()
  if guess_letter in blank_spaces:
    print(f"You've already guessed the letter {guess_letter}")
  else:
    checkWord(guess_letter)
  


