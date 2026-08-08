import random


cards = [2, 3, 4, 5, 6, 7, 8, 9, 10,
         "J", "Q", "K", "A"]


def draw_card():
    return random.choice(cards)


def calculate_score(hand):
    score = 0
    aces = 0

    for card in hand:
        if card in ["J", "Q", "K"]:
            score += 10

        elif card == "A":
            score += 11
            aces += 1

        else:
            score += card

    while score > 21 and aces > 0:
        score -= 10
        aces -= 1

    return score


def display_hand(name, hand):
    print(f"{name}: {hand}")
    print("Score:", calculate_score(hand))


def play_game():

    player = [draw_card(), draw_card()]
    computer = [draw_card(), draw_card()]

    while True:

        print("\n----------------------------")
        display_hand("Your Hand", player)
        print("Computer's first card:", computer[0])
        print("----------------------------")

        player_score = calculate_score(player)

        if player_score > 21:
            print("\nYou went over 21!")
            print("Computer Wins!")
            return

        choice = input("\nDo you want another card? (yes/no): ").lower()

        if choice == "yes":
            player.append(draw_card())

        elif choice == "no":
            break

        else:
            print("Invalid choice. Please enter yes or no.")

    while calculate_score(computer) < 17:
        computer.append(draw_card())

    print("\n========== FINAL RESULT ==========")

    display_hand("Your Hand", player)
    print()
    display_hand("Computer Hand", computer)

    player_score = calculate_score(player)
    computer_score = calculate_score(computer)

    print("\nYour Score:", player_score)
    print("Computer Score:", computer_score)

    if computer_score > 21:
        print("Computer went over 21!")
        print("You Win!")

    elif player_score > computer_score:
        print("You Win!")

    elif player_score < computer_score:
        print("Computer Wins!")

    else:
        print("It's a Draw!")


def main():

    print("========== BLACKJACK ==========")

    while True:

        play_game()

        choice = input("\nPlay Again? (yes/no): ").lower()

        if choice != "yes":
            print("\nThank you for playing!")
            break


main()
