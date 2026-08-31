import random
from abc import ABC, abstractmethod


class Pirate(ABC):

    def __init__(self, name):
        self._name = name
        self._health = 100
        self._score = 0

    @abstractmethod
    def attack(self):
        pass

    def take_damage(self, damage):
        self._health -= damage

        if self._health < 0:
            self._health = 0

    def add_score(self, points):
        self._score += points

    def is_alive(self):
        return self._health > 0

    def get_name(self):
        return self._name

    def get_health(self):
        return self._health

    def get_score(self):
        return self._score


class PlayerPirate(Pirate):

    def attack(self):
        damage = random.randint(15, 25)
        print(f"You attacked for {damage} damage!")
        return damage


class ComputerPirate(Pirate):

    def attack(self):
        damage = random.randint(10, 25)
        print(f"Computer attacked for {damage} damage!")
        return damage


def show_status(player, computer):
    print("\n----------------------------")
    print(f"Your Health      : {player.get_health()}")
    print(f"Computer Health  : {computer.get_health()}")
    print(f"Your Score       : {player.get_score()}")
    print("----------------------------")


def search_treasure(player):
    result = random.choice(["treasure", "nothing", "trap"])

    if result == "treasure":
        points = random.randint(10, 30)
        player.add_score(points)
        print(f"You found treasure! +{points} points.")

    elif result == "trap":
        damage = random.randint(5, 15)
        player.take_damage(damage)
        print(f"You found a trap! You lost {damage} health.")

    else:
        print("You found nothing.")


def main():

    player = PlayerPirate("Player")
    computer = ComputerPirate("Computer")

    print("========== PIRATE TREASURE BATTLE ==========")
    print("Defeat the computer and collect treasure!")

    while player.is_alive() and computer.is_alive():

        show_status(player, computer)

        choice = input(
            "\nAttack / Search / Exit: "
        ).strip().lower()

        if choice == "exit":
            print("\nYou left the island.")
            break

        elif choice == "attack":

            damage = player.attack()
            computer.take_damage(damage)

        elif choice == "search":

            search_treasure(player)

        else:
            print("Invalid choice.")
            continue

        if not computer.is_alive():
            break

        damage = computer.attack()
        player.take_damage(damage)

    print("\n========== FINAL RESULT ==========")

    show_status(player, computer)

    if not computer.is_alive():
        print("You defeated the computer pirate!")
        print("You won the treasure!")

    elif not player.is_alive():
        print("The computer pirate defeated you!")

    else:
        print("You left the island.")


main()
