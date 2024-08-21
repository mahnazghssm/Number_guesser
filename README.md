# Number Guessing Game

This Python-based Number Guessing Game allows players to guess a randomly generated number between 1 and 100. The player’s score starts at 100 and decreases by 10 points for each incorrect guess. The game provides feedback on whether the player's guess is too high or too low and allows the player to continue guessing or quit at any time.

## Project Structure
```
number-guessing-game/
|
|–game.py - The main game logic implementation
|
|–README.md - This file
```

## Requirements

- Python 3.7 or higher

## How to Run

To run the game, execute the `game.py` script using Python:

```bash
python game.py
```

## How to Play

	1.	When prompted, enter a number between 1 and 100 or ‘q’ to quit.
	2.	If your guess is higher than the computer’s number, you’ll receive a hint indicating that your guess is too high. If it’s lower, you’ll be told that it’s too low.
	3.	For each incorrect guess, your score will decrease by 10 points.
	4.	If you guess the correct number, you win the game and your score is displayed.
	5.	After winning or quitting, you will be asked if you want to play again:
	•	Enter yes to play another round. The game will restart with a new random number and your score will reset to 100.
	•	Enter no to quit the game. A thank you message will be displayed and the game will end.
	•	Enter q at any time to quit the game immediately.

### Example

Please enter your guess number (between 1 and 100) or 'q' to quit: 50
It is much higher than my choice. Please try again.
Your score is: 90

Please enter your guess number (between 1 and 100) or 'q' to quit: 25
It is much lower than my choice. Please try again.
Your score is: 80

Please enter your guess number (between 1 and 100) or 'q' to quit: 37
You win!
Your score is: 80
Would you like to play again? (yes/no): no
Thanks for playing. Goodbye!

## Learning Outcomes

By working on this project, you will gain:

	1.	Experience with handling user input and output in Python.
	2.	Familiarity with basic game logic and flow control.
	3.	Practice in managing game state and scoring.