import tkinter as tk
from main import main

def start_ui():
    root = tk.Tk()
    root.title("Quiz Engine UI")

    tk.Label(root, text="Click to start the quiz!").pack(pady=20)
    tk.Button(root, text="Start Quiz", command=main).pack(pady=10)

    root.mainloop()

if __name__ == "__main__":
    start_ui()
