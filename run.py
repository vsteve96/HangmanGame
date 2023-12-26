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

def choose_difficulty():
    print("Choose a difficulty level:")
    print("1: Easy (12 guesses)")
    print("2: Medium (10 guesses)")
    print("3: Hard (8 guesses)")

    difficulty_choice = input("Enter your choice (1, 2, or 3): ")

    if difficulty_choice == '1':
        return 12
    elif difficulty_choice == '2':
        return 10
    elif difficulty_choice == '3':
        return 8
    else:
        print("Invalid choice. Defaulting to Medium difficulty.")
        return 10

def display_game_state(word, guessed_letters, guessed_words, incorrect_guesses, max_incorrect_guesses, difficulty):
    current_display = display_word(word, guessed_letters)
    guessed_words_display = ', '.join(guessed_words) if len(guessed_words) > 1 else ''.join(guessed_words)
    guessed_letters_display = ', '.join(guessed_letters)

    print(f"\nWord: {current_display}")
    print(f"Guesses: {guessed_letters_display}{', ' if guessed_letters_display and guessed_words_display else ''}{guessed_words_display}")
    print(f"Attempts Left: {max_incorrect_guesses - incorrect_guesses}")
    display_hangman(incorrect_guesses, max_incorrect_guesses)