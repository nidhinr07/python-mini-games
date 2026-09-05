import random

symbols = ["🍒", "🍋", "🍊", "⭐", "7"]


def spin():
    return [
        random.choice(symbols),
        random.choice(symbols),
        random.choice(symbols)
    ]


def display_balance(balance):
    print(f"\nBalance: {balance} coins")


def main():
    balance = 100

    print("========== SLOT MACHINE ==========")
    print("Each spin costs 10 coins.")

    while True:
        display_balance(balance)

        choice = input("\nPress Enter to spin or type 'exit': ").strip().lower()

        if choice == "exit":
            break

        if balance < 10:
            print("Not enough coins!")
            break

        balance -= 10

        result = spin()

        print("\n|", result[0], "|", result[1], "|", result[2], "|")

        if result[0] == result[1] == result[2]:
            print("Jackpot! You won 50 coins!")
            balance += 50

        elif result[0] == result[1] or result[1] == result[2] or result[0] == result[2]:
            print("Nice! You won 20 coins!")
            balance += 20

        else:
            print("Better luck next time!")

    print("\nGame Over!")
    print("Final Balance:", balance)


main()
