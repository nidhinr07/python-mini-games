questions = [
    {
        "question": "Which language are you learning?",
        "options": ["Python", "Java", "C++", "PHP"],
        "answer": "Python"
    },
    {
        "question": "Which keyword is used to create a function in Python?",
        "options": ["function", "def", "func", "create"],
        "answer": "def"
    },
    {
        "question": "Which data type stores multiple values in an ordered collection?",
        "options": ["List", "Integer", "Boolean", "Float"],
        "answer": "List"
    },
    {
        "question": "Which symbol is used for comments in Python?",
        "options": ["//", "#", "/*", "--"],
        "answer": "#"
    },
    {
        "question": "Which module is commonly used to generate random values?",
        "options": ["time", "math", "random", "os"],
        "answer": "random"
    }
]


def display_question(question, number):
    print(f"\nQuestion {number}")
    print(question["question"])

    for i, option in enumerate(question["options"], start=1):
        print(f"{i}. {option}")


def play_game():
    score = 0

    print("========== QUIZ BATTLE ==========")

    for number, question in enumerate(questions, start=1):

        display_question(question, number)

        choice = input("Enter your answer (1-4): ").strip()

        if not choice.isdigit() or int(choice) not in range(1, 5):
            print("Invalid choice!")
            continue

        answer = question["options"][int(choice) - 1]

        if answer == question["answer"]:
            print("Correct!")
            score += 1
        else:
            print("Wrong!")
            print("Correct answer:", question["answer"])

    print("\n========== FINAL RESULT ==========")
    print("Your Score:", score, "/", len(questions))

    if score == len(questions):
        print("Excellent! You got everything correct.")

    elif score >= 3:
        print("Good job!")

    else:
        print("Keep practicing!")


def main():

    while True:

        play_game()

        choice = input("\nPlay Again? (yes/no): ").strip().lower()

        if choice != "yes":
            print("\nThanks for playing!")
            break


main()
