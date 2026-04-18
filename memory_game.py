import tkinter as tk
from tkinter import messagebox
import random

class MemoryGame:
    def __init__(self, root):
        self.root = root
        self.root.title("Memory Game")
        self.root.geometry("500x550")

        self.emojis = ["🐶","🐱","🐭","🐹","🐰","🦊","🐻","🐼"]

        self.cards = []
        self.buttons = []
        self.flipped = []
        self.score = 0
        self.moves = 0

        self.top = tk.Label(root, text="Memory Game", font=("Arial", 18))
        self.top.pack(pady=10)

        self.info = tk.Label(root, text="Moves: 0  Score: 0", font=("Arial", 12))
        self.info.pack()

        self.frame = tk.Frame(root)
        self.frame.pack(pady=10)

        tk.Button(root, text="Start Game", command=self.start).pack(pady=5)

    def start(self):
        self.cards = self.emojis * 2
        random.shuffle(self.cards)

        self.buttons = []
        self.flipped = []
        self.score = 0
        self.moves = 0

        for widget in self.frame.winfo_children():
            widget.destroy()

        for i in range(16):
            btn = tk.Button(self.frame, text="❓", width=6, height=3,
                            command=lambda i=i: self.flip(i))
            btn.grid(row=i//4, column=i%4)
            self.buttons.append(btn)

        self.update_info()

    def flip(self, i):
        if len(self.flipped) == 2 or self.buttons[i]["text"] != "❓":
            return

        self.buttons[i].config(text=self.cards[i])
        self.flipped.append(i)

        if len(self.flipped) == 2:
            self.root.after(500, self.check)

    def check(self):
        i1, i2 = self.flipped
        self.moves += 1

        if self.cards[i1] == self.cards[i2]:
            self.score += 10
        else:
            self.buttons[i1].config(text="❓")
            self.buttons[i2].config(text="❓")

        self.flipped = []
        self.update_info()

        if all(btn["text"] != "❓" for btn in self.buttons):
            messagebox.showinfo("Game Over", f"Score: {self.score}")

    def update_info(self):
        self.info.config(text=f"Moves: {self.moves}  Score: {self.score}")

if __name__ == "__main__":
    root = tk.Tk()
    MemoryGame(root)
    root.mainloop()