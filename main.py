from quiz_engine.loader import load_questions
from quiz_engine.evaluator import ask_question
from quiz_engine.scorer import calculate_score, save_score

def main():
    print("\n=== QUIZ ENGINE CLI ===")

    username = input("Enter your name: ").strip()

    questions = load_questions("data/Questions.json")

    correct = 0
    total = len(questions)

    for q in questions:
        if ask_question(q):
            correct += 1

    percentage = calculate_score(correct, total)

    print(f"\nQuiz Completed! {username}, your score is {correct}/{total}")
    print(f"Percentage: {percentage}%")

    save_score(username, correct, total)

if _name_ == "_main_":
    main()