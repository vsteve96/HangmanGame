# Hangman Game

## Overview

Welcome to the Hangman Game! This project implements the classic Hangman word guessing game in Python. The game challenges players to guess a secret word by suggesting letters or guessing the entire word. Incorrect guesses lead to the gradual drawing of a hangman, and players must solve the word before running out of attempts.

## Features

- **Random Word Selection:** The game selects a random word from a predefined list, ensuring variety and unpredictability.

- **Difficulty Levels:** Players can choose from three difficulty levels, each with a different number of allowed incorrect guesses.

- **User-Friendly Interface:** The game provides a clear and user-friendly interface, prompting players for input and displaying the current game state.

- **Instructions:** Players have the option to view instructions at the beginning of the game, explaining the rules and objectives.

## How to Play

1. Run the script.
2. Choose whether to view instructions.
3. Decide whether to continue to the game.
4. Guess letters or the entire word to reveal the secret word.
5. Be cautious with incorrect guesses, as they lead to the drawing of the hangman.
6. Win by correctly guessing the word or lose by running out of attempts.

## Getting Started

Clone the repository to your local machine and run the script using a Python interpreter. Ensure you have the required dependencies, including the `hangman_parts` module for displaying the hangman.

# Development Process

**Input Validations**

Ensuring a smooth and error-free user experience was a crucial aspect of the Hangman game development. The input validation process has been carefully implemented to handle various scenarios and provide helpful feedback to the player.

**Single Letter Guesses**

Players are prompted to enter a letter when making single letter guesses. The input validation for single letter guesses covers the following:

- **Non-Empty Input:** The program checks whether the user has entered a letter, and the input must not be empty.

- **Alphabetic Characters:** The input must consist of alphabetic characters only.

- **Single Character Length:** The length of the input should be exactly one character.

**Whole Word Guesses**

For whole word guesses, where the player attempts to guess the entire word, the input validation includes:

- **Non-Empty Input:** Similar to single letter guesses, the input must not be empty.

- **Alphabetic Characters:** The input must consist of alphabetic characters only.

- **Length Check:** The length of the input can be greater than one, but it should still be a valid word.

**User Feedback**

In case of invalid input, players receive informative error messages guiding them on the correct input format. This ensures that players understand why their input was rejected and encourages them to provide valid input.

```python
def get_guess():
    while True:
        guess = input("Enter a letter or the whole word: ").lower()
        if guess and ((guess.isalpha() and len(guess) == 1) or (len(guess) > 1 and guess.isalpha())):
            return guess
        else:
            print("Invalid input. Please enter a single letter or the whole word.")
```

**Single Letter Guesses**
Players are prompted to enter a letter when making single letter guesses. The input validation for single letter guesses covers the following:

Non-Empty Input: The program checks whether the user has entered a letter, and the input must not be empty.

Alphabetic Characters: The code ensures that the input must consist of alphabetic characters only.

Single Character Length: The length of the input should be exactly one character, to ensure the single character guesses are being handled correctly.

**Whole Word Guesses**
For whole word guesses, where the player attempts to guess the entire word, the input validation includes:

Non-Empty Input: Similar to single letter guesses, the input must not be empty.

Alphabetic Characters: The input must consist of alphabetic characters only.

Length Check: The length of the input can be greater than one, but it should still be a valid word.

**User Feedback**
In case of invalid input, players receive informative error messages guiding them on the correct input format. This ensures that players understand why their input was rejected and encourages them to provide valid input.

By implementing robust input validations, the development process aims to enhance user experience, prevent unintended errors, and make the Hangman game more enjoyable for players of all skill levels.