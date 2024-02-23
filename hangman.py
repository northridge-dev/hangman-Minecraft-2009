# BANNER and HANGMAN_PICS are some ASCII art
# Create your own ASCII art if you desire, but
# ONLY AFTER getting the game logic working.
from ascii_art import BANNER, HANGMAN_PICS
from word_lists import impossible, easy, medium, hard, ai_settings
from os import system
import random

def clear():
  system("clear")
clear()
# uncomment the import statement, below, when
# you're ready to implement a one player version
# of the game.
# `animal_words` is a list of . . . animal words.
# Feel free to add more words or word categories.
# from word_lists import animal_words

"""
Here's where you'll write your code. 
  - Follow the instructions in the README file.
  - If you try to write all the code in `play_hangman`, 
    it's going to be a mess. Instead, break your logic
    into smaller functions that you can call from 
    `play_hangman`.

Run your code from the terminal:
  - make sure you're in the right directory (`projects/hangman`)
    - if you're not sure how to get to the right directory, ask!
  - make sure you're at the command line prompt, not in the Python shell (not >>>)
  - type the following command: python hangman.py

Tests? No tests for this project. 
"""


# Here's where you can define helper functions
def get_word(ai = False, word_choice = False):
  # This gets the word from either the player or the hangman AI
  if not ai:
    return input("word?")
  elif ai:
    if word_choice == "easy":
      return random.choice(easy)
    if word_choice == "medium":
      return random.choice(medium)
    if word_choice == "hard":
      return random.choice(hard)
    if word_choice == "impossible":
      return random.choice(impossible)
def get_guess(guessed ,ai=False):
  # This gets the guess from the second player or the potential AI
  if not ai:
    good_guess = False
    while not good_guess:
      guess = input("What is your guess? (1 letter)")
      if guess == "~":
        return "~"
      if guess not in guessed:
        return guess
def win(answer, current):
  # check if the player's guesses are the word
  if answer == current:
    return True
  return False
def print_gallows(lives):
  # This is to get the proper ascii art for the gallows
  print(HANGMAN_PICS[lives])
def is_dead(lives):
  # check if the player is dead
  if lives <= 0:
    return True
  return False

# `play_hangman` is the main function, the function
# that will orchestrate all the helper functions
# you define, above.
def play_hangman():
    # Get secret word and listify
    got_is_ai = False
    while not got_is_ai:
      is_ai = input("singleplayer?? y/n: ")
      if is_ai == "y":
        got_difficulty = False
        while not got_difficulty:
          difficulty_set = input("difficulty? easy, medium, hard, or impossible: ")
          if difficulty_set in ai_settings:
            got_difficulty = True
          print("Spell correctly you idiot")
        secret_word = (get_word(True, difficulty_set)).lower()
        got_is_ai = True
      if is_ai == "n":
        secret_word = (get_word()).lower()
        got_is_ai = True
      else:
        print('please do not be the gay retard you are and just say "y" or "n".')
    sw_list = []
    # make displayed list
    disp_word = []
    # whether the word is guessed or lives run out
    guessed = False
    lives = 6
    # Make the lists with proper length
    for l in secret_word:
      sw_list.append(l)
      disp_word.append("_")
    clear()
    # print(sw_list) # Test
    # list of guessed letters
    guessed_letters = []
    # repeat until the word is guessed
    while not guessed:
      print(disp_word)
      print("you already guessed", guessed_letters)
      guess = (get_guess(guessed_letters)).lower()
      if guess == "~":
        clear()
        print("You Win!!!")
        print("""
\      /\      /  
 \    /  \    /
  \  /    \  /
   \/      \/
""")
        print(sw_list)
        return "Success"
      clear()
      # Check to see if the guess is correct
      got_letter = False
      indexed = 0
      for g in sw_list:
        # print(g)
        if guess == g:
          # add the guess to the list of guessssed 
          guessed_letters.append(guess)
          g_pos = indexed
          # print(g_pos)
          disp_word[g_pos] = guess
          got_letter = True
        indexed +=1
      
      if not got_letter:
        lives -= 1
        print(f"only {lives} lives left")
        guessed_letters.append(guess)
        if is_dead(lives):
          print("You have died. haha loser")
          print(""" 
|
|
|
|_____
""")
          break
      # Check if the word was guessed
      print_gallows(lives)
      if win(sw_list, disp_word):
        clear()
        print("You Win!!!")
        print("""
\      /\      /  
 \    /  \    /
  \  /    \  /
   \/      \/
""")
        print(disp_word)
        return "Success"
      
while True:     
  print(BANNER)
  play_hangman()

# """
# Don't worry about the code below, and don't change it.

# It's just a way to trigger the `play_hangman` function
# when you run this file from the command line.
# """
# if __name__ == "__main__":
#     play_hangman()
