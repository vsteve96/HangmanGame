import random
import colorama
from hangman_parts import display_hangman

colorama.init()


def choose_word():
    words = ["python", "hangman", "developer", "programming", "coding",
             "javascript", "software", "scripts", "terminal", "ubuntu"]
    return random.choice(words)


def display_word(word, guessed_letters):
    return ''.join(letter if letter in guessed_letters else '_'
                   for letter in word)


def get_guess():

    while True:
        guess = input("Enter a letter or the whole word: ").lower()
        if guess and (guess.isalpha() and len(guess) >= 1):
            return guess
        else:
            print(colorama.Style.BRIGHT + colorama.Fore.RED + "Invalid input. \
Please enter a single letter or the whole word." + colorama.Style.RESET_ALL)


def instructions():
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
    print(
          "Choose a difficulty level:")
    print("1: Easy (12 guesses)")
    print("2: Medium (10 guesses)")
    print("3: Hard (8 guesses)")

    difficulty_choice = input("Enter your choice (1, 2, or 3): " +
                              colorama.Style.RESET_ALL)
    try:
        if difficulty_choice == '1':
            return 12
        elif difficulty_choice == '2':
            return 10
        elif difficulty_choice == '3':
            return 8
    except ValueError as e:
        print(e)
        return choose_difficulty


def display_game_state(secret_word, guessed_letters, guessed_words,
                       incorrect_guesses, max_incorrect_guesses, difficulty):
    # Display the current state of the secret word
    # with guessed letters revealed
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
      f"Guesses: {guessed_letters_display}{', ' if guessed_letters_display and guessed_words_display else ''} "
      f"{guessed_words_display}")

    # Print the number of incorrect guesses remaining and display the hangman
    print(f"Incorrect guesses remaining: {max_incorrect_guesses - incorrect_guesses}")
    display_hangman(incorrect_guesses, max_incorrect_guesses, difficulty)


def hangman():
    """
    The main hangman game loop
    """
    print("\nWelcome to Hangman!")

    incorrect_guesses = 0

    show_instructions = input(colorama.Style.BRIGHT + colorama.Fore.YELLOW
                          + "Do you want to see the instructions? (y/n): "
                          + colorama.Style.RESET_ALL).lower()

    while show_instructions not in ['y', 'n']:
        print(colorama.Style.BRIGHT + colorama.Fore.RED +
            "Incorrect input. Please enter 'y' for yes or 'n' for no." +
            colorama.Style.RESET_ALL)
        show_instructions = input(colorama.Style.BRIGHT + colorama.Fore.YELLOW +
                                "Do you want to see the instructions? (y/n): " +
                                colorama.Style.RESET_ALL).lower()

    if show_instructions == 'y':
        instructions()

    play_game = input(colorama.Style.BRIGHT + colorama.Fore.YELLOW +
                      "Do you want to continue to the game? (y/n): " +
                      colorama.Style.RESET_ALL).lower()

    if play_game == 'y':

        secret_word = choose_word()
        guessed_letters = []
        guessed_words = []

        # Set the return value from choose_difficulty function as the maximum
        # incorrect guesses allowed
        max_incorrect_guesses = choose_difficulty()

        # Get the chosen difficulty level
        difficulty = 'easy'  # Default to 'easy'
        if max_incorrect_guesses == 10:
            difficulty = 'medium'
        elif max_incorrect_guesses == 8:
            difficulty = 'hard'

        while incorrect_guesses < max_incorrect_guesses:
            display_game_state(secret_word, guessed_letters, guessed_words,
                               incorrect_guesses, max_incorrect_guesses, difficulty)
            try:
                guess = get_guess()

                if len(guess) == 1:
                    incorrect_guesses = process_single_letter_guess(guess, secret_word, 
                                                                    guessed_letters, 
                                                                    incorrect_guesses)
                elif len(guess) > 1 and guess.isalpha():
                    incorrect_guesses = process_whole_word_guess(guess, secret_word, 
                                                                 guessed_words, 
                                                                 incorrect_guesses)

                if all(letter in guessed_letters for letter in secret_word):
                    print(colorama.Style.BRIGHT + colorama.Fore.GREEN 
                    + f"Congratulations! You guessed the word '{secret_word}'!" + colorama.Style.RESET_ALL)
                    break
            except ValueError as ve:
                print(f"Invalid input: {ve}")

        if incorrect_guesses == max_incorrect_guesses:
            print(f"\nSorry, you ran out of attempts. The correct word was '{secret_word}'.")

    elif play_game == 'n':
        print(colorama.Style.BRIGHT + colorama.Fore.YELLOW +
              "Game ended. Goodbye!" + colorama.Style.RESET_ALL)
        return
    else:
        while play_game not in ['y', 'n']:
            print(colorama.Style.BRIGHT + colorama.Fore.RED \
+ "Incorrect input. Please enter 'y' to continue or 'n' to exit." \
+ colorama.Style.RESET_ALL)
            play_game = input(colorama.Style.BRIGHT + colorama.Fore.YELLOW +
                            "Do you want to continue to the game? (y/n): " +
                            colorama.Style.RESET_ALL).lower() 


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
    with the already guessed word and exiting the loop in case
    of correct guess.
    """
    if guess == secret_word:
        print(colorama.Style.BRIGHT + colorama.Fore.GREEN +
              "Congratulations! You guessed the word!" +
              colorama.Style.RESET_ALL)
        exit()
    elif guess in guessed_words:
        print(colorama.Style.BRIGHT + colorama.Fore.RED +
              "You've already guessed that word. Try again." +
              colorama.Style.RESET_ALL)
        return incorrect_guesses
    else:
        print(colorama.Style.BRIGHT + colorama.Fore.RED +
              "Incorrect guess. Try again." + colorama.Style.RESET_ALL)
        guessed_words.append(guess)
        return incorrect_guesses + 1


if __name__ == "__main__":
    hangman()
