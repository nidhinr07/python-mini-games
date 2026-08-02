board = [" " for i in range(9)]


def display_board():
    print()
    print(f" {board[0]} | {board[1]} | {board[2]} ")
    print("---+---+---")
    print(f" {board[3]} | {board[4]} | {board[5]} ")
    print("---+---+---")
    print(f" {board[6]} | {board[7]} | {board[8]} ")
    print()


def check_winner(player):
    winning_positions = [
        [0, 1, 2],
        [3, 4, 5],
        [6, 7, 8],
        [0, 3, 6],
        [1, 4, 7],
        [2, 5, 8],
        [0, 4, 8],
        [2, 4, 6]
    ]

    for position in winning_positions:
        if (
            board[position[0]] == player and
            board[position[1]] == player and
            board[position[2]] == player
        ):
            return True

    return False


def board_full():
    return " " not in board


def play_game():
    current_player = "X"

    while True:
        display_board()

        try:
            choice = int(input(f"Player {current_player}, enter position (1-9): "))

            if choice < 1 or choice > 9:
                print("Please enter a number between 1 and 9.")
                continue

            if board[choice - 1] != " ":
                print("This position is already taken.")
                continue

            board[choice - 1] = current_player

            if check_winner(current_player):
                display_board()
                print(f"Player {current_player} wins!")
                break

            if board_full():
                display_board()
                print("It's a Draw!")
                break

            if current_player == "X":
                current_player = "O"
            else:
                current_player = "X"

        except ValueError:
            print("Please enter a valid number.")


def main():

    print("========== TIC TAC TOE ==========")

    while True:

        global board
        board = [" " for i in range(9)]

        play_game()

        choice = input("\nPlay Again? (yes/no): ").strip().lower()

        if choice != "yes":
            print("Thank you for playing!")
            break


main()
