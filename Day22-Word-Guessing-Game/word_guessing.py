import random


words = [
    "python",
    "computer",
    "program",
    "keyboard",
    "developer",
    "internet"
]


def display_word(word, guessed_letters):
    result = ""

    for letter in word:
        if letter in guessed_letters:
            result += letter + " "
        else:
            result += "_ "

    return result


def play_game():
    word = random.choice(words)
    guessed_letters = []
    attempts = 6

    print("\n========== WORD GUESSING GAME ==========")

    while attempts > 0:

        print("\nWord:", display_word(word, guessed_letters))
        print("Attempts left:", attempts)

        guess = input("Guess a letter: ").strip().lower()

        if len(guess) != 1 or not guess.isalpha():
            print("Please enter one letter.")
            continue

        if guess in guessed_letters:
            print("You already guessed that letter.")
            continue

        guessed_letters.append(guess)

        if guess in word:
            print("Correct guess!")

        else:
            attempts -= 1
            print("Wrong guess!")

        if all(letter in guessed_letters for letter in word):
            print("\nYou guessed the word!")
            print("The word was:", word)
            return

    print("\nGame Over!")
    print("The word was:", word)


def main():

    while True:

        play_game()

        choice = input("\nPlay again? (yes/no): ").strip().lower()

        if choice != "yes":
            print("\nThanks for playing!")
            break


main()
