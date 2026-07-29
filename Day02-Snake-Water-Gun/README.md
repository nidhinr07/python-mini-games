# Snake, Water, Gun Game

## Overview

This project is a console-based implementation of the classic **Snake, Water, Gun** game using Python.

The player competes against the computer, which randomly selects its move each round. The game continues until the player enters **`exit`**, allowing multiple rounds to be played in a single session.

At the end of the game, the final scores are displayed and the overall winner is announced.

---

## Game Rules

* Snake beats Water
* Water beats Gun
* Gun beats Snake
* If both players choose the same option, the round ends in a draw.

---

## Features

* Play unlimited rounds until you choose to exit.
* Random computer moves.
* Real-time score tracking.
* Final winner announcement.
* Input validation for invalid choices.
* Organized using Python functions.

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
Day-02-Snake-Water-Gun/
│
├── snake_water_gun.py
└── README.md
```

---

## How to Run

```bash
python snake_water_gun.py
```

---

## Sample Gameplay

```text
>>>>>>>>>>>>> LET'S START THE GAME <<<<<<<<<<<<<

Your Score     : 0
Computer Score : 0

Enter Snake, Water, Gun or Exit: snake

Computer Choice: water

You Win!

Enter Snake, Water, Gun or Exit: exit

========== FINAL RESULT ==========

Your Score     : 1
Computer Score : 0

Congratulations! You Won the Game.
```

---

## Difficulty

**Beginner to Intermediate**

This project is a great way to practice loops, functions, conditional logic, score tracking, and building an interactive command-line application.
