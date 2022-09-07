word_list = ["ardvark","baboon","camel"]
import random

stages = ['''
  +---+
  |   |
  0   |
 /|\  |
 / \  |
      |
=========
      ''','''
 +---+
  |   |
  0   |
 /|\  |
 /    |
      |
=========
      ''','''
 +---+
  |   |
  0   |
 /|\  |
      |
      |
=========
      ''','''
 +---+
  |   |
  0   |
 /|   |
      |
      |
=========
      ''','''
 +---+
  |   |
  0   |
 /    |
      |
      |
=========
      ''','''
 +---+
  |   |
  0   |
      |
      |
      |
=========
      ''','''
 +---+
  |   |
      |
      |
      |
      |
=========
''']
chosen_word = random.choice(word_list)

print(f'Pssst, the solution is {chosen_word}.')

word_length = len(chosen_word)
display = []
for letter in chosen_word:
    display += "_"
print(display)

lives = 6
end_of_game = False
while not end_of_game:
    
    guess = input("Guess a letter: ").lower()
    for position in range(word_length):
        letter = chosen_word[position]
        if letter == guess:
            display[position] = letter

    if guess not in chosen_word:
        lives -= 1
        if lives == 0:
            end_of_game = True
            print("You lose.")
    print(display)

    if "_" not in display:
        end_of_game = True
        print("You win")
    print(stages[lives])
