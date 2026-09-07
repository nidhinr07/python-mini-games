import random


class Player:

    def __init__(self, name):
        self.name = name
        self.health = 100
        self.score = 0

    def take_damage(self, damage):
        self.health -= damage

        if self.health < 0:
            self.health = 0

    def add_score(self, points):
        self.score += points

    def is_alive(self):
        return self.health > 0

    def show_status(self):
        print("\n----------------------------")
        print(f"Player : {self.name}")
        print(f"Health : {self.health}")
        print(f"Score  : {self.score}")
        print("----------------------------")


class Dungeon:

    def __init__(self):
        self.rooms = ["trap", "treasure", "empty", "exit"]
        self.current_room = 1

    def enter_room(self):
        return random.choice(self.rooms)


def main():

    print("========== DUNGEON ESCAPE ==========")

    name = input("Enter your name: ").strip()

    if not name:
        print("Please enter a name.")
        return

    player = Player(name)
    dungeon = Dungeon()

    print("\nYou entered the dungeon.")
    print("Find the exit before you lose all your health.")

    while player.is_alive():

        player.show_status()

        choice = input(
            "\nEnter the dungeon? (yes/exit): "
        ).strip().lower()

        if choice == "exit":
            print("\nYou left the dungeon.")
            break

        if choice != "yes":
            print("Invalid choice.")
            continue

        room = dungeon.enter_room()

        print("\nYou entered a new room...")

        if room == "trap":

            damage = random.randint(10, 30)

            print("You stepped on a trap!")
            print(f"You lost {damage} health.")

            player.take_damage(damage)

        elif room == "treasure":

            points = random.randint(10, 30)

            print("You found a treasure!")
            print(f"You gained {points} points.")

            player.add_score(points)

        elif room == "empty":

            print("This room is empty.")

        elif room == "exit":

            print("\nYou found the exit!")
            print("Congratulations! You escaped the dungeon.")
            player.add_score(50)
            break

    print("\n========== GAME OVER ==========")
    player.show_status()

    if not player.is_alive():
        print("You ran out of health!")
        print("The dungeon defeated you.")

    print(f"\nFinal Score: {player.score}")


main()
