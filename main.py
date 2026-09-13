"""
Number Guessing Game - Project 02
A beginner-friendly command-line number guessing game in Python.
"""

import json
import os
import random

# Score persistence file path
SCORE_FILE = "scores.json"

# Difficulty configuration mapping: (name, min_val, max_val, max_attempts, multiplier)
DIFFICULTIES = {
    "1": ("Easy", 1, 50, 10, 1),
    "2": ("Medium", 1, 100, 7, 2),
    "3": ("Hard", 1, 500, 5, 3),
}

# Base score constant for clean score calculation
BASE_SCORE = 100


def load_best_score() -> int:
    """
    Load the best score from the local JSON file.
    Safely handles missing, empty, or corrupted JSON files.
    """
    if not os.path.exists(SCORE_FILE):
        return 0

    try:
        with open(SCORE_FILE, "r", encoding="utf-8") as file:
            data = json.load(file)
            return int(data.get("best_score", 0))
    except (json.JSONDecodeError, ValueError, OSError, TypeError):
        return 0


def save_best_score(score: int) -> bool:
    """
    Save the new best score to scores.json safely.
    Returns True if save was successful, False otherwise.
    """
    try:
        with open(SCORE_FILE, "w", encoding="utf-8") as file:
            json.dump({"best_score": score}, file, indent=4)
        return True
    except OSError:
        return False


def generate_number(min_value: int, max_value: int) -> int:
    """Generate a random target integer between min_value and max_value (inclusive)."""
    return random.randint(min_value, max_value)


def check_guess(guess: int, target: int) -> str:
    """Compare guess to target and return 'too_low', 'too_high', or 'correct'."""
    if guess < target:
        return "too_low"
    elif guess > target:
        return "too_high"
    else:
        return "correct"


def give_hint(guess: int, target: int, attempts_used: int, max_attempts: int):
    """Provide helpful feedback and smart hints to the player."""
    result = check_guess(guess, target)
    remaining = max_attempts - attempts_used

    if result == "too_low":
        print("Too low! Try a higher number.")
    elif result == "too_high":
        print("Too high! Try a lower number.")

    # Smart hint after multiple failed attempts
    if attempts_used >= 3 and remaining > 0:
        if target % 2 == 0:
            print("?? Hint: The secret number is EVEN.")
        else:
            print("?? Hint: The secret number is ODD.")

    if remaining > 0 and result != "correct":
        print(f"Attempts remaining: {remaining}\n")


def calculate_score(attempts_used: int, max_attempts: int, multiplier: int) -> int:
    """
    Calculate game score based on difficulty and remaining attempts.
    
    Formula:
        remaining_attempts = max_attempts - attempts_used + 1
        score = multiplier * remaining_attempts * BASE_SCORE
    """
    remaining_attempts = max_attempts - attempts_used + 1
    score = multiplier * remaining_attempts * BASE_SCORE
    return max(0, score)


def select_difficulty():
    """Prompt the user to select a game difficulty and return the configuration tuple."""
    while True:
        print("========================================")
        print("          SELECT DIFFICULTY             ")
        print("========================================")
        print("1. Easy   (Range: 1 - 50,  Attempts: 10)")
        print("2. Medium (Range: 1 - 100, Attempts: 7)")
        print("3. Hard   (Range: 1 - 500, Attempts: 5)")
        print("========================================")
        
        choice = input("Choose difficulty (1-3): ").strip()
        if choice in DIFFICULTIES:
            name, min_val, max_val, attempts, multiplier = DIFFICULTIES[choice]
            print(f"\nYou selected: {name.upper()}")
            print(f"Number range: {min_val} - {max_val}")
            print(f"Attempts available: {attempts}\n")
            return name, min_val, max_val, attempts, multiplier
        
        print("\nInvalid choice. Please select 1, 2, or 3.\n")


def play_game():
    """Run one single session of the number guessing game and update best score."""
    name, min_val, max_val, max_attempts, multiplier = select_difficulty()
    secret_number = generate_number(min_val, max_val)

    print("========================================")
    print("             GAME START                 ")
    print("========================================")
    print(f"I'm thinking of a number between {min_val} and {max_val}.")
    print(f"You have {max_attempts} attempts.")
    print("Good luck!\n")

    attempts_used = 0

    while attempts_used < max_attempts:
        user_input = input(f"Attempt {attempts_used + 1} of {max_attempts} - Enter your guess: ").strip()

        try:
            guess = int(user_input)
        except ValueError:
            print("Invalid input. Please enter a whole number.\n")
            continue

        if guess < min_val or guess > max_val:
            print(f"Please enter a number between {min_val} and {max_val}.\n")
            continue

        attempts_used += 1
        result = check_guess(guess, secret_number)

        if result == "correct":
            print("\n========================================")
            print("              YOU WON!                  ")
            print("========================================")
            print("Correct! You guessed the number.")
            print(f"Attempts used: {attempts_used}")
            
            score = calculate_score(attempts_used, max_attempts, multiplier)
            print(f"Score: {score}")

            current_best = load_best_score()
            if score > current_best:
                print("\n?? NEW BEST SCORE! ??")
                print(f"Previous Best: {current_best}")
                print(f"New Best: {score}")
                save_best_score(score)
            print()
            return True, score

        give_hint(guess, secret_number, attempts_used, max_attempts)

    print("========================================")
    print("             GAME OVER                  ")
    print("========================================")
    print("You used all your attempts.")
    print(f"The correct number was: {secret_number}")
    print("Score: 0\n")
    return False, 0


def main():
    """Main application entry point."""
    print("========================================")
    print("        NUMBER GUESSING GAME            ")
    print("========================================")
    play_game()


if __name__ == "__main__":
    main()
