# Rock, Paper, Scissors Game

## Overview

This project is a console-based implementation of the classic **Rock, Paper, Scissors** game using Python.

The player competes against the computer, which randomly selects its move each round. The game continues until the player enters **`exit`**, allowing multiple rounds to be played in a single session.

At the end of the game, the final scores are displayed and the overall winner is announced.

---

## Game Rules

* Rock beats Scissors
* Paper beats Rock
* Scissors beats Paper
* If both players choose the same option, the round ends in a draw.

---

## Features

* Play unlimited rounds until you choose to exit.
* Random computer choice using Python's `random` module.
* Live score tracking for both the player and the computer.
* Final winner announcement.
* Handles invalid user input.
* Organized using Python functions for better readability.

---

## Concepts Practiced

* Functions
* Tuples
* Variables
* User Input
* Conditional Statements (`if`, `elif`, `else`)
* `while` Loop
* `break` and `continue`
* Random Module

---

## Project Structure

```text
Day-02-Rock-Paper-Scissors/
│
├── rock_paper_scissors.py
└── README.md
```

---

## How to Run

```bash
python rock_paper_scissors.py
```

---

## Sample Gameplay

```text
>>>>>>>>>>>>> LET'S START THE GAME <<<<<<<<<<<<<

----------------------------
Your Score     : 0
Computer Score : 0
----------------------------

Enter Rock, Paper, Scissors or Exit: rock
Computer Choice: scissors
You Win!

Enter Rock, Paper, Scissors or Exit: exit

========== FINAL RESULT ==========

----------------------------
Your Score     : 1
Computer Score : 0
----------------------------

Congratulations! You Won the Game.
```

---

## Difficulty

**Beginner to Intermediate**

This project is a great way to practice functions, loops, conditional logic, score tracking, user input handling, and building an interactive command-line application.
