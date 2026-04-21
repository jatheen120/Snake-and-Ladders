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

    def play(self, choice):
        if self.rounds >= 5:
            messagebox.showinfo("Game Over", "Start new game")
            return

        self.rounds += 1
        comp = random.choice(self.choices)

        self.display.config(text=f"{self.emojis[choice]} vs {self.emojis[comp]}")

        if choice == comp:
            result = "Draw"
        elif (choice == "Rock" and comp == "Scissors") or \
             (choice == "Paper" and comp == "Rock") or \
             (choice == "Scissors" and comp == "Paper"):
            result = "You Win"
            self.player_score += 1
        else:
            result = "Computer Wins"
            self.comp_score += 1

        self.result.config(text=result)
        self.score.config(text=f"You: {self.player_score}  Computer: {self.comp_score}")
        self.info.config(text=f"Round: {self.rounds}/5")

        if self.rounds == 5:
            if self.player_score > self.comp_score:
                final = "You Win Game 🎉"
            elif self.comp_score > self.player_score:
                final = "Computer Wins 🤖"
            else:
                final = "Draw Game"

            messagebox.showinfo("Final Result", final)

if __name__ == "__main__":
    root = tk.Tk()
    RPS(root)
    root.mainloop()