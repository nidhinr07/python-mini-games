from abc import ABC, abstractmethod
import random


class Character(ABC):

    def __init__(self, name, health):
        self.name = name
        self.__health = health

    def get_health(self):
        return self.__health

    def take_damage(self, damage):
        self.__health -= damage

        if self.__health < 0:
            self.__health = 0

    def is_alive(self):
        return self.__health > 0

    @abstractmethod
    def attack(self, enemy):
        pass


class Warrior(Character):

    def attack(self, enemy):
        damage = random.randint(10, 20)
        enemy.take_damage(damage)

        print(f"{self.name} attacks with a sword!")
        print(f"Damage: {damage}")


class Mage(Character):

    def attack(self, enemy):
        damage = random.randint(8, 25)
        enemy.take_damage(damage)

        print(f"{self.name} attacks with magic!")
        print(f"Damage: {damage}")


class Monster(Character):

    def attack(self, enemy):
        damage = random.randint(5, 15)
        enemy.take_damage(damage)

        print(f"{self.name} attacks!")
        print(f"Damage: {damage}")


def display_status(player, monster):
    print("\n----------------------------")
    print(f"{player.name} Health   : {player.get_health()}")
    print(f"{monster.name} Health : {monster.get_health()}")
    print("----------------------------")


def main():

    print("========== MONSTER BATTLE ==========")

    print("\nChoose your character:")
    print("1. Warrior")
    print("2. Mage")

    choice = input("Enter your choice: ")

    if choice == "1":
        player = Warrior("Warrior", 100)

    elif choice == "2":
        player = Mage("Mage", 100)

    else:
        print("Invalid choice.")
        return

    monster = Monster("Monster", 100)

    print(f"\n{player.name} vs {monster.name}")
    print("Battle begins!")

    while player.is_alive() and monster.is_alive():

        display_status(player, monster)

        print("\n1. Attack")
        print("2. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":

            player.attack(monster)

            if not monster.is_alive():
                break

            monster.attack(player)

        elif choice == "2":
            print("You left the battle.")
            return

        else:
            print("Invalid choice.")

    print("\n========== BATTLE RESULT ==========")

    if player.is_alive():
        print("You won the battle!")

    else:
        print("Monster won the battle!")


main()
