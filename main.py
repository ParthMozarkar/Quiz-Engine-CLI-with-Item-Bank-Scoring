from quiz_engine.loader import load_questions
from quiz_engine.evaluator import evaluate_answer
from quiz_engine.scorer import calculate_score, save_score
from ui import QuizUI


class QuizController:
    def __init__(self):
        self.ui = QuizUI(self)
        self.username = ""      # stored internally, not shown
        self.questions = []
        self.current_q = 0
        self.correct = 0

    def start_quiz(self, username):
        # Save the username only for the leaderboard
        self.username = username.strip() if username.strip() else "Player"

        # Load questions and initialize quiz
        self.questions = load_questions("data/Questions.json")
        self.current_q = 0
        self.correct = 0

        self.show_next_question()

    def show_next_question(self):
        if self.current_q >= len(self.questions):
            self.end_quiz()
            return

        q = self.questions[self.current_q]
        self.ui.show_question(q["question"], q["options"])

    def check_answer(self, selected):
        # Prevent going beyond the list
        if self.current_q >= len(self.questions):
            return

        q = self.questions[self.current_q]
        result = evaluate_answer(selected, q["answer"])
        if result:
            self.correct += 1

        self.current_q += 1

        if self.current_q >= len(self.questions):
            self.end_quiz()
        else:
            self.show_next_question()

    def end_quiz(self):
        total = len(self.questions)
        percentage = calculate_score(self.correct, total)

        save_score(self.username, self.correct, total)

        self.ui.show_result(self.correct, total, percentage)

    def run(self):
        self.ui.start()


if __name__ == "__main__":
    app = QuizController()
    app.run()