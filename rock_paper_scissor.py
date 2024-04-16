import tkinter as tk
from tkinter import messagebox
import random

def play_game(player_choice):
    choices = ['Rock', 'Paper', 'Scissors']
    computer_choice = random.choice(choices)

    result = ""

    if player_choice == computer_choice:
        result = "It's a tie!"
    elif (
        (player_choice == 'Rock' and computer_choice == 'Scissors') or
        (player_choice == 'Paper' and computer_choice == 'Rock') or
        (player_choice == 'Scissors' and computer_choice == 'Paper')
    ):
        result = "You win!"
    else:
        result = "You lose!"

    messagebox.showinfo("Result", f"Computer chose {computer_choice}. {result}")

# GUI setup
root = tk.Tk()
root.title("Rock, Paper, Scissors")

# Function to handle button clicks
def on_button_click(choice):
    play_game(choice)

# Create buttons for each choice
rock_button = tk.Button(root, text="Rock", command=lambda: on_button_click("Rock"))
rock_button.pack(side=tk.LEFT, padx=10)

paper_button = tk.Button(root, text="Paper", command=lambda: on_button_click("Paper"))
paper_button.pack(side=tk.LEFT, padx=10)

scissors_button = tk.Button(root, text="Scissors", command=lambda: on_button_click("Scissors"))
scissors_button.pack(side=tk.LEFT, padx=10)

# Run the main loop
root.mainloop()
