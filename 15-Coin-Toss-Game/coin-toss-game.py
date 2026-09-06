import random


def toss_coin():
    return random.choice(["heads", "tails"])


def display_score(player_score, computer_score):
    print("\n----------------------------")
    print("Your Score     :", player_score)
    print("Computer Score :", computer_score)
    print("----------------------------")


def main():
    player_score = 0
    computer_score = 0

    print("========== COIN TOSS GAME ==========")

    while True:

        display_score(player_score, computer_score)

        choice = input(
            "\nChoose Heads or Tails "
            "(or type 'exit'): "
        ).strip().lower()

        if choice == "exit":
            break

        if choice not in ["heads", "tails"]:
            print("Invalid choice. Please choose heads or tails.")
            continue

        result = toss_coin()

        print("Coin:", result)

        if choice == result:
            print("You Win!")
            player_score += 1
        else:
            print("Computer Wins!")
            computer_score += 1

    print("\n========== FINAL RESULT ==========")

    display_score(player_score, computer_score)

    if player_score > computer_score:
        print("You won the game!")

    elif computer_score > player_score:
        print("Computer won the game!")

    else:
        print("The game is a draw!")


main()
