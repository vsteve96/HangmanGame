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

def display_game_state(word, guessed_letters, guessed_words, incorrect_guesses, 
max_incorrect_guesses, difficulty):
    current_display = display_word(word, guessed_letters)
    guessed_words_display = ', '.join(guessed_words) if len(guessed_words) > 1 else ''.join(guessed_words)
    guessed_letters_display = ', '.join(guessed_letters)

    print(f"\nWord: {current_display}")
    print(f"Guesses: {guessed_letters_display}{', ' if guessed_letters_display and 
    guessed_words_display else ''}{guessed_words_display}")
    print(f"Attempts Left: {max_incorrect_guesses - incorrect_guesses}")
    display_hangman(incorrect_guesses, max_incorrect_guesses)

def hangman():
    print("\nWelcome to Hangman!")
    show_instructions_flag = input("Do you want to see the instructions? (y/n): ").lower() == 'y'
    
    if show_instructions_flag:
        show_instructions()
        
    secret_word = choose_word()
    guessed_letters = []
    guessed_words = []
    incorrect_guesses = 0
    difficulty = choose_difficulty()
    max_incorrect_guesses = difficulty

    while incorrect_guesses < max_incorrect_guesses:
        display_game_state(secret_word, guessed_letters, guessed_words, incorrect_guesses,
        max_incorrect_guesses, difficulty)
        guess = get_guess(secret_word, guessed_letters)

        if len(guess) == 1:
            if guess in guessed_letters:
                print("You've already made that guess. Please make another guess.")
            else:
                guessed_letters.append(guess)
                if guess not in secret_word:
                    incorrect_guesses += 1
        elif len(guess) > 1 and guess.isalpha():
            if guess == secret_word:
                print("Congratulations! You guessed the word!")
                break
            elif guess in guessed_words:
                print("You've already guessed that word. Try again.")
            else:
                print("Incorrect guess. Try again.")
                if guess.lower() not in [word.lower() for word in guessed_words]:
                    guessed_words.append(guess)  # Append only if not already guessed
                    incorrect_guesses += 1
        else:
            print("Invalid input. Please enter a single letter or the whole word.")

    if incorrect_guesses == max_incorrect_guesses:
        print(f"\nSorry, you ran out of attempts. The correct word was '{secret_word}'.")

if __name__ == "__main__":
    hangman()