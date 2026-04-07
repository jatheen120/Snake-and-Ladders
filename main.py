import tkinter as tk
import random

CELL_SIZE = 50
BOARD_SIZE = 10

# Create window
root = tk.Tk()
root.title("Snake and Ladder")

canvas = tk.Canvas(root, width=500, height=500)
canvas.pack()

# Game state
player1 = 1
player2 = 1
turn_p1 = True

# Snakes & ladders
snakes = {99:54, 70:55, 52:42, 25:2}
ladders = {6:25, 11:40, 60:85, 46:90}

# Draw board
def draw_board():
    num = 1
    for row in range(BOARD_SIZE):
        for col in range(BOARD_SIZE):
            x1 = col * CELL_SIZE
            y1 = 500 - (row + 1) * CELL_SIZE
            x2 = x1 + CELL_SIZE
            y2 = y1 + CELL_SIZE

            if row % 2 == 0:
                actual_col = col
            else:
                actual_col = BOARD_SIZE - col - 1

            x1 = actual_col * CELL_SIZE
            x2 = x1 + CELL_SIZE

            canvas.create_rectangle(x1, y1, x2, y2, fill="white")
            canvas.create_text(x1 + 25, y1 + 25, text=str(num))

            num += 1

# Convert position to coordinates
def get_coords(pos):
    row = (pos - 1) // 10
    col = (pos - 1) % 10

    if row % 2 == 1:
        col = 9 - col

    x = col * CELL_SIZE + 25
    y = 500 - (row * CELL_SIZE + 25)

    return x, y

# Draw players
p1_token = canvas.create_oval(0, 0, 20, 20, fill="red")
p2_token = canvas.create_oval(0, 0, 20, 20, fill="blue")

def update_tokens():
    x1, y1 = get_coords(player1)
    x2, y2 = get_coords(player2)

    canvas.coords(p1_token, x1-10, y1-10, x1+10, y1+10)
    canvas.coords(p2_token, x2-10, y2-10, x2+10, y2+10)

# Status label
status = tk.Label(root, text="Player 1 Turn", font=("Arial", 12))
status.pack()

# Dice roll
def roll_dice():
    global player1, player2, turn_p1

    dice = random.randint(1, 6)

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
            button.config(state="disabled")

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
            button.config(state="disabled")

    turn_p1 = not turn_p1
    update_tokens()

# Button
button = tk.Button(root, text="Roll Dice 🎲", command=roll_dice)
button.pack(pady=10)

# Initialize
draw_board()
update_tokens()

root.mainloop()