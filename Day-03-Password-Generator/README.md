# Password Generator

## Overview

This project is a simple command-line Password Generator built using Python.

The program allows the user to generate a random password by entering the desired password length. It creates a password using a combination of uppercase letters, lowercase letters, numbers, and special characters.

The program continues generating passwords until the user types **`exit`**.

---

## Features

* Generate passwords of any length.
* Includes uppercase and lowercase letters.
* Includes numbers and special characters.
* Generates a different password every time.
* Allows multiple password generations in a single session.
* Handles invalid user input.

---

## Concepts Practiced

* Functions
* Strings
* Loops
* User Input
* Conditional Statements (`if`, `else`)
* `while` Loop
* `break`
* `continue`
* `random` Module
* `string` Module

---

## Project Structure

```text
Day-03-Password-Generator/
│
├── password_generator.py
└── README.md
```

---

## How to Run

```bash
python password_generator.py
```

---

## Sample Output

```text
========== PASSWORD GENERATOR ==========

Enter password length (or type 'exit' to quit): 10

Generated Password: A@7m#2Qx!P

Enter password length (or type 'exit' to quit): exit

Thank you for using Password Generator.
```

---

## Difficulty

**Beginner to Intermediate**

This project is a good way to practice working with strings, loops, functions, and Python's built-in `random` and `string` modules while creating a useful command-line application.
