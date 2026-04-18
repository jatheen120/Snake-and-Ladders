import tkinter as tk
from tkinter import messagebox
import random

class HigherLower:
    def __init__(self, root):
        self.root = root
        self.root.title("Higher Lower Game")
        self.root.geometry("400x500")
        self.root.configure(bg="#222")

        self.current = 0
        self.score = 0
        self.streak = 0

        self.title = tk.Label(root, text="HIGHER LOWER", font=("Arial", 20, "bold"), bg="#222", fg="white")
        self.title.pack(pady=10)

        self.score_label = tk.Label(root, text="Score: 0", font=("Arial", 14), bg="#222", fg="green")
        self.score_label.pack()

        self.streak_label = tk.Label(root, text="Streak: 0", font=("Arial", 14), bg="#222", fg="orange")
        self.streak_label.pack()

        self.number_label = tk.Label(root, text="?", font=("Arial", 60), bg="#222", fg="white")
        self.number_label.pack(pady=20)

        btn_frame = tk.Frame(root, bg="#222")
        btn_frame.pack()

        tk.Button(btn_frame, text="HIGHER", width=10, command=lambda: self.guess("high")).grid(row=0, column=0, padx=10)
        tk.Button(btn_frame, text="LOWER", width=10, command=lambda: self.guess("low")).grid(row=0, column=1, padx=10)

        self.result = tk.Label(root, text="", font=("Arial", 14), bg="#222", fg="yellow")
        self.result.pack(pady=10)

        tk.Button(root, text="Start Game", command=self.start).pack(pady=10)

    def start(self):
        self.score = 0
        self.streak = 0
        self.current = random.randint(1, 100)

        self.number_label.config(text=str(self.current))
        self.score_label.config(text="Score: 0")
        self.streak_label.config(text="Streak: 0")
        self.result.config(text="")

    def guess(self, choice):
        if self.current == 0:
            return

        next_num = random.randint(1, 100)

        correct = (choice == "high" and next_num > self.current) or \
                  (choice == "low" and next_num < self.current) or \
                  (next_num == self.current)

        if correct:
            self.streak += 1
            points = 10 + self.streak * 2
            self.score += points

            self.result.config(text=f"Correct +{points}", fg="green")
        else:
            messagebox.showinfo("Game Over", f"Final Score: {self.score}")
            self.current = 0
            self.number_label.config(text="?")
            self.result.config(text="Game Over", fg="red")
            return

        self.current = next_num
        self.number_label.config(text=str(self.current))
        self.score_label.config(text=f"Score: {self.score}")
        self.streak_label.config(text=f"Streak: {self.streak}")

if __name__ == "__main__":
    root = tk.Tk()
    HigherLower(root)
    root.mainloop()