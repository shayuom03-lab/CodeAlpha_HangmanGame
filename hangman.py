
import random

# Predefined list of 5 words
words = ["python", "computer", "apple", "coding", "program"]

# Select a random word
secret_word = random.choice(words)

# Game variables
guessed_letters = []
incorrect_guesses = 0
max_attempts = 6

print("================================")
print("       WELCOME TO HANGMAN")
print("================================")
print("Guess the hidden word one letter at a time!")
print("You have 6 incorrect attempts.")

# Main game loop
while incorrect_guesses < max_attempts:

    # Display current word progress
    display_word = ""

    for letter in secret_word:
        if letter in guessed_letters:
            display_word += letter + " "
        else:
            display_word += "_ "

    print("\nWord:", display_word)
    print("Incorrect guesses:", incorrect_guesses, "/", max_attempts)

    # Check if player has guessed the word
    if all(letter in guessed_letters for letter in secret_word):
        print("\nCongratulations! You won!")
        print("The correct word was:", secret_word)
        break

    # Take user input
    guess = input("Enter a letter: ").lower().strip()

    # Validate input
    if len(guess) != 1 or not guess.isalpha():
        print("Please enter a single valid letter.")
        continue

    # Check duplicate guesses
    if guess in guessed_letters:
        print("You have already guessed this letter!")
        continue

    guessed_letters.append(guess)

    # Check the guessed letter
    if guess in secret_word:
        print("Correct guess!")
    else:
        incorrect_guesses += 1
        print("Wrong guess!")

# Check losing condition
if incorrect_guesses == max_attempts:
    print("\nGame Over! You lost.")
    print("The correct word was:", secret_word)

print("\nThanks for playing Hangman!")