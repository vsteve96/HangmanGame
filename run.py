import random

def choose_word():
    """
    A set of words that are chosen randomly at the start of the game
    """
    words = ["python", "hangman", "developer", "programming", "coding", ]
    return random.choice(words)

def display_word(word, guessed_letters):
    """
    Generates a display string for the word, revealing guessed letters and hiding others.
        word: The secret word to be guessed.
        guessed_letters (list): List of letters that the player has guessed.
    Returns a string: The current word
    """
    display = ""
    for letter in word:
        display += letter if letter in guessed_letters else "_"
    return display