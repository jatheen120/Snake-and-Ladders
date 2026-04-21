import tkinter as tk
from tkinter import messagebox
import random

class RPS:
    def __init__(self, root):
        self.root = root
        self.root.title("Rock Paper Scissors")
        self.root.geometry("400x500")

        self.choices = ["Rock", "Paper", "Scissors"]
        self.emojis = {"Rock":"✊", "Paper":"✋", "Scissors":"✌️"}

        self.player_score = 0
        self.comp_score = 0
        self.rounds = 0

        tk.Label(root, text="Rock Paper Scissors", font=("Arial", 18)).pack(pady=10)

        self.info = tk.Label(root, text="Round: 0", font=("Arial", 12))
        self.info.pack()

        self.result = tk.Label(root, text="", font=("Arial", 14))
        self.result.pack(pady=10)

        self.display = tk.Label(root, text="❓ vs ❓", font=("Arial", 40))
        self.display.pack(pady=20)

        frame = tk.Frame(root)
        frame.pack()

        tk.Button(frame, text="Rock ✊", command=lambda: self.play("Rock")).grid(row=0, column=0, padx=5)
        tk.Button(frame, text="Paper ✋", command=lambda: self.play("Paper")).grid(row=0, column=1, padx=5)
        tk.Button(frame, text="Scissors ✌️", command=lambda: self.play("Scissors")).grid(row=0, column=2, padx=5)

        self.score = tk.Label(root, text="You: 0  Computer: 0", font=("Arial", 12))
        self.score.pack(pady=10)

if __name__ == "__main__":
    root = tk.Tk()
    RPS(root)
    root.mainloop()