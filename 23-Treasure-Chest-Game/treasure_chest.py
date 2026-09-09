import random


def create_chests():
    return {
        1: random.choice(["gold", "empty", "trap"]),
        2: random.choice(["gold", "empty", "trap"]),
        3: random.choice(["gold", "empty", "trap"])
    }


def open_chest(chests, choice):
    result = chests[choice]

    if result == "gold":
        points = random.randint(10, 50)
        print(f"\nYou found gold! +{points} points")
        return points

    elif result == "trap":
        print("\nOh no! You found a trap!")
        return -10

    else:
        print("\nThe chest is empty.")
        return 0


def main():
    score = 0

    print("========== TREASURE CHEST ==========")
    print("Choose a chest and try to find the treasure.")

    while True:

        chests = create_chests()

        print("\n----------------------------")
        print("Chest 1")
        print("Chest 2")
        print("Chest 3")
        print("Score:", score)
        print("----------------------------")

        choice = input(
            "Choose a chest (1-3) or type 'exit': "
        ).strip().lower()

        if choice == "exit":
            break

        if choice not in ["1", "2", "3"]:
            print("Invalid choice. Try again.")
            continue

        score += open_chest(chests, int(choice))

    print("\n========== GAME OVER ==========")
    print("Final Score:", score)

    if score > 0:
        print("Good job!")

    elif score == 0:
        print("You didn't find any treasure.")

    else:
        print("The traps got you!")


main()
