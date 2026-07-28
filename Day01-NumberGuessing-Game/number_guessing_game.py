import random

number = random.randint(1, 100)
attempts_left = 7

print("Welcome to the Number Guessing Game")
print("Guess a number between 1 and 100")
print("You have 7 attempts")

while attempts_left > 0:
    guess = int(input("Enter your guess: "))

    attempts_left -= 1

    if guess == number:
        print("Congratulations! You guessed the correct number.")
        break

    elif guess < number:
        print("Your guess is too low.")

    else:
        print("Your guess is too high.")

    print("Attempts left:", attempts_left)

if attempts_left == 0:
    print("Game Over!")
    print("The correct number was:", number)
