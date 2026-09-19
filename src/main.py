import random
import time
from typing import Tuple


def select_difficulty() -> Tuple[
    int | None, str | None, int | None, int | None, int | None
]:
    while True:
        difficulty = input(
            "Choose difficulty: Easy, Medium, or Hard "
            "(or type 'q' to quit): "
        ).lower()

        if difficulty == "easy":
            return random.randint(1, 50), "1 to 50", 1, 50, 60
        elif difficulty == "medium":
            return random.randint(1, 100), "1 to 100", 1, 100, 45
        elif difficulty == "hard":
            return random.randint(1, 200), "1 to 200", 1, 200, 30
        elif difficulty == "q":
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
    attempts = 0
    start_time = time.time()

    while True:
        elapsed_time = time.time() - start_time
        time_left = max(0, time_limit - int(elapsed_time))

        if time_left == 0:
            print(
                f"Time's up! The correct number was {computer_choice}. "
                "You ran out of time!"
            )
            return False

        print(f"You have {time_left} seconds left.")
        user_guess = input(
            f"Guess a number between {range_text} "
            "or type 'q' to quit: "
        )

        if user_guess.lower() == "q":
            print("Exiting the game. Have a great day!")
            return False

        try:
            guess = int(user_guess)
        except ValueError:
            print(
                f"Invalid input. Please enter a number between "
                f"{min_range} and {max_range} or 'q' to quit."
            )
            continue

        attempts += 1

        if guess < min_range or guess > max_range:
            print(
                f"Out of range! Please choose a number between "
                f"{min_range} and {max_range}."
            )
        elif guess == computer_choice:
            print(
                f"Congratulations, you guessed the number "
                f"in {attempts} attempts!"
            )
            return True
        elif abs(guess - computer_choice) <= 10:
            print(
                f"You're very close! You guessed {guess}. "
                f"Try {'higher' if guess < computer_choice else 'lower'}."
            )
        elif guess < computer_choice:
            print(
                f"You guessed {guess}, which is too low! "
                "Try a higher number."
            )
        else:
            print(
                f"You guessed {guess}, which is too high! "
                "Try a lower number."
            )


def ask_to_play_again() -> bool:
    play_again = input("Do you want to play again? (yes/no): ").lower()
    return play_again == "yes"


def main() -> None:
    print("Welcome to the Random Number Guessing Game")
    print("Try to guess the number before time runs out!")
    print("You can type 'q' at any time to quit.\n")

    while True:
        (
            computer_choice,
            range_text,
            min_range,
            max_range,
            time_limit
        ) = select_difficulty()

        if computer_choice is None:
            print("Goodbye! Thanks for playing!")
            break

        result = play_guessing_game(
            computer_choice,
            range_text,
            min_range,
            max_range,
            time_limit
        )

        if not result:
            break

        if not ask_to_play_again():
            print("Goodbye! Thanks for playing!")
            break


if __name__ == "__main__":
    main()
