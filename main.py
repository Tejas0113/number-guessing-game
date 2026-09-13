"""
Number Guessing Game - Project 02
A beginner-friendly command-line number guessing game in Python.
"""

import random

# Difficulty configuration mapping: (name, min_val, max_val, max_attempts)
DIFFICULTIES = {
    "1": ("Easy", 1, 50, 10),
    "2": ("Medium", 1, 100, 7),
    "3": ("Hard", 1, 500, 5),
}


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
            name, min_val, max_val, attempts = DIFFICULTIES[choice]
            print(f"\nYou selected: {name.upper()}")
            print(f"Number range: {min_val} - {max_val}")
            print(f"Attempts available: {attempts}\n")
            return name, min_val, max_val, attempts
        
        print("\nInvalid choice. Please select 1, 2, or 3.\n")


def play_game():
    """Run one single session of the number guessing game."""
    name, min_val, max_val, max_attempts = select_difficulty()
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
            print(f"Attempts used: {attempts_used}\n")
            return True, attempts_used, max_attempts, name

        give_hint(guess, secret_number, attempts_used, max_attempts)

    print("========================================")
    print("             GAME OVER                  ")
    print("========================================")
    print("You used all your attempts.")
    print(f"The correct number was: {secret_number}\n")
    return False, attempts_used, max_attempts, name


def main():
    """Main application entry point."""
    print("========================================")
    print("        NUMBER GUESSING GAME            ")
    print("========================================")
    play_game()


if __name__ == "__main__":
    main()
