questions = [
    {
        "question": "What is the keyword used to define a function in Python?",
        "options": ["A. function", "B. define", "C. def", "D. fun"],
        "answer": "C"
    },
    {
        "question": "Which loop is used when the number of iterations is known?",
        "options": ["A. while", "B. do while", "C. for", "D. repeat"],
        "answer": "C"
    },
    {
        "question": "Which module is used to generate random numbers?",
        "options": ["A. math", "B. random", "C. string", "D. os"],
        "answer": "B"
    },
    {
        "question": "Which data type stores True or False?",
        "options": ["A. int", "B. str", "C. bool", "D. float"],
        "answer": "C"
    },
    {
        "question": "Which symbol is used for comments in Python?",
        "options": ["A. //", "B. <!--", "C. #", "D. **"],
        "answer": "C"
    }
]


def display_score(score, total):
    print("\n-------------------------")
    print("Score:", score, "/", total)
    print("-------------------------")


def play_quiz():
    score = 0

    for question in questions:
        print("\n" + question["question"])

        for option in question["options"]:
            print(option)

        answer = input("Enter your answer: ").strip().upper()

        if answer == question["answer"]:
            print("Correct!")
            score += 1
        else:
            print("Wrong!")
            print("Correct Answer:", question["answer"])

    return score


def main():

    while True:

        print("\n========== PYTHON QUIZ GAME ==========")

        score = play_quiz()

        display_score(score, len(questions))

        if score == len(questions):
            print("Excellent!")
        elif score >= 3:
            print("Good Job!")
        else:
            print("Keep Practicing!")

        choice = input("\nDo you want to play again? (yes/no): ").lower()

        if choice != "yes":
            print("\nThank you for playing!")
            break


main()
