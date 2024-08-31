"""
Author: Mahnaz Ghassemi
Date created: 01,07,2024
Description: Number Guessing Game
"""

import random


def main():
    # loop for replaying the game
    while True:
        # Generate a random number between 1 and 100 for the computer's choice
        computer_choice: int = random.randint(1, 100)
        score: int = 100  # Initialize the score to 100

        while True:
            # Get user input (either a number or 'q' to quit)
            user_guess: str = input("Please enter your guess number (between 1 and 100) or 'q' to quit: ")
            
            # Check if the user input is a digit
            if user_guess.isdigit():
                user_guess: int = int(user_guess)  # Convert input to integer
                
                # Check if the guess is within the valid range
                if user_guess > 100 or user_guess < 1:
                    print("Your guess is out of range. Please choose a number between 1 and 100.")
                    continue
                
                # Compare the user's guess with the computer's choice
                elif user_guess > computer_choice:
                    print("It is much higher than my choice. Please try again.")
                    score -= 10  # Deduct 10 points for an incorrect guess
                    continue
                
                elif user_guess < computer_choice:
                    print("It is much lower than my choice. Please try again.")
                    score -= 10  # Deduct 10 points for an incorrect guess
                    continue
                
                elif user_guess == computer_choice:
                    print("You win!")
                    print(f"Your score is: {score}")
                    
                    # Ask the user if they want to play again
                    wanna_play: str = input("Would you like to play again? (yes/no): ").lower()
                
                # If the user wants to play again, restart the game
                if wanna_play == "yes":
                    print("Welcome back to the game!")
                    computer_choice = random.randint(1, 100)  # Reset the computer's choice
                    score = 100  # Reset the score
                    continue
                
                # If the user doesn't want to play again, exit the loop
                elif wanna_play == "no":
                    print("Thanks for playing. Goodbye!")
                    break
            
            # If the user input is not a digit, check if they want to quit
            if not user_guess.isdigit():
                if user_guess == "q":
                    print("Thanks for playing the game. Have a nice day!")
                    break
                else:
                    print("Invalid input, please try again.")
                    continue


if __name__ == "__main__":
    main()