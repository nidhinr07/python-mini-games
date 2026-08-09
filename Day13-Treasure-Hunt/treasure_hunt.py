import random


def create_board():
    board = []

    for i in range(9):
        board.append("□")

    return board


def display_board(board):
    print("\n")

    for i in range(0, 9, 3):
        print(" | ".join(board[i:i + 3]))
        if i < 6:
            print("--+---+--")


def main():
    print("========== TREASURE HUNT ==========")
    print("Find the hidden treasure!")
    print("Choose a position from 1 to 9.")

    while True:

        board = create_board()
        treasure = random.randint(0, 8)
        attempts = 3

        while attempts > 0:

            display_board(board)

            choice = input(
                f"\nChoose a position (1-9) "
                f"or type 'exit': "
            ).strip().lower()

            if choice == "exit":
                print("\nThanks for playing!")
                return

            if not choice.isdigit():
                print("Please enter a number from 1 to 9.")
                continue

            position = int(choice)

            if position < 1 or position > 9:
                print("Please choose a number from 1 to 9.")
                continue

            index = position - 1

            if board[index] != "□":
                print("You already checked this position.")
                continue

            if index == treasure:
                board[index] = "T"
                display_board(board)
                print("\nYou found the treasure!")
                break

            board[index] = "X"
            attempts -= 1

            print("No treasure here!")
            print("Attempts left:", attempts)

        else:
            board[treasure] = "T"
            display_board(board)
            print("\nYou couldn't find the treasure.")
            print("The treasure was at position:", treasure + 1)

        play_again = input("\nPlay Again? (yes/no): ").strip().lower()

        if play_again != "yes":
            print("\nThanks for playing!")
            break


main()
