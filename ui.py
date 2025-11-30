import tkinter as tk

class QuizUI:
    def __init__(self, controller):
        self.controller = controller  
        self.root = tk.Tk()
        self.root.title("Quiz Engine")
        self.root.geometry("600x400")
        self.selected_option = tk.IntVar()

        self.username_entry = None
        self.question_label = None
        self.option_buttons = []
        self.next_button = None

        self.create_welcome_screen()

    def create_welcome_screen(self):
        self.clear_screen()
        tk.Label(self.root, text="Welcome to the Quiz!", font=("Arial", 18, "bold")).pack(pady=30)
        tk.Label(self.root, text="Enter your name:", font=("Arial", 14)).pack(pady=10)

        self.username_entry = tk.Entry(self.root, font=("Arial", 14))
        self.username_entry.pack(pady=10)

        tk.Button(
            self.root,
            text="Start Quiz",
            font=("Arial", 12, "bold"),
            command=lambda: self.controller.start_quiz(self.username_entry.get())
        ).pack(pady=20)

    def show_question(self, question_text, options):
        self.clear_screen()

        self.selected_option.set(-1)
        self.question_label = tk.Label(self.root, text=question_text, font=("Mono", 14, "bold"), wraplength=550)
        self.question_label.pack(pady=20)

        self.option_buttons = []
        for i, opt in enumerate(options):
            btn = tk.Radiobutton(
                self.root,
                text=opt,
                variable=self.selected_option,
                value=i,
                font=("Mono", 12),
                anchor="w",
                justify="left"
            )
            btn.pack(fill="x", padx=40, pady=5)
            self.option_buttons.append(btn)

        self.next_button = tk.Button(
            self.root,
            text="Next",
            font=("Mono", 12, "bold"),
            command=lambda: self.controller.check_answer(self.selected_option.get())
        )
        self.next_button.pack(pady=20)

    def show_result(self, score, total, percentage):
        self.clear_screen()
        tk.Label(self.root, text="🎉 Quiz Completed!", font=("Arial", 18, "bold")).pack(pady=20)
        tk.Label(
            self.root,
            text=f"You scored {score}/{total}\nPercentage: {percentage}%",
            font=("Arial", 14)
        ).pack(pady=20)

        tk.Button(self.root, text="Exit", font=("Arial", 12, "bold"),
            command=self.root.destroy).pack(pady=10)

    def clear_screen(self):
        for widget in self.root.winfo_children():
            widget.destroy()

    def start(self):
        self.root.mainloop()
