# Number Guessing Game - CLI Mini-Game

Can you outsmart the algorithm before your attempts hit zero?

Welcome to **Project 02** of my Python learning and GitHub portfolio roadmap! Building upon the foundations of the previous Smart Calculator project, this project introduces interactive gameplay loops, pseudo-random number generation, dynamic scoring mathematics, input validation shields, and persistent high-score tracking using pure standard Python.

---

## 1. Project Overview

Most introductory number guessing scripts run once and immediately terminate. This project is structured as a resilient, full-featured terminal application:

- **Random Number Engine**: Unbiased target generation powered by Python built-in `random.randint()`.
- **Adaptive Difficulty Tiers**: Three distinct difficulty modes with scaled ranges, attempt limits, and scoring multipliers.
- **Smart Parity Clues**: Automatically detects prolonged attempts and provides dynamic parity hints (Even vs. Odd) after 3 failed guesses.
- **Dynamic Score Multipliers**: A mathematical scoring system that rewards harder difficulties and fewer attempts:
  Score = Difficulty Multiplier * Remaining Attempts * 100
- **Persistent High Score**: Automatically stores and loads personal best scores from `scores.json`, with built-in recovery against corrupted or empty files.
- **Defensive Input Validation**: Safely handles non-numeric strings, decimal floats, negative numbers, out-of-range guesses, blank inputs, and keyboard interrupts without crashing or consuming attempts.
- **Seamless Replay Loop**: Continue playing multiple rounds or navigate back to the main menu without restarting the program.

---

## 2. Difficulty Modes and Mechanics

| Difficulty | Number Range | Attempts Allowed | Score Multiplier | Gameplay Style |
| :--- | :---: | :---: | :---: | :--- |
| **Easy** | 1 - 50 | 10 | 1x | Casual / Warm-up |
| **Medium** | 1 - 100 | 7 | 2x | Balanced Tactical Play |
| **Hard** | 1 - 500 | 5 | 3x | Advanced Binary-Search |

---

## 3. Step-by-Step Build Journey

This project was built incrementally using a clean Git workflow, where each milestone was tested and committed:

- **Milestone 1 - Project Setup**: Configured repository structure, `.gitignore`, initial `scores.json`, `requirements.txt`, and entry point.
- **Milestone 2 - Random Number Generation**: Integrated the `random` module with decoupled `generate_number()` function.
- **Milestone 3 - Difficulty Modes**: Added Easy, Medium, and Hard configurations with custom ranges and attempt limits.
- **Milestone 4 - Guessing Logic and Hints**: Implemented `check_guess()`, dynamic higher/lower feedback, and smart parity clues.
- **Milestone 5 - Scoring System**: Designed mathematical scoring formula and session score tracking.
- **Milestone 6 - Persistent Score Storage**: Added JSON serialization (`scores.json`) with safe exception handling (`OSError`, `json.JSONDecodeError`).
- **Milestone 7 - Replay and Game Navigation**: Built the interactive main menu, How to Play guide, and replay flow.
- **Milestone 8 - Input Validation**: Protected all input prompts against invalid types, empty strings, and EOF interrupts.
- **Milestone 9 - Polish and Usability**: Refined terminal layout, user messages, and clean documentation.

---

## 4. Project Structure

```text
number-guessing-game/
|
|-- main.py              # Main application logic and single-responsibility functions
|-- scores.json          # Persistent high-score JSON file
|-- requirements.txt     # Standard library dependencies (zero third-party packages)
|-- .gitignore           # Git ignore rules for Python artifacts
-- README.md            # Project documentation and user guide
```

---

## 5. Live Terminal Gameplay Example

```text
========================================
        NUMBER GUESSING GAME
========================================
1. Play Game
2. View Best Score
3. How to Play
4. Exit
========================================
Choose an option: 1

========================================
          SELECT DIFFICULTY
========================================
1. Easy   (Range: 1 - 50,  Attempts: 10)
2. Medium (Range: 1 - 100, Attempts: 7)
3. Hard   (Range: 1 - 500, Attempts: 5)
========================================
Choose difficulty (1-3): 2

You selected: MEDIUM
Number range: 1 - 100
Attempts available: 7

========================================
             GAME START
========================================
I am thinking of a number between 1 and 100.
You have 7 attempts.
Good luck!

Attempt 1 of 7 - Enter your guess: 50
Too high! Try a lower number.
Attempts remaining: 6

Attempt 2 of 7 - Enter your guess: 25
Too low! Try a higher number.
Attempts remaining: 5

Attempt 3 of 7 - Enter your guess: 37
Too high! Try a lower number.
Hint: The secret number is EVEN.
Attempts remaining: 4

Attempt 4 of 7 - Enter your guess: 32

========================================
              YOU WON!
========================================
Correct! You guessed the number.
Attempts used: 4
Score: 800

NEW BEST SCORE!
Previous Best: 0
New Best: 800

Do you want to play again? (y/n): n

Returning to main menu...
```

---

## 6. How to Run Locally

### Prerequisites
- Python 3.8 or higher installed on your system.

### Steps
1. **Clone the repository**:
   ```bash
   git clone https://github.com/Tejas0113/number-guessing-game.git
   ```

2. **Navigate into the project directory**:
   ```bash
   cd number-guessing-game
   ```

3. **Run the application**:
   ```bash
   python main.py
   ```

---

## 7. How to Play

1. Run `python main.py` to open the main menu.
2. Select **1. Play Game** and pick a difficulty level (1, 2, or 3).
3. The computer generates a secret number within the chosen range.
4. Enter your guess in the prompt.
5. Use the **Too low!** or **Too high!** clues, as well as the **Smart Parity Hint** after 3 attempts, to narrow down your next guess.
6. Guess correctly before running out of attempts to score points and set a new personal best!

---

## 8. Learning Outcomes

This project demonstrates core Python programming and software engineering fundamentals:

- **Modular Functions**: Single-responsibility functions with clear inputs and return values.
- **Control Flow and Logic**: Nested condition branching (`if-elif-else`) for guess comparison and menu handling.
- **Iteration and State**: `while` loops managing gameplay sessions, attempt counters, and replay cycles.
- **Defensive Exception Handling**: Protecting user inputs against `ValueError`, `json.JSONDecodeError`, and `OSError`.
- **JSON File Persistence**: Reading, validating, and writing persistent data locally.
- **Clean Code and CLI Design**: Readable snake_case identifiers, structured output headers, and clear user prompts.
- **Git Version Control**: Clean, chronological commit history covering every engineering milestone.

---

## 9. License

This project is open-source and available under the [MIT License](LICENSE).
