import random
import colorama
from hangman_parts import display_hangman

colorama.init()

def choose_word():
    words = ["python", "hangman", "developer", "programming", "coding", "javascript",
             "software", "scripts", "terminal", "ubuntu"]
    return random.choice(words)

def display_word(word, guessed_letters):
    return ''.join(letter if letter in guessed_letters else '_' for letter in word)

def get_guess():
    while True:
        guess = input("Enter a letter or the whole word: ").lower()
        if guess and (guess.isalpha() and len(guess) >= 1):
            return guess
        else:
            print("Invalid input. Please enter a single letter or the whole word.")

def instructions():
    print(colorama.Style.BRIGHT + colorama.Back.BLACK + colorama.Fore.BLUE + "Try to guess the secret word by entering one letter at a time.")
    print("(Hint: The secret word is tech-related)")
    print("If you think you know the whole word, you can enter the entire word.")
    print("Be careful! You have limited attempts before you get hanged!")
    print("You can choose from three difficulty levels, each with a different number of guessing attempts.")
    print("Good luck!\n" + colorama.Style.RESET_ALL)
    
def choose_difficulty():
    print(colorama.Style.BRIGHT + colorama.Back.BLACK + colorama.Fore.MAGENTA + "Choose a difficulty level:")
    print("1: Easy (12 guesses)")
    print("2: Medium (10 guesses)")
    print("3: Hard (8 guesses)")

    difficulty_choice = input("Enter your choice (1, 2, or 3): " + colorama.Style.RESET_ALL)

    if difficulty_choice == '1':
        return 12
    elif difficulty_choice == '2':
        return 10
    elif difficulty_choice == '3':
        return 8
    else:
        print("Invalid choice. Defaulting to Medium difficulty.")
        return 10

def display_game_state(secret_word, guessed_letters, guessed_words,
                       incorrect_guesses, max_incorrect_guesses):
    # Display the current state of the secret word with guessed letters revealed
    current_display = display_word(secret_word, guessed_letters)
    # Format the display of guessed words with commas
    guessed_words_display = ', '.join(guessed_words) if guessed_words else ''
    # Format the display of guessed letters with commas
    guessed_letters_display = ', '.join(guessed_letters)

    print(f"\nWord: {current_display}")
    """
    adds a comma and space (', ') only if both guessed_letters_display
    and guessed_words_display are not empty. 
    Otherwise, it adds an empty string.
    """
    # Print guessed letters and guessed words with appropriate formatting
    print(colorama.Style.BRIGHT + colorama.Back.BLACK + colorama.Fore.BLUE + 
          f"Guesses: {guessed_letters_display}{', ' if guessed_letters_display and guessed_words_display else ''}{guessed_words_display}")
    # Print the number of incorrect guesses remaining and display the hangman
    print(f"Incorrect guesses remaining: {max_incorrect_guesses - incorrect_guesses}")
    display_hangman(incorrect_guesses, max_incorrect_guesses, difficulty='easy)

def hangman():
    """
    The main hangman game logic.

    """
    print("\nWelcome to Hangman!")

    incorrect_guesses = 0

    show_instructions = input("Do you want to see the instructions? (y/n): ").lower()
    if show_instructions == 'y':
        instructions()

    play_game = input("Do you want to continue to the game? (y/n): ").lower() 
    if play_game == 'y':

        secret_word = choose_word()
        guessed_letters = []
        guessed_words = []
            
        # Set the return value from choose_difficulty function as the maximum 
        # incorrect guesses allowed
        max_incorrect_guesses = choose_difficulty()
            
        while incorrect_guesses < max_incorrect_guesses:
            display_game_state(secret_word, guessed_letters, guessed_words, incorrect_guesses, max_incorrect_guesses)

            guess = get_guess()
                
            if len(guess) == 1:
                incorrect_guesses = process_single_letter_guess(guess, secret_word, guessed_letters, incorrect_guesses)
            elif len(guess) > 1 and guess.isalpha():
                incorrect_guesses = process_whole_word_guess(guess, secret_word, guessed_words, incorrect_guesses)

            if all(letter in guessed_letters for letter in secret_word):
                print(f"Congratulations! You guessed the word '{secret_word}'!")
                break
                
        if incorrect_guesses == max_incorrect_guesses:
            print(f"\nSorry, you ran out of attempts. The correct word was '{secret_word}'.")

    elif play_game == 'n':
        print("Game ended. Goodbye!")
        return

def process_single_letter_guess(guess, secret_word, guessed_letters, incorrect_guesses):
    if guess in guessed_letters:
        print("You've already made that guess. Please make another guess.")
        return incorrect_guesses
    else:
        guessed_letters.append(guess)
        if guess not in secret_word:
            return incorrect_guesses + 1
        else:
            return incorrect_guesses

def process_whole_word_guess(guess, secret_word, guessed_words, incorrect_guesses):
    if guess == secret_word:
        print("Congratulations! You guessed the word!")
        exit()
    elif guess in guessed_words:
        print("You've already guessed that word. Try again.")
        return incorrect_guesses
    else:
        print("Incorrect guess. Try again.")
        guessed_words.append(guess)
        return incorrect_guesses + 1

if __name__ == "__main__":
    hangman()