import random


def draw_card():
    return random.randint(1, 13)


def card_name(card):
    cards = {
        1: "Ace",
        11: "Jack",
        12: "Queen",
        13: "King"
    }

    return cards.get(card, str(card))


def main():

    print("========== HIGH LOW CARD GAME ==========")

    score = 0

    current_card = draw_card()

    while True:

        print("\nCurrent Card:", card_name(current_card))

        choice = input("Will the next card be Higher or Lower? (h/l or exit): ").lower()

        if choice == "exit":
            break

        if choice not in ["h", "l"]:
            print("Invalid Choice!")
            continue

        next_card = draw_card()

        print("Next Card:", card_name(next_card))

        if (choice == "h" and next_card > current_card) or \
           (choice == "l" and next_card < current_card):

            print("Correct!")
            score += 1

        elif next_card == current_card:
            print("Same Card! No Points.")

        else:
            print("Wrong!")

        current_card = next_card

    print("\nFinal Score:", score)
    print("Thanks for Playing!")


main()
