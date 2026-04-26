import tkinter as tk
from tkinter import messagebox

class TicTacToe:
    def __init__(self, root):
        self.root = root
        self.root.title("Tic Tac Toe")
        self.root.geometry("400x500")

        self.board = [""] * 9
        self.current = "X"

        tk.Label(root, text="Tic Tac Toe", font=("Arial", 18)).pack(pady=10)

        self.status = tk.Label(root, text="X Turn", font=("Arial", 12))
        self.status.pack()

        self.frame = tk.Frame(root)
        self.frame.pack(pady=20)

        self.buttons = []
        for i in range(9):
            btn = tk.Button(self.frame, text="", font=("Arial", 30),
                            width=4, height=2,
                            command=lambda i=i: self.move(i))
            btn.grid(row=i//3, column=i%3)
            self.buttons.append(btn)

        tk.Button(root, text="Reset", command=self.reset).pack(pady=10)

    def move(self, i):
        if self.board[i] != "":
            return

        self.board[i] = self.current
        self.buttons[i].config(text=self.current)

        if self.check():
            messagebox.showinfo("Winner", f"{self.current} Wins")
            self.reset()
            return

        if "" not in self.board:
            messagebox.showinfo("Draw", "Match Draw")
            self.reset()
            return

        self.current = "O" if self.current == "X" else "X"
        self.status.config(text=f"{self.current} Turn")

    def check(self):
        wins = [(0,1,2),(3,4,5),(6,7,8),
                (0,3,6),(1,4,7),(2,5,8),
                (0,4,8),(2,4,6)]

        for a,b,c in wins:
            if self.board[a] == self.board[b] == self.board[c] != "":
                return True
        return False

    def reset(self):
        self.board = [""] * 9
        self.current = "X"
        for b in self.buttons:
            b.config(text="")
        self.status.config(text="X Turn")

if __name__ == "__main__":
    root = tk.Tk()
    TicTacToe(root)
    root.mainloop()