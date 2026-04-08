import tkinter as tk
import random

easy = ["cat","dog","sun","moon","tree","book","pen","fish","bird"]
medium = ["python","java","array","stack","queue","graph","binary","search","matrix","string"]
hard = ["algorithm","function","variable","compiler","interpreter","recursion","framework","database","backend","frontend","encryption","scalability","microservices","cybersecurity","polymorphism"]

root = tk.Tk()
root.title("Guess the Word")
root.geometry("420x450")

word = ""
guessed = []
used = []
attempts = 6
game_active = False

def start_game(level):
    global word, guessed, used, attempts, game_active
    if level == "easy":
        word = random.choice(easy)
    elif level == "medium":
        word = random.choice(medium)
    else:
        word = random.choice(hard)

    guessed = ["_"] * len(word)
    used = []
    attempts = 6
    game_active = True

    result_label.config(text="")
    guess_btn.config(state="normal")
    update_display()

def update_display():
    word_label.config(text=" ".join(guessed))
    attempts_label.config(text="Attempts: " + str(attempts))
    used_label.config(text="Used: " + " ".join(used))

def guess_letter():
    global attempts, game_active
    if not game_active:
        return

    letter = entry.get().lower().strip()
    entry.delete(0, tk.END)

    if len(letter) != 1 or not letter.isalpha():
        result_label.config(text="Enter a single letter")
        return

    if letter in used:
        result_label.config(text="Already used")
        return

    used.append(letter)
    attempts -= 1

    if letter in word:
        for i in range(len(word)):
            if word[i] == letter:
                guessed[i] = letter
        result_label.config(text="Correct")
    else:
        result_label.config(text="Wrong")

    update_display()

    if "_" not in guessed:
        word_label.config(text="You Won! " + word)
        guess_btn.config(state="disabled")
        game_active = False
    elif attempts == 0:
        word_label.config(text="Game Over! " + word)
        guess_btn.config(state="disabled")
        game_active = False

def restart():
    global game_active
    game_active = False
    word_label.config(text="")
    attempts_label.config(text="")
    used_label.config(text="")
    result_label.config(text="Select difficulty to start")
    guess_btn.config(state="disabled")

title = tk.Label(root, text="Guess the Word", font=("Arial", 18))
title.pack(pady=10)

frame = tk.Frame(root)
frame.pack()

tk.Button(frame, text="Easy", width=10, command=lambda: start_game("easy")).grid(row=0, column=0, padx=5)
tk.Button(frame, text="Medium", width=10, command=lambda: start_game("medium")).grid(row=0, column=1, padx=5)
tk.Button(frame, text="Hard", width=10, command=lambda: start_game("hard")).grid(row=0, column=2, padx=5)

word_label = tk.Label(root, text="", font=("Arial", 22))
word_label.pack(pady=20)

attempts_label = tk.Label(root, text="")
attempts_label.pack()

used_label = tk.Label(root, text="")
used_label.pack()

entry = tk.Entry(root, font=("Arial", 14))
entry.pack(pady=10)

guess_btn = tk.Button(root, text="Guess", state="disabled", command=guess_letter)
guess_btn.pack()

result_label = tk.Label(root, text="Select difficulty to start", fg="blue")
result_label.pack(pady=10)

restart_btn = tk.Button(root, text="Restart", command=restart)
restart_btn.pack(pady=5)

root.mainloop()