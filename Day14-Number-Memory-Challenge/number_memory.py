import random
import time


def generate_number(length):
    number = ""

    for i in range(length):
        number += str(random.randint(0, 9))

    return number


def main():
    print("========== NUMBER MEMORY CHALLENGE ==========")

    level = 1
    length = 3

    while True:

        print("\nLevel:", level)

        number = generate_number(length)

        print("Remember this number:")
        print(number)

        time.sleep(3)

        print("\n" * 30)

        answer = input(
            "Enter the number you remember "
            "(or type 'exit'): "
        ).strip()

        if answer.lower() == "exit":
            break

        if answer == number:
            print("Correct!")
            level += 1
            length += 1

        else:
            print("Wrong!")
            print("The correct number was:", number)
            print("You reached Level:", level)
            break

    print("\nThanks for playing!")


main()
