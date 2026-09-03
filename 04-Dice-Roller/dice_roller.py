import random


def roll_dice():
    return random.randint(1, 6)


def main():
    print("========== DICE ROLLER ==========")

    while True:
        choice = input("\nPress Enter to roll the dice or type 'exit' to quit: ").strip().lower()

        if choice == "exit":
            break

        print("You rolled:", roll_dice())

    print("\nThank you for playing!")


main()
