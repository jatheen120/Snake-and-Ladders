import tkinter as tk
import random
import subprocess
import sys

CELL_SIZE = 50
BOARD_SIZE = 10

root = tk.Tk()
root.title("Snake and Ladder")

canvas = tk.Canvas(root, width=500, height=500)
canvas.pack()

player1 = 1
player2 = 1
turn_p1 = True

snakes = {99:54, 70:55, 52:42, 25:2}
ladders = {6:25, 11:40, 60:85, 46:90}

cells = {}

def draw_board():
    num = 1
    for row in range(BOARD_SIZE):
        for col in range(BOARD_SIZE):

            if row % 2 == 0:
                actual_col = col
            else:
                actual_col = BOARD_SIZE - col - 1

            x1 = actual_col * CELL_SIZE
            y1 = 500 - (row + 1) * CELL_SIZE
            x2 = x1 + CELL_SIZE
            y2 = y1 + CELL_SIZE

            rect = canvas.create_rectangle(x1, y1, x2, y2, fill="#f5f5f5")
            circle = canvas.create_oval(x1+15, y1+15, x2-15, y2-15, fill="#ddd")

            canvas.create_text(x1 + 25, y1 + 25, text=str(num), font=("Arial", 8))

            cells[num] = (rect, circle)

            num += 1

def get_coords(pos):
    row = (pos - 1) // 10
    col = (pos - 1) % 10

    if row % 2 == 1:
        col = 9 - col

    x = col * CELL_SIZE + 25
    y = 500 - (row * CELL_SIZE + 25)

    return x, y

def draw_snakes_ladders():
    for s,e in snakes.items():
        x1,y1 = get_coords(s)
        x2,y2 = get_coords(e)
        canvas.create_line(x1,y1,x2,y2,width=4,fill="red",smooth=True)

    for s,e in ladders.items():
        x1,y1 = get_coords(s)
        x2,y2 = get_coords(e)
        canvas.create_line(x1,y1,x2,y2,width=4,fill="green")

p1_token = canvas.create_oval(0,0,20,20,fill="blue")
p2_token = canvas.create_oval(0,0,20,20,fill="orange")

def update_cell_colors():
    for num in cells:
        rect, circle = cells[num]
        canvas.itemconfig(rect, fill="#f5f5f5")
        canvas.itemconfig(circle, fill="#ddd")

    if player1 == player2:
        _, circle = cells[player1]
        canvas.itemconfig(circle, fill="purple")
    else:
        _, circle1 = cells[player1]
        _, circle2 = cells[player2]
        canvas.itemconfig(circle1, fill="blue")
        canvas.itemconfig(circle2, fill="orange")

def update_tokens():
    x1,y1 = get_coords(player1)
    x2,y2 = get_coords(player2)

    canvas.coords(p1_token,x1-10,y1-10,x1+10,y1+10)
    canvas.coords(p2_token,x2-10,y2-10,x2+10,y2+10)

    update_cell_colors()

status = tk.Label(root, text="Player 1 Turn", font=("Arial", 12))
status.pack()

def roll_dice():
    global player1, player2, turn_p1

    dice = random.randint(1,6)

    if turn_p1:
        player1 += dice
        if player1 > 100:
            player1 -= dice

        if player1 in snakes:
            player1 = snakes[player1]
        elif player1 in ladders:
            player1 = ladders[player1]

        status.config(text=f"P1 rolled {dice} → {player1}")

        if player1 == 100:
            status.config(text="🎉 Player 1 Wins!")
            roll_btn.config(state="disabled")

    else:
        player2 += dice
        if player2 > 100:
            player2 -= dice

        if player2 in snakes:
            player2 = snakes[player2]
        elif player2 in ladders:
            player2 = ladders[player2]

        status.config(text=f"P2 rolled {dice} → {player2}")

        if player2 == 100:
            status.config(text="🎉 Player 2 Wins!")
            roll_btn.config(state="disabled")

    turn_p1 = not turn_p1
    update_tokens()

def open_word_game():
    subprocess.Popen([sys.executable, "word.py"])
def open_higher_lower():
    subprocess.Popen([sys.executable, "higher_lower.py"])
def open_memory_game():
    subprocess.Popen([sys.executable, "memory_game.py"])


roll_btn = tk.Button(root, text="Roll Dice 🎲", command=roll_dice)
roll_btn.pack(pady=10)

word_btn = tk.Button(root, text="Play Guess Game 🧠", command=open_word_game)
word_btn.pack(pady=5)

hl_btn = tk.Button(root, text="Play Higher Lower 🔢", command=open_higher_lower)
hl_btn.pack(pady=5)

mem_btn = tk.Button(root, text="Play Memory Game 🃏", command=open_memory_game)
mem_btn.pack(pady=5)


draw_board()
draw_snakes_ladders()
update_tokens()

root.mainloop()

