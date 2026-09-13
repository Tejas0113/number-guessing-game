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


def main():
    """Main application entry point."""
    print("========================================")
    print("        NUMBER GUESSING GAME            ")
    print("========================================")
    
    difficulty_name, min_val, max_val, attempts = select_difficulty()
    secret_number = generate_number(min_val, max_val)
    print(f"Game configured! Secret number generated between {min_val} and {max_val}.")


if __name__ == "__main__":
    main()

