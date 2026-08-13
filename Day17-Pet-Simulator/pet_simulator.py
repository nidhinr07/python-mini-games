class Pet:

    def __init__(self, name):
        self.name = name
        self.__hunger = 50
        self.__happiness = 50

    def feed(self):
        self.__hunger += 20

        if self.__hunger > 100:
            self.__hunger = 100

        print(f"{self.name} enjoyed the food!")

    def play(self):
        if self.__hunger <= 10:
            print(f"{self.name} is too hungry to play.")
            return

        self.__happiness += 20
        self.__hunger -= 10

        if self.__happiness > 100:
            self.__happiness = 100

        print(f"{self.name} had fun playing!")

    def status(self):
        print("\n----------------------------")
        print(f"Pet Name  : {self.name}")
        print(f"Hunger    : {self.__hunger}")
        print(f"Happiness : {self.__happiness}")
        print("----------------------------")

    def is_happy(self):
        return self.__happiness >= 50


def main():

    print("========== PET SIMULATOR ==========")

    name = input("Enter your pet's name: ").strip()

    if not name:
        print("Please enter a name.")
        return

    pet = Pet(name)

    while True:

        pet.status()

        print("\n1. Feed")
        print("2. Play")
        print("3. Check Happiness")
        print("4. Exit")

        choice = input("Enter your choice: ").strip()

        if choice == "1":
            pet.feed()

        elif choice == "2":
            pet.play()

        elif choice == "3":
            if pet.is_happy():
                print(f"{pet.name} is happy!")
            else:
                print(f"{pet.name} needs some attention.")

        elif choice == "4":
            print(f"\nGoodbye! Take care of {pet.name}.")
            break

        else:
            print("Invalid choice. Try again.")


main()
