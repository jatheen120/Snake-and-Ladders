import tkinter as tk
from tkinter import messagebox
import random

class NumberGuess:
    def __init__(self, root):
        self.root = root
        self.root.title("Number Guessing Game")
        self.root.geometry("400x500")

        self.target = 0
        self.attempts = 0
        self.max_attempts = 10

        tk.Label(root, text="Number Guessing Game", font=("Arial", 18)).pack(pady=10)

        tk.Button(root, text="Easy (1-50)", command=lambda: self.start(50)).pack(pady=5)
        tk.Button(root, text="Medium (1-100)", command=lambda: self.start(100)).pack(pady=5)
        tk.Button(root, text="Hard (1-200)", command=lambda: self.start(200)).pack(pady=5)

        self.info = tk.Label(root, text="")
        self.info.pack(pady=10)

        self.entry = tk.Entry(root, font=("Arial", 14))
        self.entry.pack(pady=10)

        tk.Button(root, text="Guess", command=self.check).pack(pady=5)

        self.result = tk.Label(root, text="", font=("Arial", 14))
        self.result.pack(pady=10)

    def start(self, limit):
        self.target = random.randint(1, limit)
        self.attempts = 0
        self.info.config(text=f"Guess number between 1 and {limit}")
        self.result.config(text="")
        self.entry.config(state="normal")

    def check(self):
        try:
            guess = int(self.entry.get())
        except:
            self.result.config(text="Enter valid number")
            return

        self.attempts += 1

        if guess < self.target:
            self.result.config(text="Too Low ⬆️")
        elif guess > self.target:
            self.result.config(text="Too High ⬇️")
        else:
            messagebox.showinfo("Win", f"Correct! Attempts: {self.attempts}")
            self.entry.config(state="disabled")
            return

        if self.attempts >= self.max_attempts:
            messagebox.showinfo("Game Over", f"Number was {self.target}")
            self.entry.config(state="disabled")

if __name__ == "__main__":
    root = tk.Tk()
    NumberGuess(root)
    root.mainloop()