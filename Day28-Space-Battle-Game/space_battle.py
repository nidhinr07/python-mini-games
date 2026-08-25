import random


def show_status(player_health, enemy_health):
    print("\n----------------------------")
    print(f"Your Health   : {player_health}")
    print(f"Enemy Health  : {enemy_health}")
    print("----------------------------")


def player_attack():
    damage = random.randint(10, 25)
    print(f"You attacked the enemy for {damage} damage!")
    return damage


def enemy_attack():
    damage = random.randint(5, 20)
    print(f"The enemy attacked you for {damage} damage!")
    return damage


def main():
    player_health = 100
    enemy_health = 100

    print("========== SPACE BATTLE ==========")
    print("Defeat the enemy spaceship!")

    while player_health > 0 and enemy_health > 0:

        show_status(player_health, enemy_health)

        choice = input(
            "\nAttack / Heal / Exit: "
        ).strip().lower()

        if choice == "exit":
            print("\nYou escaped from the battle.")
            break

        elif choice == "attack":
            damage = player_attack()
            enemy_health -= damage

        elif choice == "heal":
            heal = random.randint(10, 20)
            player_health += heal

            if player_health > 100:
                player_health = 100

            print(f"You repaired your spaceship by {heal} health.")

        else:
            print("Invalid choice.")
            continue

        if enemy_health <= 0:
            break

        damage = enemy_attack()
        player_health -= damage

    print("\n========== FINAL RESULT ==========")

    if enemy_health <= 0:
        print("You destroyed the enemy spaceship!")
        print("You won!")

    elif player_health <= 0:
        print("Your spaceship was destroyed!")
        print("Enemy won!")

    else:
        print("Battle ended.")

    print("\nYour Health  :", max(player_health, 0))
    print("Enemy Health :", max(enemy_health, 0))


main()
