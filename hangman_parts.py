def display_hangman(incorrect_guesses, max_incorrect_guesses, difficulty='medium'):
    """
    Displays the visual representation of the hangman parts based on
    difficulty and steps one line within the selected list at
    every incorrect guess.

    If the limit is reached, a game-over message is displayed,
    to prevent the game from continuing after there's no more attempts.
    """

    hangman_parts = {
        'easy': [
            "      \n      |\n      |\n      |\n      |\n______|",
            "     _\n      |\n      |\n      |\n      |\n______|",
            "    __\n      |\n      |\n      |\n      |\n______|",
            "   ___\n      |\n      |\n      |\n      |\n______|",
            "  ____\n      |\n      |\n      |\n      |\n______|",
            "  ____\n |    |\n      |\n      |\n      |\n______|",
            "  ____\n |    |\n O    |\n      |\n      |\n______|",
            "  ____\n |    |\n O    |\n |    |\n      |\n______|",
            "  ____\n |    |\n O    |\n/|    |\n      |\n______|",
            "  ____\n |    |\n O    |\n/|\\   |\n      |\n______|",
            "  ____\n |    |\n O    |\n/|\\   |\n  \\   |\n______|",
            "  ____\n |    |\n O    |\n/|\\   |\n/ \\   |\n______|",
        ],
        'medium': [
            "    __\n      |\n      |\n      |\n      |\n______|",
            "   ___\n      |\n      |\n      |\n      |\n______|",
            "  ____\n      |\n      |\n      |\n      |\n______|",
            "  ____\n |    |\n      |\n      |\n      |\n______|",
            "  ____\n |    |\n O    |\n      |\n      |\n______|",
            "  ____\n |    |\n O    |\n |    |\n      |\n______|",
            "  ____\n |    |\n O    |\n/|    |\n      |\n______|",
            "  ____\n |    |\n O    |\n/|\\   |\n      |\n______|",
            "  ____\n |    |\n O    |\n/|\\   |\n  \\   |\n______|",
            "  ____\n |    |\n O    |\n/|\\   |\n/ \\   |\n______|",
        ],
        'hard': [
            "  ____\n      |\n      |\n      |\n      |\n______|",
            "  ____\n |    |\n      |\n      |\n      |\n______|",
            "  ____\n |    |\n O    |\n      |\n      |\n______|",
            "  ____\n |    |\n O    |\n |    |\n      |\n______|",
            "  ____\n |    |\n O    |\n/|    |\n      |\n______|",
            "  ____\n |    |\n O    |\n/|\\   |\n      |\n______|",
            "  ____\n |    |\n O    |\n/|\\   |\n  \\   |\n______|",
            "  ____\n |    |\n O    |\n/|\\   |\n/ \\   |\n______|",
        ],
    }

    # The condition checks if  incorrect_guesses is less than the total
    # number of steps needed to complete the hangman.
    # If incorrect_guesses reaches that number, the full hangman is printed,
    # and the game-over message is displayed.

    if difficulty not in hangman_parts:
        print(f"Invalid difficulty level: {difficulty}")
        return

    if incorrect_guesses < max_incorrect_guesses:
        print(hangman_parts[difficulty][incorrect_guesses])
    else:
        print("Game over! You've reached the maximum number of \
incorrect guesses.")
