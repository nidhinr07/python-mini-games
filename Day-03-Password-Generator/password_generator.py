import random
import string


def generate_password(length):
    characters = (
        string.ascii_letters +
        string.digits +
        string.punctuation
    )

    password = ""

    for i in range(length):
        password += random.choice(characters)

    return password


def main():
    print("========== PASSWORD GENERATOR ==========")

    while True:
        length = input("\nEnter password length (or type 'exit' to quit): ").strip().lower()

        if length == "exit":
            print("\nThank you for using Password Generator.")
            break

        if not length.isdigit():
            print("Please enter a valid number.")
            continue

        length = int(length)

        if length < 4:
            print("Password length should be at least 4.")
            continue

        password = generate_password(length)

        print("\nGenerated Password:", password)


main()
