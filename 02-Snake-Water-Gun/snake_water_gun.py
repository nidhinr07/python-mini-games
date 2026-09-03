import random

options = ("snake", "water", "gun")


def computer_choice():
    return random.choice(options)


def check_winner(user, computer):
    if user == computer:
        return "draw"

    elif (user == "snake" and computer == "water") or \
         (user == "water" and computer == "gun") or \
         (user == "gun" and computer == "snake"):
        return "user"

    else:
        return "computer"


def display_score(user_score, computer_score):
    print("\n----------------------------")
    print(f"Your Score     : {user_score}")
    print(f"Computer Score : {computer_score}")
    print("----------------------------")


def main():
    user_score = 0
    computer_score = 0

    print(">>>>>>>>>>>>> LET'S START THE GAME <<<<<<<<<<<<<")

    while True:
        display_score(user_score, computer_score)

        user = input("Enter Snake, Water, Gun or Exit: ").strip().lower()

        if user == "exit":
            break

        if user not in options:
            print("Invalid Choice! Try Again.")
            continue

        computer = computer_choice()

        print("Computer Choice:", computer)

        result = check_winner(user, computer)

        if result == "draw":
            print("It's a Draw!")

        elif result == "user":
            user_score += 1
            print("🎉 You Win!")

        else:
            computer_score += 1
            print("💻 Computer Wins!")

    print("\n========== FINAL RESULT ==========")
    display_score(user_score, computer_score)

    if user_score > computer_score:
        print("🏆 Congratulations! You Won the Game.")

    elif computer_score > user_score:
        print("💻 Computer Won the Game.")

    else:
        print("🤝 Match Draw!")


main()
