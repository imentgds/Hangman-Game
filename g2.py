import nltk
import random
from nltk.corpus import words

nltk.download('words')

def choose_word():
    word_list = words.words()
    return random.choice(word_list).lower()

def display_word(word, guessed_letters):
    displayed_word = ''
    for letter in word:
        if letter in guessed_letters:
            displayed_word += letter + ' '
        else:
            displayed_word += '_ '
    return displayed_word.strip()

def hangman():
    word = choose_word()
    guessed_letters = []
    incorrect_guesses = 0
    max_incorrect_guesses = 6

    print("Welcome to Hangman!")
    print("Guess the word by entering one letter at a time.")
    print("You have {} incorrect guesses before the man is hanged.".format(max_incorrect_guesses))

    while True:
        print("\n" + display_word(word, guessed_letters))

        guess = input("Enter your guess: ").lower()

        if len(guess) != 1 or not guess.isalpha():
            print("Please enter a single letter.")
            continue

        if guess in guessed_letters:
            print("You already guessed that letter.")
            continue

        guessed_letters.append(guess)

        if guess not in word:
            incorrect_guesses += 1
            print("Incorrect guess! You have {} guesses left.".format(max_incorrect_guesses - incorrect_guesses))
            if incorrect_guesses == max_incorrect_guesses:
                print("You've run out of guesses! The word was '{}'.".format(word))
                break
        else:
            print("Correct guess!")

        if all(letter in guessed_letters for letter in word):
            print("Congratulations, you've guessed the word '{}'!".format(word))
            break


hangman()
