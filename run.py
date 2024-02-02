import random
import colorama
from hangman_parts import display_hangman

colorama.init()


def choose_word():
    """
    Chooses a random word from a predefined list of words.
    Returns:
        str: The chosen word.
    """
    words = ["python", "hangman", "developer", "programming", "coding",
             "javascript", "software", "scripts", "terminal", "ubuntu"]
    return random.choice(words)


def display_word(word, guessed_letters):
    """
    Displays the current state of the word, revealing guessed letters.
    word (str): The secret word to be guessed.
    guessed_letters (list): List of letters that have been guessed.
    Returns a str: the word with underscores for unguessed letters.
    """
    return ' '.join(letter if letter in guessed_letters else '_'
                   for letter in word)


def get_guess():
    """
    Gets a valid user input for a letter or the entire word.
    Returns str: The user's input.
    """
    while True:
        guess = input("Enter a letter or the whole word: ").lower()
        if guess and (guess.isalpha() and len(guess) >= 1):
            return guess
        else:
            print(colorama.Style.BRIGHT + colorama.Fore.RED + "Invalid input. \
Please enter a single letter or the whole word." + colorama.Style.RESET_ALL)


def instructions():
    """
    Displays game instructions.
    """
    print(colorama.Style.BRIGHT + colorama.Back.BLACK + colorama.Fore.BLUE +
"Try to guess the secret word by entering one letter at a time.")
    print("(Hint: The secret word is tech-related)")
    print("If you think you know the whole word, \
you can enter the entire word.")
    print("Be careful! You have limited attempts before you get hanged!")
    print("You can choose from three difficulty levels, \
each with a different number of guessing attempts.")
    print("Good luck!\n" + colorama.Style.RESET_ALL)


def choose_difficulty():
    """
    Allows the user to choose the game difficulty level.
    Returns int: The maximum number of incorrect guesses allowed.
    Which is then used on the hangman_parts.py to display the hangman parts.
    """
    print("Choose a difficulty level:")
    print("1: Easy (12 guesses)")
    print("2: Medium (10 guesses)")
    print("3: Hard (8 guesses)")

    while True:
        difficulty_choice = input("Enter your choice (1, 2, or 3): ")

        if difficulty_choice == '1':
            return 12
        elif difficulty_choice == '2':
            return 10
        elif difficulty_choice == '3':
            return 8
        else:
            print(colorama.Style.BRIGHT + colorama.Fore.RED +
                  "Invalid input. Please enter '1', '2', or '3'." +
                  colorama.Style.RESET_ALL)


def display_game_state(secret_word, guessed_letters, guessed_words,
                       incorrect_guesses, max_incorrect_guesses, difficulty):
    """
    Displays the current state of the game, including the word, guessed letters, and hangman.
    secret_word (str): The secret word to be guessed.
    guessed_letters (list): List of letters that have been guessed.
    guessed_words (list): List of words that have been guessed.
    incorrect_guesses (int): Number of incorrect guesses made so far.
    max_incorrect_guesses (int): Maximum allowed incorrect guesses.
    difficulty (str): Difficulty level of the game.
    """
    current_display = display_word(secret_word, guessed_letters)
    guessed_words_display = ', '.join(guessed_words) if guessed_words else ''
    guessed_letters_display = ', '.join(guessed_letters)

    print(f"\nWord: {current_display}")
    """
    adds a comma and space (', ') only if both guessed_letters_display
    and guessed_words_display are not empty.
    Otherwise, it adds an empty string.
    """

    print(colorama.Style.BRIGHT + colorama.Back.BLACK + colorama.Fore.BLUE +
          f"Guesses: {guessed_letters_display}{', ' if guessed_letters_display and guessed_words_display else ''} "
          f"{guessed_words_display}")

    print(f"Incorrect guesses remaining: {max_incorrect_guesses - incorrect_guesses}")
    display_hangman(incorrect_guesses, max_incorrect_guesses, difficulty)


def show_game_instructions():
    """
    Displays the option to show game instructions and shows them if requested by the user.
    """
    print(colorama.Style.BRIGHT + colorama.Fore.YELLOW +
          "Do you want to see the instructions? (y/n): " +
          colorama.Style.RESET_ALL)

    while True:
        show_instructions = input().lower()

        if show_instructions in ['y', 'n']:
            break
        else:
            print(colorama.Style.BRIGHT + colorama.Fore.RED +
                  "Incorrect input. Please enter 'y' for yes or 'n' for no." +
                  colorama.Style.RESET_ALL)

    if show_instructions == 'y':
        instructions()


def display_game_over_message(secret_word):
    """
    Displays a game over message with the correct secret word.
    secret_word (str): The correct secret word.
    """
    print(f"\nSorry, you ran out of attempts. The correct word was '{secret_word}'.")


def start_new_game():
    show_game_instructions()

    while True:
        play_game = input(colorama.Style.BRIGHT + colorama.Fore.YELLOW +
                          "Do you want to start a new game? (y/n): " +
                          colorama.Style.RESET_ALL).lower()

        if play_game == 'n':
            print(colorama.Style.BRIGHT + colorama.Fore.YELLOW +
                  "Game ended. Goodbye!" + colorama.Style.RESET_ALL)
            return
        elif play_game == 'y':
            play_hangman_game()
            return
        else:
            print(colorama.Style.BRIGHT + colorama.Fore.RED +
                  "Incorrect input. Please enter 'y' to start a new game or 'n' to exit." +
                  colorama.Style.RESET_ALL)


def play_hangman_game():
    while True:
        secret_word = choose_word()
        guessed_letters = []
        guessed_words = []
        incorrect_guesses = 0
        max_incorrect_guesses = choose_difficulty()
        difficulty = 'easy' if max_incorrect_guesses == 12 else 'medium' if max_incorrect_guesses == 10 else 'hard'

        while incorrect_guesses < max_incorrect_guesses:
            display_game_state(secret_word, guessed_letters, guessed_words, incorrect_guesses, max_incorrect_guesses, difficulty)

            try:
                guess = get_guess()

                if len(guess) == 1:
                    incorrect_guesses = process_single_letter_guess(guess, secret_word, guessed_letters, incorrect_guesses)
                elif len(guess) > 1 and guess.isalpha():
                    incorrect_guesses = process_whole_word_guess(guess, secret_word, guessed_words, incorrect_guesses)

                if incorrect_guesses == -1:  # Player has won
                    break

                if all(letter in guessed_letters for letter in secret_word):
                    print(colorama.Style.BRIGHT + colorama.Fore.GREEN +
                          f"Congratulations! You guessed the word '{secret_word}'!" +
                          colorama.Style.RESET_ALL)
                    break

            except ValueError as ve:
                print(f"Invalid input: {ve}")

        if incorrect_guesses >= max_incorrect_guesses:
            display_game_over_message(secret_word)

        play_again = input(colorama.Style.BRIGHT + colorama.Fore.YELLOW +
                           "Do you want to play again? (y/n): " +
                           colorama.Style.RESET_ALL).lower()

        if play_again != 'y':
            print(colorama.Style.BRIGHT + colorama.Fore.YELLOW +
                  "Game ended." + colorama.Style.RESET_ALL)
            exit()

        show_game_instructions()  # Ask if the player wants to see instructions
        print(colorama.Style.BRIGHT + colorama.Fore.YELLOW +
              "Starting a new game..." + colorama.Style.RESET_ALL)

def hangman():
    """
    Initiates the Hangman game.
    Displays welcome messages, provides the option to view instructions,
    and enters the main game loop where players can choose to continue playing or exit.
    The game loop handles the selection of difficulty levels, the initiation of each game round,
    and the conclusion of the game with appropriate messages.
    """
     
    print("\nWelcome to Hangman!")
    show_game_instructions()

    while True:
        play_game = input(colorama.Style.BRIGHT + colorama.Fore.YELLOW +
                            "Do you want to continue to the game? (y/n): " +
                            colorama.Style.RESET_ALL).lower()

        while play_game not in ['y', 'n']:
            print(colorama.Style.BRIGHT + colorama.Fore.RED +
                    "Incorrect input. Please enter 'y' to continue or 'n' to exit." +
                    colorama.Style.RESET_ALL)
            play_game = input(colorama.Style.BRIGHT + colorama.Fore.YELLOW +
                                "Do you want to continue to the game? (y/n): " +
                                colorama.Style.RESET_ALL).lower()

        if play_game == 'n':
            print(colorama.Style.BRIGHT + colorama.Fore.YELLOW +
                    "Game ended. Goodbye!" + colorama.Style.RESET_ALL)
            return
        elif play_game == 'y':
            play_hangman_game()
        else:
            print(colorama.Style.BRIGHT + colorama.Fore.RED +
                    "Incorrect input. Please enter 'y' to continue or 'n' to exit." +
                    colorama.Style.RESET_ALL)


import random
import colorama
from hangman_parts import display_hangman

colorama.init()


def choose_word():
    """
    Chooses a random word from a predefined list of words.
    Returns:
        str: The chosen word.
    """
    words = ["python", "hangman", "developer", "programming", "coding",
             "javascript", "software", "scripts", "terminal", "ubuntu"]
    return random.choice(words)


def display_word(word, guessed_letters):
    """
    Displays the current state of the word, revealing guessed letters.
    word (str): The secret word to be guessed.
    guessed_letters (list): List of letters that have been guessed.
    Returns a str: the word with underscores for unguessed letters.
    """
    return ' '.join(letter if letter in guessed_letters else '_'
                   for letter in word)


def get_guess():
    """
    Gets a valid user input for a letter or the entire word.
    Returns str: The user's input.
    """
    while True:
        guess = input("Enter a letter or the whole word: ").lower()
        if guess and (guess.isalpha() and len(guess) >= 1):
            return guess
        else:
            print(colorama.Style.BRIGHT + colorama.Fore.RED + "Invalid input. \
Please enter a single letter or the whole word." + colorama.Style.RESET_ALL)



def process_single_letter_guess(guess, secret_word, guessed_letters,
                                incorrect_guesses):
    """
    Handles the single letter guesses, by substituting underscores with
    the correctly guessed letter(s)and incrementing the incorrect guesses
    value in case of incorrect guesses  - thereby reducing incorrect guesses
    remaining value from display_game_state function
    """
    if guess in guessed_letters:
        print(colorama.Style.BRIGHT + colorama.Fore.RED
              + "You've already made that guess. Please make another guess."
              + colorama.Style.RESET_ALL)
        return incorrect_guesses
    else:
        guessed_letters.append(guess)
        if guess not in secret_word:
            return incorrect_guesses + 1
        else:
            return incorrect_guesses


def process_whole_word_guess(guess, secret_word, guessed_words,
                             incorrect_guesses):
    """
    Handles full word guesses, by comparing the input value
    with the secret word, handles already guessed words by informing the user
    with the already guessed word and providing an option to play again
    in case of a correct guess.
    Returns:
        int: -1 if the player has won, 0 if the player wants to play again, otherwise returns incorrect_guesses.
    """
    if guess == secret_word:
        print(colorama.Style.BRIGHT + colorama.Fore.GREEN +
              "Congratulations! You guessed the word!" +
              colorama.Style.RESET_ALL)
        return -1  # Flag indicating the player has won

    elif guess in guessed_words:
        print(colorama.Style.BRIGHT + colorama.Fore.RED +
              "You've already guessed that word. Try again." +
              colorama.Style.RESET_ALL)
        return incorrect_guesses
    else:
        print(colorama.Style.BRIGHT + colorama.Fore.RED +
              "Incorrect guess. Try again." +
              colorama.Style.RESET_ALL)
        guessed_words.append(guess)
        return incorrect_guesses + 1



if __name__ == "__main__":
    hangman()
