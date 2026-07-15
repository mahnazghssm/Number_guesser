"""
Author: Mahnaz Ghassemi
Date created: 05,01,2024
Description: Number Guessing Game with difficulty levels and time limits
"""

import random
import time
from typing import Tuple


def select_difficulty() -> Tuple[int | None, str | None, int | None, int | None, int | None]:
    """
    Prompts the user to select a difficulty level and returns relevant game settings.

    Returns:
        tuple:
            - computer_choice (int | None): The number randomly chosen by the computer.
            - range_text (str | None): Text representation of the guessing range (e.g., "1 to 50").
            - min_range (int | None): Minimum possible value in the range.
            - max_range (int | None): Maximum possible value in the range.
            - time_limit (int | None): Time limit in seconds to guess the number.
    """
    while True:
        difficulty = input("Choose difficulty: Easy, Medium, or Hard (or type 'q' to quit): ").lower()

        if difficulty == "easy":
            return random.randint(1, 50), "1 to 50", 1, 50, 60
        elif difficulty == "medium":
            return random.randint(1, 100), "1 to 100", 1, 100, 45
        elif difficulty == "hard":
            return random.randint(1, 200), "1 to 200", 1, 200, 30
        elif difficulty == "q":
            # Exit signal
            return None, None, None, None, None
        else:
            print("Invalid input. Please choose Easy, Medium, or Hard.")


def play_guessing_game(
    computer_choice: int,
    range_text: str,
    min_range: int,
    max_range: int,
    time_limit: int
) -> bool:
    """
    Main gameplay loop where the user tries to guess the number within a time limit.

    Args:
        computer_choice (int): The target number to guess.
        range_text (str): A string representation of the valid range (e.g., "1 to 100").
        min_range (int): Minimum allowed guess.
        max_range (int): Maximum allowed guess.
        time_limit (int): Time limit in seconds for guessing.

    Returns:
        bool: True if the user guesses correctly, False otherwise (timeout or quit).
    """
    attempts = 0
    start_time = time.time()

    while True:
        # Calculate remaining time
        elapsed_time = time.time() - start_time
        time_left = max(0, time_limit - int(elapsed_time))

        if time_left == 0:
            print(f"Time's up! The correct number was {computer_choice}. You ran out of time!")
            return False

        print(f"You have {time_left} seconds left.")
        user_guess = input(f"Guess a number between {range_text} or type 'q' to quit: ")

        if user_guess.lower() == "q":
            print("Exiting the game. Have a great day!")
            return False

        try:
            guess = int(user_guess)
        except ValueError:
            print(f"Invalid input. Please enter a number between {min_range} and {max_range} or 'q' to quit.")
            continue

        attempts += 1

        # Out-of-range input check
        if guess < min_range or guess > max_range:
            print(f"Out of range! Please choose a number between {min_range} and {max_range}.")
        # Correct guess
        elif guess == computer_choice:
            print(f"🎉 Congratulations, you guessed the number in {attempts} attempts!")
            return True
        # Close guess (within 10 units)
        elif abs(guess - computer_choice) <= 10:
            print(f"You're very close! You guessed {guess}. Try {'higher' if guess < computer_choice else 'lower'}.")
        # Too low
        elif guess < computer_choice:
            print(f"You guessed {guess}, which is too low! Try a higher number.")
        # Too high
        else:
            print(f"You guessed {guess}, which is too high! Try a lower number.")


def ask_to_play_again() -> bool:
    """
    Asks the user whether they would like to play again.

    Returns:
        bool: True if the user wants to play again, False otherwise.
    """
    play_again = input("Do you want to play again? (yes/no): ").lower()
    return play_again == "yes"


def main() -> None:
    """
    Controls the overall flow of the game:
    - Displays welcome message
    - Handles difficulty selection
    - Runs guessing game loop
    - Handles replay prompt
    """
    print("🎯 Welcome to the Random Number Guessing Game by Mahnaz Ghassemi 🎯")
    print("Try to guess the number before time runs out!")
    print("You can type 'q' at any time to quit.\n")

    while True:
        # Get game parameters based on chosen difficulty
        computer_choice, range_text, min_range, max_range, time_limit = select_difficulty()

        if computer_choice is None:
            print("Goodbye! Thanks for playing!")
            break

        # Run the guessing game
        result = play_guessing_game(computer_choice, range_text, min_range, max_range, time_limit)
        if not result:
            break

        # Ask to play again
        if not ask_to_play_again():
            print("Goodbye! Thanks for playing!")
            break


if __name__ == "__main__":
    main()