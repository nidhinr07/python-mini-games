import random


class Animal:

    def __init__(self, name):
        self.name = name
        self.position = 0

    def move(self):
        self.position += random.randint(1, 5)


class Rabbit(Animal):

    def move(self):
        self.position += random.randint(2, 6)


class Turtle(Animal):

    def move(self):
        self.position += random.randint(1, 3)


class Cheetah(Animal):

    def move(self):
        self.position += random.randint(3, 8)


def display_race(animals):
    print("\n========== RACE ==========")

    for animal in animals:
        print(f"{animal.name:<10} {'-' * animal.position}>")


def main():

    print("========== ANIMAL RACE ==========")
    print("First animal to reach 30 wins!")

    animals = [
        Rabbit("Rabbit"),
        Turtle("Turtle"),
        Cheetah("Cheetah")
    ]

    while True:

        for animal in animals:
            animal.move()

            if animal.position >= 30:
                display_race(animals)
                print(f"\n{animal.name} wins the race!")
                return

        display_race(animals)

        input("\nPress Enter for next round...")


main()
