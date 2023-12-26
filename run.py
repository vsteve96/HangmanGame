import random

def choose_word():
    words = ["python", "hangman", "developer", "programming", "coding", "javascript",
    "software", "scripts", "terminal", "ubuntu"]
    return random.choice(words)

def display_word(word, guessed_letters):
    return ''.join(letter if letter in guessed_letters else '_' for letter in word)

def display_hangman(incorrect_guesses, max_incorrect_guesses):
    hangman_parts = [
        [
            "  ____\n |    |\n      |\n      |\n      |\n      |\n______|",
            "  ____\n |    |\n      |\n      |\n      |\n      |\n______|",
            "  ____\n |    |\n O    |\n      |\n      |\n      |\n______|",
            "  ____\n |    |\n O    |\n |    |\n      |\n      |\n______|",
            "  ____\n |    |\n O    |\n/|    |\n      |\n      |\n______|",
            "  ____\n |    |\n O    |\n/|\\   |\n      |\n      |\n______|",
            "  ____\n |    |\n O    |\n/|\\   |\n/     |\n      |\n______|",
            "  ____\n |    |\n O    |\n/|\\   |\n/ \\   |\n      |\n______|",
            "  ____\n |    |\n O    |\n/|\\   |\n/ \\   |\n      |\n______|",
            "  ____\n |    |\n O    |\n/|\\   |\n/ \\   |\n      |\n______|",
        ]
    ]

    if incorrect_guesses < len(hangman_parts[0]):
        print(hangman_parts[0][incorrect_guesses])
    else:
        print("Game over! You've reached the maximum number of incorrect guesses.")

def get_guess(secret_word, guessed_letters):
    while True:
        guess = input("Enter a letter or the whole word: ").lower()
        if guess and ((guess.isalpha() and len(guess) == 1) or (len(guess) > 1 and guess.isalpha())):
            return guess
        else:
            print("Invalid input. Please enter a single letter or the whole word.")


def show_instructions():
    
    print("Try to guess the secret word by entering one letter at a time.")
    print("If you think you know the whole word, you can enter the entire word.")
    print("Be careful! You have limited attempts before the hangman is complete.")
    print("Good luck!\n")
    return input("Do you want to continue to the game? (y/n): ").lower() == 'y'