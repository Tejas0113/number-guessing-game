# Number Guessing Game

A clean, beginner-friendly command-line Number Guessing Game built in pure Python. The game challenges players to guess a randomly generated number within a limited number of attempts across multiple difficulty levels, complete with real-time feedback, smart hints, score calculations, and persistent best-score tracking.

This project represents **Project 02** in my Python learning journey and GitHub portfolio.

---

## ?? Features

* **Random Number Generation**: Dynamically generates unique secret numbers each game using Python's built-in \andom\ module.
* **Three Difficulty Levels**: Choose between Easy (1–50), Medium (1–100), and Hard (1–500) modes.
* **Higher / Lower Hints**: Immediate feedback guiding the player closer to the secret number.
* **Smart Hints**: Unlocks contextual parity hints (EVEN / ODD) after consecutive incorrect attempts.
* **Intelligent Score System**: Rewards higher difficulty and fewer attempts with dynamic multipliers.
* **Persistent Best Score**: Stores and updates high scores locally in \scores.json\ across sessions.
* **Robust Input Validation**: Safely handles non-numeric input, floats, negative numbers, out-of-range guesses, empty inputs, and EOF signals without consuming attempts or crashing.
* **Replay & Navigation**: Interactive main menu and seamless replay workflow.

---

## ?? Game Difficulties

| Difficulty | Number Range | Attempts Allowed | Score Multiplier |
| :--------- | :----------- | :--------------- | :--------------- |
| **Easy**   | 1 – 50       | 10               | 1x               |
| **Medium** | 1 – 100      | 7                | 2x               |
| **Hard**   | 1 – 500      | 5                | 3x               |

---

## ??? Technologies Used

* **Language**: Python 3
* **Libraries**: Python Standard Library only (\andom\, \json\, \os\)
* **Environment**: Platform-independent CLI (Windows, macOS, Linux)

---

## ?? Project Structure

\\\	ext
number-guessing-game/
¦
+-- main.py              # Main application logic & game loop
+-- README.md            # Comprehensive project documentation
+-- requirements.txt     # Dependency definition (standard library only)
+-- .gitignore           # Git ignore file for Python cache and environments
+-- scores.json          # Persistent high-score data file
\\\

---

## ?? How to Run

1. **Clone the repository**:
   \\\ash
   git clone https://github.com/Tejas0113/number-guessing-game.git
   cd number-guessing-game
   \\\

2. **Run the application**:
   \\\ash
   python main.py
   \\\

---

## ?? How to Play

1. Run \python main.py\ to open the main menu.
2. Select **1. Play Game** and pick a difficulty (1, 2, or 3).
3. The computer generates a secret number within the chosen range.
4. Enter your guesses in the terminal.
5. Pay attention to the **Too low!** or **Too high!** hints, as well as the **Smart Hint** after 3 attempts.
6. Guess the number before your attempts run out to score points and set new high scores!

---

## ?? Example Gameplay

\\\	ext
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
\\\

---

## ?? Learning Outcomes

This project demonstrates core Python programming principles:

* **Variables & Data Types**: Storing strings, integers, tuples, and dictionaries.
* **Control Flow & Branching**: \if\, \elif\, \else\ statements for guess comparisons and menu dispatch.
* **Loops**: \while\ loops for the game cycle, replay prompts, and robust input validation.
* **Functions & Modularity**: Breaking code down into small, single-responsibility functions.
* **Randomness**: Generating pseudo-random numbers with \andom.randint()\.
* **Exception Handling**: Using \	ry-except\ blocks (\ValueError\, \json.JSONDecodeError\, \OSError\) for crash-proof CLI operation.
* **File I/O & JSON Serialization**: Reading from and writing to \scores.json\ safely.
* **Git & Version Control**: Building a realistic commit history through structured milestones.

---

## ?? License

This project is open-source and available under the [MIT License](LICENSE).
