def display_hangman(incorrect_guesses, max_incorrect_guesses):
    """
    Displays the visual representation of the hangman based on incorrect guesses.

    The function prints hangman art corresponding to incorrect guesses.
    If the limit is reached, a game-over message is displayed.
    """

    hangman_parts = [
    [
        "  ____\n |    |\n      |\n      |\n      |\n      |\n______|",  
        "  ____\n |    |\n O    |\n      |\n      |\n      |\n______|",  
        "  ____\n |    |\n O    |\n |    |\n      |\n      |\n______|",  
        "  ____\n |    |\n O    |\n/|    |\n      |\n      |\n______|",  
        "  ____\n |    |\n O    |\n/|\\   |\n      |\n      |\n______|",  
        "  ____\n |    |\n O    |\n/|\\   |\n/     |\n      |\n______|",  
        "  ____\n |    |\n O    |\n/|\\   |\n/ \\   |\n      |\n______|",  
        "  ____\n |    |\n O    |\n/|\\   |\n/ \\   |\n      |\n______|",  
        "  ____\n |    |\n O    |\n/|\\   |\n/ \\   |\n      |\n______|",  
        "  ____\n |    |\n O    |\n/|\\   |\n/ \\   |\n      |\n______|",  
        "  ____\n |    |\n O    |\n/|\\   |\n/ \\   |\n      |\n______|",  
        "  ____\n |    |\n O    |\n/|\\   |\n/ \\   |\n      |\n______|" 
    ]
]
    # Check if there are still available hangman parts based on the incorrect guesses
    if incorrect_guesses < len(hangman_parts):
        print(hangman_parts[0][incorrect_guesses])
    else:
        print("Game over! You've reached the maximum number of incorrect guesses.")