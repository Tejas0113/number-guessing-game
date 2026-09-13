# Number Guessing Game

A clean, beginner-friendly command-line Number Guessing Game written in pure Python. The player tries to guess a randomly generated secret number within a limited number of attempts based on the selected difficulty level.

## Features

* Random number generation
* Easy / Medium / Hard difficulty
* Limited attempts
* Higher / Lower hints
* Smart hints
* Score system
* Best score tracking
* Replay functionality
* Input validation
* JSON score persistence

## Difficulty

| Difficulty | Range | Attempts |
| ---------- | ----- | -------- |
| Easy       | 1–50  | 10       |
| Medium     | 1–100 | 7        |
| Hard       | 1–500 | 5        |

## Technologies

* Python 3
* \andom\
* \json\
* Python Standard Library

## How to Run

\\\ash
python main.py
\\\

## How to Play

1. Choose a difficulty level (Easy, Medium, or Hard).
2. The computer randomly picks a secret number within the difficulty range.
3. Type your guess in the terminal.
4. Use the "Higher" or "Lower" feedback and smart hints to adjust your guesses.
5. Guess the number before running out of attempts to score points!
6. Try to beat your personal best score stored locally.

## Learning Outcomes

This project demonstrates foundational Python programming and software design concepts:

* **Variables & Types**: Managing game parameters, attempts, ranges, and user inputs.
* **Functions**: Modular design with single-responsibility functions.
* **Conditions & Logic**: Guiding gameplay through if-elif-else branching.
* **Loops**: Game state loops and continuous replay loops.
* **Random Module**: Generating unbiased pseudo-random target numbers.
* **Input Validation**: Handling non-numeric values, out-of-range guesses, and empty inputs gracefully.
* **File Handling & JSON**: Reading and persisting high scores across sessions.
* **Git & GitHub**: Structured version control workflow with meaningful milestone commits.
