import random

words = ["python", "computer", "keyboard", "programming", "developer"]

word = random.choice(words)
guessed_letters = []
attempts = 6

print("========== HANGMAN ==========")

while attempts > 0:
    display = ""

    for letter in word:
        if letter in guessed_letters:
            display += letter + " "
        else:
            display += "_ "

    print("\nWord:", display)

    if "_" not in display:
        print("\nCongratulations! You guessed the word.")
        break

    guess = input("Enter a letter: ").lower()

    if len(guess) != 1 or not guess.isalpha():
        print("Please enter a single letter.")
        continue

    if guess in guessed_letters:
        print("You already guessed that letter.")
        continue

    guessed_letters.append(guess)

    if guess not in word:
        attempts -= 1
        print("Wrong guess!")
        print("Attempts left:", attempts)

else:
    print("\nGame Over!")
    print("The word was:", word)
