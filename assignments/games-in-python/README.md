# 📘 Assignment: Games in Python

## 🎯 Objective

Build a classic Hangman word-guessing game using Python strings, loops, conditional statements, and user input.

## 📝 Tasks

### 🛠️ Set Up the Game

#### Description
Prepare the starting state for the Hangman game. The starter code provides a list of possible words and placeholders for the game variables.

#### Requirements
Completed program should:

- Randomly select a secret word from the predefined `words` list
- Track guessed letters
- Track the number of incorrect guesses
- Set a maximum number of incorrect guesses

### 🛠️ Create the Guessing Loop

#### Description
Repeatedly ask the player to guess a letter and update the game state until the word is found or the player runs out of attempts.

#### Requirements
Completed program should:

- Accept letter guesses from the user
- Reject input that is not a single letter
- Check whether each valid guess appears in the secret word
- Avoid counting repeated guesses as additional incorrect guesses
- Display the current progress in `_ _ _` format
- Display the letters that have been guessed incorrectly

### 🛠️ End the Game

#### Description
Finish the game with a clear result when the player wins or loses.

#### Requirements
Completed program should:

- End when every letter in the secret word has been guessed
- End when the player reaches the maximum number of incorrect guesses
- Display a win message when the player guesses the word
- Display a lose message that reveals the secret word
