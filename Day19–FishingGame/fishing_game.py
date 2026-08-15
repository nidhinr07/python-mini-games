import random


class FishingGame:

    def __init__(self):
        self.score = 0
        self.casts = 5

    def cast_line(self):
        result = random.choice(["small", "medium", "large", "nothing"])

        if result == "small":
            print("You caught a small fish!")
            self.score += 10

        elif result == "medium":
            print("You caught a medium fish!")
            self.score += 20

        elif result == "large":
            print("You caught a large fish!")
            self.score += 50

        else:
            print("Nothing! The fish got away.")

        self.casts -= 1

    def show_status(self):
        print("\n----------------------------")
        print("Casts Left :", self.casts)
        print("Score      :", self.score)
        print("----------------------------")


def main():

    print("========== FISHING GAME ==========")
    print("You have 5 casts to catch fish.")
    print("Try to get the highest score!")

    game = FishingGame()

    while game.casts > 0:

        game.show_status()

        choice = input(
            "\nPress Enter to cast or type 'exit': "
        ).strip().lower()

        if choice == "exit":
            break

        game.cast_line()

    print("\n========== GAME OVER ==========")
    print("Final Score:", game.score)

    if game.score >= 100:
        print("Great job! Excellent catch!")

    elif game.score >= 50:
        print("Good job!")

    else:
        print("Better luck next time!")


main()
