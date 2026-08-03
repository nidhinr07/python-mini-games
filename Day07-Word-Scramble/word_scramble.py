import random

words = [
    "python",
    "computer",
    "keyboard",
    "developer",
    "programming",
    "function",
    "variable",
    "project"
]


def scramble_word(word):
    letters = list(word)
    random.shuffle(letters)
    return "".join(letters)


def main():
    print("========== WORD SCRAMBLE GAME ==========")

    score = 0

    while True:
        word = random.choice(words)
        scrambled = scramble_word(word)

        print("\nScrambled Word:", scrambled)

        guess = input("Guess the word (or type 'exit' to quit): ").strip().lower()

        if guess == "exit":
            break

        if guess == word:
            print("Correct!")
            score += 1
        else:
            print("Wrong!")
            print("Correct Word:", word)

    print("\n========== FINAL SCORE ==========")
    print("Your Score:", score)
    print("Thank you for playing!")


main()
