import tkinter as tk
from tkinter import messagebox
import random

# Sample African country data (add more later)
countries = [
    {
        "name": "Nigeria",
        "capital": "Abuja",
        "population": "213 million",
        "independence": "October 1, 1960",
        "president": "Bola Ahmed Tinubu",
        "language": "English",
        "flag": "🇳🇬",
        "facts": "Nigeria is the most populous country in Africa."
    },
    {
        "name": "Egypt",
        "capital": "Cairo",
        "population": "110 million",
        "independence": "February 28, 1922",
        "president": "Abdel Fattah el-Sisi",
        "language": "Arabic",
        "flag": "🇪🇬",
        "facts": "The pyramids of Egypt are one of the seven wonders of the world."
    },
    {
        "name": "South Africa",
        "capital": "Pretoria",
        "population": "60 million",
        "independence": "May 31, 1961",
        "president": "Cyril Ramaphosa",
        "language": "11 official languages",
        "flag": "🇿🇦",
        "facts": "South Africa has three capital cities."
    }
]

class CapitalGame:
    def __init__(self, root):
        self.root = root
        self.root.title("Guess the Capital - Africa")
        self.score = 0
        self.current_question = None
        self.mode = None

        self.setup_widgets()

    def setup_widgets(self):
        self.frame = tk.Frame(self.root, padx=20, pady=20)
        self.frame.pack()

        self.name_label = tk.Label(self.frame, text="What's your name?")
        self.name_label.pack()

        self.name_entry = tk.Entry(self.frame)
        self.name_entry.pack()

        self.start_button = tk.Button(self.frame, text="Start Game", command=self.start_game)
        self.start_button.pack()

        self.score_label = tk.Label(self.root, text="Score: 0", font=("Helvetica", 12))
        self.score_label.pack()

    def start_game(self):
        self.player_name = self.name_entry.get()
        if not self.player_name:
            messagebox.showwarning("Input needed", "Please enter your name.")
            return
        self.clear_frame()
        greeting = tk.Label(self.frame, text=f"Hi {self.player_name}, welcome!", font=("Helvetica", 14))
        greeting.pack()

        start_msg = tk.Label(self.frame, text="Choose how you want to play:", pady=10)
        start_msg.pack()

        btn1 = tk.Button(self.frame, text="Choose by country name", command=lambda: self.set_mode("name"))
        btn1.pack(pady=5)

        btn2 = tk.Button(self.frame, text="Choose by flag", command=lambda: self.set_mode("flag"))
        btn2.pack(pady=5)

        self.reset_button = tk.Button(self.root, text="Reset Game", command=self.reset_game)
        self.reset_button.pack(pady=10)

    def set_mode(self, mode):
        self.mode = mode
        self.next_question()

    def next_question(self):
        self.clear_frame()
        self.current_question = random.choice(countries)

        question_text = (
            f"What is the capital of {self.current_question['name']}?"
            if self.mode == "name" else
            f"What is the capital of this country? {self.current_question['flag']}"
        )
        tk.Label(self.frame, text=question_text, font=("Helvetica", 12), wraplength=300).pack(pady=10)

        # Shuffle options
        options = [self.current_question['capital']]
        while len(options) < 4:
            option = random.choice(countries)['capital']
            if option not in options:
                options.append(option)
        random.shuffle(options)

        for option in options:
            tk.Button(self.frame, text=option, command=lambda opt=option: self.check_answer(opt)).pack(pady=2)

    def check_answer(self, answer):
        if answer == self.current_question['capital']:
            self.score += 1
            self.score_label.config(text=f"Score: {self.score}")
            info = self.current_question
            messagebox.showinfo(
                "Correct!",
                f"Correct! 🎉\n\n"
                f"Country: {info['name']} {info['flag']}\n"
                f"Capital: {info['capital']}\n"
                f"Population: {info['population']}\n"
                f"Independence: {info['independence']}\n"
                f"President: {info['president']}\n"
                f"Official Language: {info['language']}\n"
                f"Fact: {info['facts']}"
            )
        else:
            messagebox.showerror("Wrong!", f"Oops! The correct answer was {self.current_question['capital']}.")
        self.next_question()

    def reset_game(self):
        self.score = 0
        self.score_label.config(text="Score: 0")
        self.frame.destroy()
        self.setup_widgets()

    def clear_frame(self):
        for widget in self.frame.winfo_children():
            widget.destroy()

# Start the app
root = tk.Tk()
app = CapitalGame(root)
root.mainloop()
