# ?? Number Guessing Game — The Mind-Reader CLI

> *Can you outsmart the algorithm before your attempts hit zero?*

Welcome to **Project 02** of my Python Mastery & Portfolio Journey! ??

Building on the foundations of my previous **Smart Calculator** project, this project levels up into interactive game theory, pseudo-random state generation, dynamic scoring mathematics, and resilient data persistence—all crafted in **pure Python** with zero external dependencies.

---

## ? What Makes This Project Special?

Most beginner number guessing games are simple scripts that run once and quit. This project is built like a **production-ready CLI mini-game**:

* ?? **Cryptic Random Number Engine**: Unbiased target generation powered by Python's andom module.
* ??? **Adaptive Difficulty Tiers**: From quick rounds to high-stakes number hunts across a 500-number span.
* ?? **Smart Parity Radar**: Stuck after multiple guesses? The system detects your struggle and drops dynamic parity hints (Even vs. Odd).
* ?? **Skill-Driven Score Multiplier**: Rewarding difficulty level and guess efficiency with a mathematical formula:
  \text{Score} = \text{Difficulty Multiplier} \times \text{Remaining Attempts} \times 100
* ?? **Session-Persistent Leaderboard**: Saves and loads your all-time high score to scores.json with self-healing corrupted JSON handling.
* ??? **Bulletproof Input Armor**: Enter letters, floats, negative numbers, blank inputs, or press Ctrl+C—the game will never crash, and invalid inputs never cost you an attempt!
* ?? **Seamless Game Loop**: Complete replay & menu system without needing to restart the Python process.

---

## ?? Difficulty Modes & Mechanics

| Mode | Range | Attempts | Multiplier | Challenge Level |
| :--- | :---: | :---: | :---: | :--- |
| ?? **Easy** | 1 – 50 | **10** | **1x** | Warm-up / Casual |
| ?? **Medium** | 1 – 100 | **7** | **2x** | Balanced Tactical Play |
| ?? **Hard** | 1 – 500 | **5** | **3x** | Binary-Search Masterclass |

---

## ??? Step-by-Step Build Journey (What Was Done)

This project was developed incrementally through **real engineering milestones** with full Git commit traceability:

`	ext
ba54e2f Initial project setup
    ¦   +-- Configured repository structure, .gitignore, scores.json, requirements.txt
86a2ee4 Add random number generation
    ¦   +-- Integrated random.randint() with decoupled generate_number() function
58a0c76 Add easy medium and hard difficulty modes
    ¦   +-- Implemented multi-tier configuration mapping and select_difficulty()
84814ff Add guessing logic and hints
    ¦   +-- Built check_guess(), dynamic higher/lower hints, and smart parity clues
d3da540 Add score calculation and best score
    ¦   +-- Implemented mathematical scoring system with difficulty multipliers
fc1aa20 Add persistent score storage
    ¦   +-- Added JSON serialization (scores.json) with error recovery
26e651b Add replay and game navigation
    ¦   +-- Created interactive menu, 'How to Play' guide, and replay loops
e333479 Improve input validation and error handling
    ¦   +-- Built input shields against ValueError, empty strings, and EOF interrupts
643facd Polish CLI experience and documentation
        +-- Enhanced visual layout, ANSI-style boxes, and comprehensive docs
`

---

## ?? Project Architecture

`	ext
number-guessing-game/
¦
+-- main.py              # Single-responsibility modular game engine
+-- scores.json          # Persistent JSON high-score record
+-- requirements.txt     # Dependency definition (Pure Standard Library)
+-- .gitignore           # Clean repository hygiene
+-- README.md            # Interactive documentation & project story
`

---

## ??? Live Terminal Walkthrough

Here is a glimpse of the game in action:

`	ext
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
I'm thinking of a number between 1 and 100.
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
?? Hint: The secret number is EVEN.
Attempts remaining: 4

Attempt 4 of 7 - Enter your guess: 32

========================================
              YOU WON!
========================================
Correct! You guessed the number.
Attempts used: 4
Score: 800

?? NEW BEST SCORE! ??
Previous Best: 0
New Best: 800

Do you want to play again? (y/n): n

Returning to main menu...
`

---

## ?? Quickstart Guide

### Prerequisites
* Python 3.8 or higher installed on your machine.

### Installation & Execution
`ash
# 1. Clone the repository
git clone https://github.com/Tejas0113/number-guessing-game.git

# 2. Navigate to the project directory
cd number-guessing-game

# 3. Launch the game
python main.py
`

---

## ?? Skills & Engineering Concepts Demonstrated

* ?? **Clean Modular Code**: Zero monolithic functions—each component has a single purpose.
* ?? **State Management**: Handling attempt counters, difficulty state, and target values across loops.
* ??? **Defensive Programming**: Handling empty inputs, invalid types (ValueError), and file exceptions (json.JSONDecodeError, OSError).
* ?? **Data Persistence**: Safe JSON reading and writing with fallback default states.
* ?? **Mathematical Logic**: Formulating score incentives based on difficulty and attempt conservation.
* ?? **Version Control Discipline**: Maintaining a clear, chronological Git history with meaningful milestone commits.

---

## ?? License & Author

Crafted with ?? by **[Tejas](https://github.com/Tejas0113)** as part of the Python Learning & Portfolio Roadmap.

Licensed under the **MIT License**.
