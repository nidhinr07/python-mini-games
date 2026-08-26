import random


def catch_fish():
    return random.randint(0, 5)


def show_score(player_score, computer_score):
    print("\n----------------------------")
    print(f"Your Fish     : {player_score}")
    print(f"Computer Fish : {computer_score}")
    print("----------------------------")


def main():
    player_score = 0
    computer_score = 0
    round_number = 1

    print("========== FISHING COMPETITION ==========")
    print("Catch more fish than the computer!")
    print("There are 5 rounds.")

    while round_number <= 5:

        print(f"\n========== ROUND {round_number} ==========")

        input("Press Enter to cast your fishing line...")

        player_fish = catch_fish()
        computer_fish = catch_fish()

        print(f"\nYou caught {player_fish} fish!")
        print(f"Computer caught {computer_fish} fish!")

        player_score += player_fish
        computer_score += computer_fish

        round_number += 1

    print("\n========== FINAL RESULT ==========")

    show_score(player_score, computer_score)

    if player_score > computer_score:
        print("You won the fishing competition!")

    elif computer_score > player_score:
        print("Computer won the fishing competition!")

    else:
        print("The competition ended in a draw!")


main()
