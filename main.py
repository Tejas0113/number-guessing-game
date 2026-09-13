"""
Number Guessing Game - Project 02
A beginner-friendly command-line number guessing game in Python.
"""

import random


def generate_number(min_value: int, max_value: int) -> int:
    """Generate a random target integer between min_value and max_value (inclusive)."""
    return random.randint(min_value, max_value)


def main():
    """Main application entry point."""
    print("========================================")
    print("        NUMBER GUESSING GAME            ")
    print("========================================")
    
    # Test random generation
    min_val, max_val = 1, 100
    secret_number = generate_number(min_val, max_val)
    print(f"I am thinking of a number between {min_val} and {max_val}.")
    print(f"[Debug] Random number generated: {secret_number}")


if __name__ == "__main__":
    main()

