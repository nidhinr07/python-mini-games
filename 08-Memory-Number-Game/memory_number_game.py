import random
import time


def generate_numbers():
    numbers = []

    for i in range(5):
        numbers.append(random.randint(1, 99))

    return numbers


def main():

    print("========== MEMORY NUMBER GAME ==========")

    while True:

        numbers = generate_numbers()

        print("\nRemember these numbers:")

        print(numbers)

        time.sleep(5)

        print("\n" * 40)

        answer = input("Enter the numbers separated by spaces (or type 'exit'): ").strip()

        if answer.lower() == "exit":
            break

        user_numbers = answer.split()

        correct = True

        if len(user_numbers) != len(numbers):
            correct = False
        else:
            for i in range(len(numbers)):
                if user_numbers[i] != str(numbers[i]):
                    correct = False
                    break

        if correct:
            print("Correct! Great Memory.")
        else:
            print("Wrong!")
            print("Correct Numbers:", numbers)

        play = input("\nPlay Again? (yes/no): ").lower()

        if play != "yes":
            break

    print("\nThank you for playing!")


main()
