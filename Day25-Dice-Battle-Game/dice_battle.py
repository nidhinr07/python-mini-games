import random


def roll_dice():
    return random.randint(1, 6)


def display_score(player_score, computer_score):
    print("\n----------------------------")
    print("Your Score     :", player_score)
    print("Computer Score :", computer_score)
    print("----------------------------")


def main():
    player_score = 0
    computer_score = 0

    print("========== DICE BATTLE ==========")

    while True:

        display_score(player_score, computer_score)

        choice = input(
            "\nPress Enter to roll the dice or type 'exit': "
        ).strip().lower()

        if choice == "exit":
            break

        player_dice = roll_dice()
        computer_dice = roll_dice()

        print("\nYour Dice     :", player_dice)
        print("Computer Dice :", computer_dice)

        if player_dice > computer_dice:
            print("You win this round!")
            player_score += 1

        elif computer_dice > player_dice:
            print("Computer wins this round!")
            computer_score += 1

        else:
            print("It's a draw!")

    print("\n========== FINAL RESULT ==========")

    display_score(player_score, computer_score)

    if player_score > computer_score:
        print("You won the game!")

    elif computer_score > player_score:
        print("Computer won the game!")

    else:
        print("The game is a draw!")


main()
