# Final Project
# Yeghiazar Hovhannisyan
# Code in Place
# Stanford
import random
import string
import csv
from hangman_visual import lives_visual_dict


def get_valid_word():
    with open('words.csv') as csvfile:
        spamreader = csv.reader(csvfile, delimiter=',')
        words = []

        for row in spamreader:
             words.append(row)

    wordsi = random.choice(words)
    word = random.choice(wordsi)

    while '-' in word or ' ' in word or '.' in word:
        word = random.choice(words[0])

    return word.upper()


def hangman():
    hello_screen()
    word = get_valid_word()
    word_letters = set(word)  # letters in the word
    alphabet = set(string.ascii_uppercase)
    used_letters = set()  # what the user has guessed

    lives = 7

    # getting user input
    while len(word_letters) > 0 and lives > 0:
        # letters used
        # ' '.join(['a', 'b', 'cd']) --> 'a b cd'

        print('You have', lives, 'lives left and you have used these letters: ', ' '.join(used_letters))

        # what current word is (ie W - R D)
        word_list = [letter if letter in used_letters else '-' for letter in word]
        print(lives_visual_dict[lives])
        print('Current word: ', ' '.join(word_list))

        user_letter = input('Guess a letter: ').upper()
        if user_letter in alphabet - used_letters:
            used_letters.add(user_letter)
            if user_letter in word_letters:
                word_letters.remove(user_letter)
                print('')

            else:
                lives = lives - 1  # takes away a life if wrong
                print('\nYour letter,', user_letter, 'is not in the word.')

        elif user_letter in used_letters:
            print('\nYou have already used that letter. Guess another letter.')

        else:
            print('\nThat is not a valid letter.')

    # gets here when len(word_letters) == 0 OR when lives == 0
    if lives == 0:
        print(lives_visual_dict[lives])
        print('You died, sorry. The word was', word)
    else:
        print('YAY! You guessed the word', word, '!!')

def hello_screen():
    print(" ")
    print("-----------------------------------------------------------------------------------------")
    print("Hi, Hangman is waiting for you 🙌")
    print("This game was made by Yeghiazar Hovhannisyan, as final project of Code in Place, Stanford")
    print("-----------------------------------------------------------------------------------------")
    print("Hangman is an old school favorite, a word game where the goal is simply to find the missing word or words.")
    print("You will be presented with a number of blank spaces representing the missing letters you need to find.")
    print("Use the keyboard to guess a letter (I recommend starting with vowels).")
    print("You have only 7 lives).")
    print("-----------------------------------------------------------------------------------------")
    print(" ")
    print("Guess the name of country!")

if __name__ == '__main__':
    hangman()
