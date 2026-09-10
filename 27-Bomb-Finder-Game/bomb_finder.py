import random


def create_board():
    board = list(range(1, 10))
    bomb = random.choice(board)
    return board, bomb


def display_board():
    print("\n-------------------")
    print(" 1 | 2 | 3 ")
    print("---+---+---")
    print(" 4 | 5 | 6 ")
    print("---+---+---")
    print(" 7 | 8 | 9 ")
    print("-------------------")


def main():
    score = 0
    board, bomb = create_board()
    selected = []

    print("========== BOMB FINDER ==========")
    print("Choose a box and avoid the hidden bomb!")
    print("There is only one bomb.")

    while True:

        display_board()

        print("\nScore:", score)

        choice = input(
            "Choose a box (1-9) or type 'exit': "
        ).strip().lower()

        if choice == "exit":
            print("\nYou left the game.")
            break

        if not choice.isdigit() or int(choice) not in board:
            print("Invalid choice. Choose a number from 1 to 9.")
            continue

        choice = int(choice)

        if choice in selected:
            print("You already selected this box.")
            continue

        selected.append(choice)

        if choice == bomb:
            print("\nBOOM!")
            print("You found the bomb!")
            print("Final Score:", score)
            break

        score += 10
        print("Safe box! +10 points.")

        if len(selected) == 8:
            print("\nYou found all the safe boxes!")
            print("You won the game!")
            print("Final Score:", score)
            break


main()
