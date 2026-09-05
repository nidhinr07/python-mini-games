import random


def generate_number():
    digits = list("0123456789")
    random.shuffle(digits)
    return "".join(digits[:4])


def check_guess(secret, guess):
    bulls = 0
    cows = 0

    for i in range(4):
        if guess[i] == secret[i]:
            bulls += 1
        elif guess[i] in secret:
            cows += 1

    return bulls, cows


def main():

    print("========== BULLS AND COWS ==========")

    secret = generate_number()
    attempts = 0

    while True:

        guess = input("\nEnter a 4-digit number (or type 'exit'): ").strip()

        if guess.lower() == "exit":
            print("Game Over!")
            print("Secret Number:", secret)
            break

        if not guess.isdigit() or len(guess) != 4:
            print("Please enter exactly 4 digits.")
            continue

        attempts += 1

        bulls, cows = check_guess(secret, guess)

        if bulls == 4:
            print("\nCongratulations!")
            print("You guessed the number in", attempts, "attempts.")
            break

        print("Bulls:", bulls)
        print("Cows :", cows)


main()
