import random


def show_status(health, food, score):
    print("\n----------------------------")
    print("Health :", health)
    print("Food   :", food)
    print("Score  :", score)
    print("----------------------------")


def main():
    health = 100
    food = 3
    score = 0

    print("========== ZOMBIE SURVIVAL ==========")
    print("Survive as long as possible!")
    print("You can search, eat, or exit.")

    while health > 0:

        show_status(health, food, score)

        choice = input(
            "\nSearch / Eat / Exit: "
        ).strip().lower()

        if choice == "exit":
            break

        elif choice == "eat":

            if food > 0:
                health += 20

                if health > 100:
                    health = 100

                food -= 1
                print("You ate food and recovered health.")

            else:
                print("You have no food!")

        elif choice == "search":

            event = random.choice(
                ["zombie", "food", "nothing", "weapon"]
            )

            if event == "zombie":
                damage = random.randint(10, 30)
                health -= damage

                print("A zombie attacked you!")
                print(f"You lost {damage} health.")

            elif event == "food":
                food += 1
                print("You found some food!")

            elif event == "weapon":
                points = random.randint(10, 30)
                score += points

                print("You found a weapon!")
                print(f"You gained {points} points.")

            else:
                print("You found nothing.")

        else:
            print("Invalid choice.")

    print("\n========== GAME OVER ==========")
    print("Final Health :", health)
    print("Final Score  :", score)

    if health <= 0:
        print("The zombies got you!")

    else:
        print("You escaped safely!")


main()
