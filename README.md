# Number Guessing Game

A simple Python number guessing game. Choose a difficulty level and try to guess the randomly selected number before the time runs out.

## Features

- Three difficulty levels
- Different number ranges for each level
- Time limit for each game
- Hints for guesses that are too high or too low
- "Very close" hint when the guess is within 10
- `q` to quit the game
- Option to play again

## Difficulty Levels

| Level  | Number Range | Time Limit |
| ------ | ------------ | ---------- |
| Easy   | 1–50         | 60 seconds |
| Medium | 1–100        | 45 seconds |
| Hard   | 1–200        | 30 seconds |

## Project Structure

```text id="k5y8zz"
.
├── .gitignore
├── README.md
└── src
    └── main.py
```

- `src/main.py`: contains the game logic
- `.gitignore`: files and folders ignored by Git
- `README.md`: project documentation

## Requirements

- Python 3.10 or later
- No external packages are required

## Running the Project

Run the game from the project root:

```bash id="6l1gqv"
python src/main.py
```

## How to Play

Choose a difficulty level and start guessing the number.

The game will tell you if your guess is:

- Too high
- Too low
- Very close
- Correct

You can type `q` at any time to quit.

After guessing the number correctly, you can choose whether to play again.

## Example

```text id="8n0c9r"
Choose difficulty: Easy, Medium, or Hard (or type 'q' to quit): medium

You have 44 seconds left.
Guess a number between 1 to 100 or type 'q' to quit: 45
You guessed 45, which is too low! Try a higher number.

You have 40 seconds left.
Guess a number between 1 to 100 or type 'q' to quit: 88
You're very close! You guessed 88. Try lower.

You have 36 seconds left.
Guess a number between 1 to 100 or type 'q' to quit: 85
Congratulations, you guessed the number in 3 attempts!

Do you want to play again? (yes/no): no
Goodbye! Thanks for playing!
```

## License

This project is licensed under the MIT License.
