import random


class Car:

    def __init__(self, name):
        self.name = name
        self.position = 0

    def move(self):
        self.position += random.randint(1, 6)


def show_race(player, computer):
    print("\n----------------------------")
    print(f"{player.name:<10} {'-' * player.position}>")
    print(f"{computer.name:<10} {'-' * computer.position}>")
    print("----------------------------")


def main():

    print("========== RACING CAR GAME ==========")
    print("First car to reach 30 wins!")

    player = Car("You")
    computer = Car("Computer")

    while True:

        input("\nPress Enter to start the next round...")

        player.move()
        computer.move()

        show_race(player, computer)

        if player.position >= 30:
            print("\nYou won the race!")
            break

        if computer.position >= 30:
            print("\nComputer won the race!")
            break


main()
