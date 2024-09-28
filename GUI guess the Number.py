import tkinter as tk
from tkinter import messagebox
import random


class GuessTheNumberApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Guess the Number")
        self.low = 1
        self.high = 100
        self.attempts = 10
        self.number_to_guess = random.randint(self.low, self.high)

        # Create GUI components
        self.label = tk.Label(root, text=f"Guess a number between {self.low} and {self.high}")
        self.label.pack(pady=10)

        self.entry = tk.Entry(root)
        self.entry.pack(pady=10)

        self.button = tk.Button(root, text="Guess", command=self.check_guess)
        self.button.pack(pady=10)

        self.attempts_label = tk.Label(root, text=f"Attempts left: {self.attempts}")
        self.attempts_label.pack(pady=10)

    def check_guess(self):
        try:
            guess = int(self.entry.get())
        except ValueError:
            messagebox.showwarning("Invalid input", "Please enter a valid number.")
            return

        if guess < self.number_to_guess:
            messagebox.showinfo("Result", "Too low!")
        elif guess > self.number_to_guess:
            messagebox.showinfo("Result", "Too high!")
        else:
            messagebox.showinfo("Result",
                                f"Congratulations! You've guessed the number {self.number_to_guess} correctly!")
            self.reset_game()
            return

        self.attempts -= 1
        self.attempts_label.config(text=f"Attempts left: {self.attempts}")

        if self.attempts == 0:
            messagebox.showinfo("Game Over",
                                f"Sorry, you've run out of attempts. The number was {self.number_to_guess}.")
            self.reset_game()

    def reset_game(self):
        self.number_to_guess = random.randint(self.low, self.high)
        self.attempts = 10
        self.attempts_label.config(text=f"Attempts left: {self.attempts}")


# Create the main window
root = tk.Tk()
app = GuessTheNumberApp(root)
root.mainloop()
