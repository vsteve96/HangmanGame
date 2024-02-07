# Hangman Game

## Overview

Welcome to the Hangman Game! This project implements the classic Hangman word guessing game in Python. The game challenges players to guess a secret word by suggesting letters or guessing the entire word. 
Incorrect guesses lead to the gradual drawing of a hangman, and players must solve the word before running out of attempts.

### Engaging Gameplay

- Enjoy the thrill of guessing words letter by letter or trying to guess the entire word at once.
- Test your vocabulary and word recognition skills in a challenging yet enjoyable way.
- Multiple difficulty levels allow players to choose the level of challenge that suits them best.
- Perfect for killing time during commutes, waiting in line, or simply relaxing at home.

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

## Deployment Process

Follow these steps to deploy the Hangman game project:

### 1. Clone the Repository

Clone the repository to your local machine using Git:

```bash```
git clone https://github.com/vsteve96/hangman.git


# Dependencies

- **blinker** (version 1.7.0)
- **click** (version 8.1.7)
- **colorama** (version 0.4.6)
- **flask** (version 3.0.1)
- **importlib-metadata** (version 7.0.1)
- **itsdangerous** (version 2.1.2)
- **Jinja2** (version 3.1.3)
- **MarkupSafe** (version 2.1.4)
- **werkzeug** (version 3.0.1)
- **zipp** (version 3.17.0)

#### To install these dependencies simply use pip:

```pip install -r requirements.txt```

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

**The flow of the game**

User Input: show_instructions

- The program starts by asking the user if they want to see instructions (show_instructions).
If the user enters an invalid input, the program repeatedly prompts until a valid input ('y' or 'n') is received.
Instructions Displayed: instructions()

![Instructions](/images/instructions.png)

- If the user chose to see instructions, the instructions() function is called to display the game instructions.
User Input: play_game

![Incorrect_input](/images/incorrect_input.png)

- The program then asks the user if they want to continue to the game (play_game).
If the user enters an invalid input, the program repeatedly prompts until a valid input ('y' or 'n') is received.
Game Initialization

![Continue](/images/continue.png)

- If the user decides to play (play_game == 'y'), the game initializes by choosing a word and setting difficulty.
Game Loop

![Game](/images/game.png)

- The main game loop starts (while incorrect_guesses < max_incorrect_guesses).
The player makes guesses until they win or run out of attempts.
Game Outcome

![Congratulations](/images/congratulations.png)

- If the player wins, a congratulatory message is displayed, and the loop breaks.
If the player loses, a message indicating the correct word is displayed.
Game Termination

- If the player chooses not to play (play_game == 'n'), a farewell message is displayed, and the program returns.

![Farewell](/images/farewell.png)

## User Feedback
*Invalid Input Handling*

- If the user enters an invalid input for playing the game (else block), the program repeatedly prompts until a valid input ('y' or 'n') is received.

![Invalid_input](/images/invalid_input.png)

- In case of invalid input, players receive informative error messages guiding them on the correct input format. This ensures that players understand why their input was rejected and encourages them to provide valid input.

- By implementing robust input validations, the development process aims to enhance user experience, prevent unintended errors, and make the Hangman game more enjoyable for the players.

**Flowchart**

![flowchart](/images/flowchart_1.png)

**Testing**

| Test Case Description | Expected Outcome | Testing Performed | Result | Pass/Fail |
| ---------| ---------| ---------| ---------| ---------|
| Verify game starts with asking to show the instructions    |     The game's first 2 initiations should prompt the see the instructions question  |     Initiated game, restarted 4 rounds, played 5 rounds altogether    |     The game showed the instructions prompt at the first 2 rounds, but didn't from the 3rd round as intended    |     Pass     |
| Verify game handles incorrect input at the instructions prompt    |     The program should handle incorrect input at instructions prompt  |     Initiated game, gave incorrect input for instructions prompt    |     The program returned a string, informing that I should input either 'y' or 'n' at the instructions prompt     |     Pass     |
| Verify game asks if the player wants to continue after showing the instructions    |     After 'y' input the game should initiate, after 'n', the game should exit   |     Tested both outcomes     |     After 'y' input the game initiated, after 'n' the game quit     |     Pass     |
| Verify game handles incorrect input at continue prompt    |     The program should handle incorrect input at continue prompt   |     Initiated game, gave incorrect input for continue prompt     |     The program returned a string, informing that I should input either 'y' or 'n' at the continue prompt     |     Pass     |
| Guessing a valid letter guess    |     The letter should be revealed within the word if the secret word contains it    |     Guessed a valid letter, contained in the word     |     The letter(s) revealed within the word, removing the initial underscore(s) from that spot     |     Pass     |
| Guessing an invalid letter guess    |     The game should prompt for a valid letter guess    |     Guessed an invalid guess, tested with symbols and numbers     |     The game returned a string, informing that it's an invalid input and prompt to enter a single letter or the whole word.     |     Pass     |
| Guessing an incorrect letter guess, that the secret word does not contain  |     The hangman display should progress one step, the incorrect guesses counter should also progress, therefore reducing the max number of guesses by 1     |     Guessed an incorrect guess     |     The hangman display progressed one step, the max number of guesses reduced by one     |     Pass     |
| Guessing an invalid word guess, that is not in the allowed format |     The game should prompt for a valid guess     |     Guessed an invalid word guess     |     The game returned a string, informing that it's an invalid input and prompt to enter a single letter or the whole word.     |     Pass     |
| Guessing an incorrect word guess, that is not the secret word |     The hangman display should progress one step, the incorrect guesses counter should also progress, therefore reducing the max number of guesses by 1     |     Guessed an incorrect word guess that is not the secret word    |     The hangman display progressed one step, the max number of guesses reduced by one     |     Pass     |
| Word populated  |     The word is displayed from the words array    |    Checked manually the word shown is pulled from the right array     |     The word is displaying from the correct array     |     Pass     |
| Selecting difficulty level    |     The maximum allowed number of incorrect guesses should match the selected difficulty level.     |     Chose each level option (easy, medium, hard)     |     The maximum allowed number of incorrect guesses matched the chosen difficulty level (easy-12, medium-10, hard-8)     |     Pass     |
| Finishing the game with reaching the maximum allowed number of incorrect guesses    |     The game should return a string, informing the player about the exceeded maximum allowed number of incorrect guesses, showing the secret word and prompting the new game option    |     Tested on all difficulty levels, reached maximum allowed number of incorrect guesses     |     The game returned the secret word, prompted the player with the new game option     |     Pass      |
| Finishing the game with correctly guessing the secret word as a whole word  |     The game should return the congratulations string and prompt the new game option.   |     Finished the game by guessing the secret word as a whole.     |     The game congratulated and prompted the new game option     |     Pass     |
| Finishing the game with correctly guessing the secret word by guessing the correct letters   |     The game should return the congratulations string and prompt the new game option.   |     Finished the game by guessing the secret word one letter at a time     |     The game congratulated and prompted the new game option     |     Pass     |
| Displaying hangman parts    |    The hangman display should progress one step at each incorrect guess     |     Made multiple incorrect guesses and inspected the hangman progression     |     Tested on each difficulty level, the hangman display progressed correctly  |     Pass      |
| Testing the new game prompt    |    The game should ask if the player wants to see the instructions again at the first 2 rounds, and after selecting 'y' the game should restart, resetting the hangman progression and incorrect guesses counter     |     Played multiple rounds, selected 'y' and 'n' at the new game prompt     |     Selecting 'y' initiated a new game, resetting everything correctly, selecting 'n' exited the game  |     Pass      |
| Testing invalid input at the new game prompt    |    The game should handle invalid input at the new game prompt     |     Played multiple rounds, gave invalid input at the new game prompt     |     The game returned the string with the information that the player's input can only be either 'y' or 'n'  |     Pass      |


## Test Case 1

Objective: Ensure game initializes correctly with the appropiate settings.

**Steps taken:**

1. Run the game
2. Verify that game starts with no guessed letters and no incorrect guesses.

**Expected outcome:** 
- The game should initialize without any errors and display the initial game state.

**Testing:**
- Testing by initiating the game
- Observed the game state upon start

**Result:**
- The game initialized successfully with the expected initial settings.

Fix:
- No fix required

## Test Case 2
Finishing the game with reaching the maximum allowed number of incorrect guesses

**Objective:** Test the game's behavior when the maximum allowed number of incorrect guesses is reached.

**Steps:**
- Make incorrect guesses until the maximum allowed number is reached.

**Expected Outcome:** The game should end with a defeat message, reveal the correct word, and prompt the player with a new game option.

**Testing:**
- Reached the maximum allowed number of incorrect guesses on each difficulty level.

**Result:** The game ended with a defeat message, displayed the correct word, and prompted the player with a new game option.

**Fix:** No fix required; the game functioned as intended.

## Test Case 3

**Objective:** Test the functionality of displaying hangman parts based on the number of incorrect guesses on all difficulty levels.

**Steps:**
- Invoke the display_hangman function with different numbers of incorrect guesses.
1. Test with 0 incorrect guesses.
2. Test with 1 incorrect guess.
3. Test with 2 incorrect guesses.
4. Test with the maximum allowed incorrect guesses.

**Expected Outcome:** The function should display the corresponding hangman parts based on the number of incorrect guesses, and handle the chosen difficulty level correctly.

- Easy difficulty level:
1. For 0 incorrect guesses, there should be 11 missing parts on the hangman display.
2. For 1 incorrect guess, there should be 10 missing parts on the hangman display.
3. For 2 incorrect guesses, there should be 9 missing parts on the hangman display.
4. For the maximum allowed incorrect guesses, the complete hangman should be displayed.

- Medium difficulty level:
1. For 0 incorrect guesses, there should be 9 missing parts on the hangman display.
2. For 1 incorrect guess, there should be 8 missing parts on the hangman display.
3. For 2 incorrect guesses, there should be 7 missing parts on the hangman display.
4. For the maximum allowed incorrect guesses, the complete hangman should be displayed.
- Hard difficulty level:
1. For 0 incorrect guesses, there should be 7 missing parts on the hangman display.
2. For 1 incorrect guess, there should be 6 missing parts on the hangman display.
3. For 2 incorrect guesses, there should be 5 missing parts on the hangman display.
4. For the maximum allowed incorrect guesses, the complete hangman should be displayed.

**Testing:**
- Stepped through the allowed number of guesses, reached the maximum allowed number of incorrect guesses and observed the hangman display progression on each difficulty level.

**Result:** The game handled the hangman display drawing on all difficulty levels correctly.

**Fix:** No fix required; the game functioned as intended.

## Accreditation

This Hangman Game project is created and maintained by [Me](https://github.com/vsteve96). Feel free to contribute to the project or provide feedback!
I'd like to express my gratitude to Graeme Taylor, my mentor, for helping me get through my milestone project work, by his guidance and support.