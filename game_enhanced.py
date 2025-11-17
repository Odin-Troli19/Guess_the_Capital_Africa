import tkinter as tk
from tkinter import messagebox, ttk
import random
import time
import json
import os
from datetime import datetime

# African Countries Complete Data
countries = [
    {
        "name": "Nigeria", 
        "capital": "Abuja", 
        "population": "213 million", 
        "independence": "October 1, 1960", 
        "president": "Bola Ahmed Tinubu", 
        "language": "English", 
        "flag": "🇳🇬", 
        "currency": "Nigerian Naira (₦)",
        "facts": "Nigeria is the most populous country in Africa.",
        "region": "West Africa"
    },
    {
        "name": "Egypt", 
        "capital": "Cairo", 
        "population": "110 million", 
        "independence": "February 28, 1922", 
        "president": "Abdel Fattah el-Sisi", 
        "language": "Arabic", 
        "flag": "🇪🇬", 
        "currency": "Egyptian Pound (E£)",
        "facts": "The pyramids of Egypt are one of the seven wonders of the world.",
        "region": "North Africa"
    },
    {
        "name": "South Africa", 
        "capital": "Pretoria", 
        "population": "60 million", 
        "independence": "May 31, 1961", 
        "president": "Cyril Ramaphosa", 
        "language": "11 official languages including English, Afrikaans, Zulu", 
        "flag": "🇿🇦", 
        "currency": "South African Rand (R)",
        "facts": "South Africa has three capital cities.",
        "region": "Southern Africa"
    },
    {
        "name": "Algeria", 
        "capital": "Algiers", 
        "population": "44 million", 
        "independence": "July 5, 1962", 
        "president": "Abdelmadjid Tebboune", 
        "language": "Arabic, Berber", 
        "flag": "🇩🇿", 
        "currency": "Algerian Dinar (DA)",
        "facts": "Algeria is the largest country in Africa by land area.",
        "region": "North Africa"
    },
    {
        "name": "Ethiopia", 
        "capital": "Addis Ababa", 
        "population": "118 million", 
        "independence": "Never colonized", 
        "president": "Sahle-Work Zewde", 
        "language": "Amharic", 
        "flag": "🇪🇹", 
        "currency": "Ethiopian Birr (Br)",
        "facts": "Ethiopia is the only African country that was never fully colonized by European powers.",
        "region": "East Africa"
    },
    {
        "name": "Morocco", 
        "capital": "Rabat", 
        "population": "37 million", 
        "independence": "March 2, 1956", 
        "president": "King Mohammed VI", 
        "language": "Arabic, Berber", 
        "flag": "🇲🇦", 
        "currency": "Moroccan Dirham (MAD)",
        "facts": "Morocco has the oldest continuously operating university in the world.",
        "region": "North Africa"
    },
    {
        "name": "Kenya", 
        "capital": "Nairobi", 
        "population": "54 million", 
        "independence": "December 12, 1963", 
        "president": "William Ruto", 
        "language": "Swahili, English", 
        "flag": "🇰🇪", 
        "currency": "Kenyan Shilling (KSh)",
        "facts": "Kenya is known for its long-distance runners and safari tourism.",
        "region": "East Africa"
    },
    {
        "name": "Tanzania", 
        "capital": "Dodoma", 
        "population": "63 million", 
        "independence": "December 9, 1961", 
        "president": "Samia Suluhu Hassan", 
        "language": "Swahili, English", 
        "flag": "🇹🇿", 
        "currency": "Tanzanian Shilling (TSh)",
        "facts": "Mount Kilimanjaro, Africa's highest peak, is located in Tanzania.",
        "region": "East Africa"
    },
    {
        "name": "Ghana", 
        "capital": "Accra", 
        "population": "32 million", 
        "independence": "March 6, 1957", 
        "president": "Nana Akufo-Addo", 
        "language": "English", 
        "flag": "🇬🇭", 
        "currency": "Ghanaian Cedi (₵)",
        "facts": "Ghana was the first sub-Saharan African country to gain independence.",
        "region": "West Africa"
    },
    {
        "name": "Senegal", 
        "capital": "Dakar", 
        "population": "17 million", 
        "independence": "April 4, 1960", 
        "president": "Macky Sall", 
        "language": "French", 
        "flag": "🇸🇳", 
        "currency": "West African CFA Franc",
        "facts": "Senegal is famous for the Dakar Rally race.",
        "region": "West Africa"
    },
]


class EnhancedCapitalGame:
    def __init__(self, root):
        self.root = root
        self.root.title("🌍 African Capitals Quiz - Enhanced Edition")
        self.root.geometry("900x700")
        self.root.configure(bg="#f0f0f0")
        
        # Game state variables
        self.score = 0
        self.total_questions = 0
        self.max_questions = 10
        self.difficulty = "medium"
        self.current_question = None
        self.timer_active = False
        self.time_remaining = 0
        self.time_limit = 30
        self.current_streak = 0
        self.best_streak = 0
        self.player_name = ""
        
        # New features
        self.lifelines = {
            "50-50": 1,
            "skip": 2,
            "hint": 3
        }
        self.questions_answered = []
        self.practice_mode = False
        self.game_mode = "normal"  # normal, practice, timed_challenge
        
        # Statistics
        self.stats = {
            "games_played": 0,
            "total_correct": 0,
            "total_questions": 0,
            "best_score": 0,
            "fastest_time": float('inf')
        }
        
        # Load saved data
        self.load_data()
        
        # Setup main menu
        self.show_main_menu()
        
    def load_data(self):
        """Load saved game data"""
        try:
            if os.path.exists("game_data.json"):
                with open("game_data.json", "r") as f:
                    data = json.load(f)
                    self.stats = data.get("stats", self.stats)
                    self.best_streak = data.get("best_streak", 0)
        except Exception as e:
            print(f"Error loading data: {e}")
    
    def save_data(self):
        """Save game data"""
        try:
            data = {
                "stats": self.stats,
                "best_streak": self.best_streak,
                "last_played": datetime.now().isoformat()
            }
            with open("game_data.json", "w") as f:
                json.dump(data, f, indent=2)
        except Exception as e:
            print(f"Error saving data: {e}")
    
    def clear_window(self):
        """Clear all widgets from the window"""
        for widget in self.root.winfo_children():
            widget.destroy()
    
    def show_main_menu(self):
        """Display the main menu"""
        self.clear_window()
        
        # Main container
        main_frame = tk.Frame(self.root, bg="#2C3E50")
        main_frame.pack(fill=tk.BOTH, expand=True)
        
        # Title
        title_label = tk.Label(
            main_frame,
            text="🌍 AFRICAN CAPITALS QUIZ",
            font=("Helvetica", 32, "bold"),
            bg="#2C3E50",
            fg="#ECF0F1"
        )
        title_label.pack(pady=40)
        
        subtitle_label = tk.Label(
            main_frame,
            text="Enhanced Edition",
            font=("Helvetica", 14, "italic"),
            bg="#2C3E50",
            fg="#BDC3C7"
        )
        subtitle_label.pack(pady=5)
        
        # Menu buttons frame
        button_frame = tk.Frame(main_frame, bg="#2C3E50")
        button_frame.pack(pady=30)
        
        buttons = [
            ("🎮 Start Game", self.show_player_setup, "#27AE60"),
            ("📚 Practice Mode", self.start_practice_mode, "#3498DB"),
            ("⚡ Timed Challenge", self.start_timed_challenge, "#E67E22"),
            ("🏆 Leaderboard", self.show_leaderboard, "#9B59B6"),
            ("📊 Statistics", self.show_statistics, "#16A085"),
            ("❓ How to Play", self.show_instructions, "#95A5A6"),
            ("❌ Exit", self.root.quit, "#E74C3C")
        ]
        
        for text, command, color in buttons:
            btn = tk.Button(
                button_frame,
                text=text,
                command=command,
                font=("Helvetica", 14, "bold"),
                bg=color,
                fg="white",
                width=20,
                height=2,
                relief=tk.RAISED,
                bd=3,
                cursor="hand2"
            )
            btn.pack(pady=8)
            btn.bind("<Enter>", lambda e, b=btn: b.configure(relief=tk.SUNKEN))
            btn.bind("<Leave>", lambda e, b=btn: b.configure(relief=tk.RAISED))
        
        # Footer with stats
        stats_text = f"Games Played: {self.stats['games_played']} | Best Score: {self.stats['best_score']}% | Best Streak: {self.best_streak}"
        footer_label = tk.Label(
            main_frame,
            text=stats_text,
            font=("Helvetica", 10),
            bg="#2C3E50",
            fg="#BDC3C7"
        )
        footer_label.pack(side=tk.BOTTOM, pady=10)
    
    def show_player_setup(self):
        """Show player name input and difficulty selection"""
        self.clear_window()
        
        setup_frame = tk.Frame(self.root, bg="#34495E")
        setup_frame.pack(fill=tk.BOTH, expand=True)
        
        # Title
        tk.Label(
            setup_frame,
            text="Game Setup",
            font=("Helvetica", 24, "bold"),
            bg="#34495E",
            fg="white"
        ).pack(pady=30)
        
        # Player name
        tk.Label(
            setup_frame,
            text="Enter Your Name:",
            font=("Helvetica", 14),
            bg="#34495E",
            fg="white"
        ).pack(pady=10)
        
        name_entry = tk.Entry(
            setup_frame,
            font=("Helvetica", 14),
            width=25,
            justify="center"
        )
        name_entry.pack(pady=10)
        name_entry.focus()
        
        # Difficulty selection
        tk.Label(
            setup_frame,
            text="Select Difficulty:",
            font=("Helvetica", 14),
            bg="#34495E",
            fg="white"
        ).pack(pady=20)
        
        difficulty_frame = tk.Frame(setup_frame, bg="#34495E")
        difficulty_frame.pack(pady=10)
        
        difficulties = [
            ("Easy (4 options, hints)", "easy", "#27AE60"),
            ("Medium (4 options)", "medium", "#3498DB"),
            ("Hard (5 options)", "hard", "#E67E22"),
            ("Expert (6 options)", "expert", "#E74C3C")
        ]
        
        for text, diff, color in difficulties:
            btn = tk.Button(
                difficulty_frame,
                text=text,
                command=lambda d=diff, n=name_entry: self.start_game_with_setup(n.get(), d),
                font=("Helvetica", 12),
                bg=color,
                fg="white",
                width=25,
                height=2
            )
            btn.pack(pady=5)
        
        # Back button
        tk.Button(
            setup_frame,
            text="← Back to Menu",
            command=self.show_main_menu,
            font=("Helvetica", 12),
            bg="#7F8C8D",
            fg="white",
            width=20
        ).pack(pady=20)
    
    def start_game_with_setup(self, name, difficulty):
        """Start game with player name and difficulty"""
        self.player_name = name.strip() if name.strip() else "Player"
        self.difficulty = difficulty
        self.game_mode = "normal"
        self.start_game()
    
    def start_practice_mode(self):
        """Start practice mode (no timer, unlimited questions)"""
        self.player_name = "Practice"
        self.difficulty = "easy"
        self.practice_mode = True
        self.game_mode = "practice"
        self.max_questions = 999
        self.start_game()
    
    def start_timed_challenge(self):
        """Start timed challenge mode"""
        self.player_name = "Challenger"
        self.difficulty = "hard"
        self.game_mode = "timed_challenge"
        self.max_questions = 20
        self.time_limit = 15
        self.start_game()
    
    def start_game(self):
        """Initialize and start the game"""
        self.clear_window()
        self.score = 0
        self.total_questions = 0
        self.current_streak = 0
        self.questions_answered = []
        
        # Reset lifelines for new game
        if self.game_mode == "normal":
            self.lifelines = {"50-50": 1, "skip": 2, "hint": 3}
        else:
            self.lifelines = {"50-50": 0, "skip": 0, "hint": 0}
        
        # Main game frame
        self.game_frame = tk.Frame(self.root, bg="#ECF0F1")
        self.game_frame.pack(fill=tk.BOTH, expand=True)
        
        # Top bar with player info
        top_bar = tk.Frame(self.game_frame, bg="#2C3E50", height=80)
        top_bar.pack(fill=tk.X)
        top_bar.pack_propagate(False)
        
        # Player name and mode
        player_label = tk.Label(
            top_bar,
            text=f"Player: {self.player_name} | Mode: {self.game_mode.replace('_', ' ').title()}",
            font=("Helvetica", 12, "bold"),
            bg="#2C3E50",
            fg="white"
        )
        player_label.pack(side=tk.LEFT, padx=20)
        
        # Score display
        self.score_label = tk.Label(
            top_bar,
            text=f"Score: 0/0",
            font=("Helvetica", 14, "bold"),
            bg="#2C3E50",
            fg="#2ECC71"
        )
        self.score_label.pack(side=tk.LEFT, padx=20)
        
        # Streak display
        self.streak_label = tk.Label(
            top_bar,
            text=f"🔥 Streak: 0",
            font=("Helvetica", 12, "bold"),
            bg="#2C3E50",
            fg="#F39C12"
        )
        self.streak_label.pack(side=tk.LEFT, padx=10)
        
        # Timer display
        self.timer_label = tk.Label(
            top_bar,
            text="Time: --",
            font=("Helvetica", 14, "bold"),
            bg="#2C3E50",
            fg="#E74C3C"
        )
        self.timer_label.pack(side=tk.RIGHT, padx=20)
        
        # Lifelines bar
        if self.game_mode == "normal":
            lifeline_bar = tk.Frame(self.game_frame, bg="#34495E", height=60)
            lifeline_bar.pack(fill=tk.X)
            lifeline_bar.pack_propagate(False)
            
            tk.Label(
                lifeline_bar,
                text="Lifelines:",
                font=("Helvetica", 11, "bold"),
                bg="#34495E",
                fg="white"
            ).pack(side=tk.LEFT, padx=20)
            
            self.lifeline_buttons = {}
            lifeline_info = [
                ("50-50", "🎯 50-50", self.use_fifty_fifty),
                ("skip", "⏭️ Skip", self.use_skip),
                ("hint", "💡 Hint", self.use_hint)
            ]
            
            for key, text, command in lifeline_info:
                btn = tk.Button(
                    lifeline_bar,
                    text=f"{text} ({self.lifelines[key]})",
                    command=command,
                    font=("Helvetica", 10),
                    bg="#3498DB",
                    fg="white",
                    width=12
                )
                btn.pack(side=tk.LEFT, padx=10)
                self.lifeline_buttons[key] = btn
        
        # Question frame
        self.question_frame = tk.Frame(self.game_frame, bg="#ECF0F1")
        self.question_frame.pack(fill=tk.BOTH, expand=True, padx=20, pady=20)
        
        # Control buttons
        control_frame = tk.Frame(self.game_frame, bg="#ECF0F1")
        control_frame.pack(fill=tk.X, pady=10)
        
        tk.Button(
            control_frame,
            text="🏠 Main Menu",
            command=self.confirm_quit_game,
            font=("Helvetica", 11),
            bg="#95A5A6",
            fg="white",
            width=15
        ).pack(side=tk.LEFT, padx=20)
        
        if self.practice_mode:
            tk.Button(
                control_frame,
                text="✅ End Practice",
                command=self.end_practice,
                font=("Helvetica", 11),
                bg="#E74C3C",
                fg="white",
                width=15
            ).pack(side=tk.RIGHT, padx=20)
        
        # Load first question
        self.next_question()
    
    def use_fifty_fifty(self):
        """Remove two wrong answers"""
        if self.lifelines["50-50"] > 0 and hasattr(self, 'option_buttons'):
            self.lifelines["50-50"] -= 1
            self.lifeline_buttons["50-50"].config(text=f"🎯 50-50 ({self.lifelines['50-50']})")
            
            correct_answer = self.current_question['capital']
            wrong_options = [btn for btn in self.option_buttons 
                           if btn['text'] != correct_answer]
            
            # Disable two random wrong answers
            for btn in random.sample(wrong_options, min(2, len(wrong_options))):
                btn.config(state=tk.DISABLED, bg="#BDC3C7")
    
    def use_skip(self):
        """Skip the current question"""
        if self.lifelines["skip"] > 0:
            self.lifelines["skip"] -= 1
            self.lifeline_buttons["skip"].config(text=f"⏭️ Skip ({self.lifelines['skip']})")
            self.stop_timer()
            messagebox.showinfo("Skipped", f"Question skipped! The answer was: {self.current_question['capital']}")
            self.next_question()
    
    def use_hint(self):
        """Show a hint about the answer"""
        if self.lifelines["hint"] > 0:
            self.lifelines["hint"] -= 1
            self.lifeline_buttons["hint"].config(text=f"💡 Hint ({self.lifelines['hint']})")
            
            capital = self.current_question['capital']
            region = self.current_question['region']
            first_two = capital[:2]
            
            hint_text = f"💡 Hint:\n\n"
            hint_text += f"• The capital starts with: '{first_two}...'\n"
            hint_text += f"• Region: {region}\n"
            hint_text += f"• Number of letters: {len(capital)}"
            
            messagebox.showinfo("Hint", hint_text)
    
    def confirm_quit_game(self):
        """Confirm before quitting the game"""
        if messagebox.askyesno("Quit Game", "Are you sure you want to quit this game?"):
            self.stop_timer()
            self.show_main_menu()
    
    def end_practice(self):
        """End practice mode"""
        self.stop_timer()
        accuracy = (self.score / self.total_questions * 100) if self.total_questions > 0 else 0
        messagebox.showinfo(
            "Practice Ended",
            f"Practice session complete!\n\n"
            f"Questions answered: {self.total_questions}\n"
            f"Correct answers: {self.score}\n"
            f"Accuracy: {accuracy:.1f}%"
        )
        self.show_main_menu()
    
    def start_timer(self):
        """Start the countdown timer"""
        if self.practice_mode:
            return
        
        self.timer_active = True
        self.time_remaining = self.time_limit
        self.update_timer()
    
    def update_timer(self):
        """Update the timer display"""
        if self.timer_active and self.time_remaining > 0:
            self.timer_label.config(text=f"Time: {self.time_remaining}s")
            self.time_remaining -= 1
            self.root.after(1000, self.update_timer)
        elif self.timer_active and self.time_remaining == 0:
            self.timer_active = False
            self.handle_timeout()
    
    def stop_timer(self):
        """Stop the timer"""
        self.timer_active = False
    
    def handle_timeout(self):
        """Handle when time runs out"""
        self.current_streak = 0
        self.update_streak_display()
        messagebox.showwarning(
            "Time's Up!",
            f"⏰ Time ran out!\n\nThe correct answer was: {self.current_question['capital']}"
        )
        self.next_question()
    
    def next_question(self):
        """Load the next question"""
        # Clear question frame
        for widget in self.question_frame.winfo_children():
            widget.destroy()
        
        # Check if game should end
        if self.total_questions >= self.max_questions and not self.practice_mode:
            self.end_game()
            return
        
        # Select a random question
        self.current_question = random.choice(countries)
        self.total_questions += 1
        
        # Update score display
        self.score_label.config(
            text=f"Score: {self.score}/{self.total_questions-1} | Q: {self.total_questions}/{self.max_questions if not self.practice_mode else '∞'}"
        )
        
        # Question container
        q_container = tk.Frame(self.question_frame, bg="white", relief=tk.RAISED, bd=2)
        q_container.pack(fill=tk.BOTH, expand=True, pady=20)
        
        # Question number and country flag
        header_frame = tk.Frame(q_container, bg="white")
        header_frame.pack(pady=20)
        
        tk.Label(
            header_frame,
            text=f"Question {self.total_questions}",
            font=("Helvetica", 14, "bold"),
            bg="white",
            fg="#2C3E50"
        ).pack()
        
        # Flag (large)
        tk.Label(
            header_frame,
            text=self.current_question['flag'],
            font=("Helvetica", 80),
            bg="white"
        ).pack(pady=10)
        
        # Question text
        question_text = f"What is the capital of {self.current_question['name']}?"
        tk.Label(
            q_container,
            text=question_text,
            font=("Helvetica", 18, "bold"),
            bg="white",
            fg="#34495E",
            wraplength=700
        ).pack(pady=20)
        
        # Options frame
        options_frame = tk.Frame(q_container, bg="white")
        options_frame.pack(pady=20)
        
        # Get options
        options = self.get_options_by_difficulty()
        
        # Create option buttons
        self.option_buttons = []
        colors = ["#3498DB", "#E74C3C", "#2ECC71", "#F39C12", "#9B59B6", "#1ABC9C"]
        
        for i, option in enumerate(options):
            btn = tk.Button(
                options_frame,
                text=option,
                command=lambda opt=option: self.check_answer(opt),
                font=("Helvetica", 14, "bold"),
                bg=colors[i % len(colors)],
                fg="white",
                width=35,
                height=2,
                relief=tk.RAISED,
                bd=3,
                cursor="hand2"
            )
            btn.pack(pady=8)
            self.option_buttons.append(btn)
        
        # Hint for easy mode
        if self.difficulty == "easy" and not hasattr(self, 'hint_used'):
            hint_text = f"💡 Hint: The capital starts with '{self.current_question['capital'][0]}'"
            tk.Label(
                q_container,
                text=hint_text,
                font=("Helvetica", 12, "italic"),
                bg="white",
                fg="#7F8C8D"
            ).pack(pady=10)
        
        # Start timer
        self.start_timer()
    
    def get_options_by_difficulty(self):
        """Generate answer options based on difficulty"""
        correct_capital = self.current_question['capital']
        
        # Determine number of options
        num_options = {
            "easy": 4,
            "medium": 4,
            "hard": 5,
            "expert": 6
        }.get(self.difficulty, 4)
        
        options = [correct_capital]
        all_capitals = [c['capital'] for c in countries if c['capital'] != correct_capital]
        
        # For harder difficulties, include similar capitals
        similar = [cap for cap in all_capitals if cap[0] == correct_capital[0]]
        other = [cap for cap in all_capitals if cap not in similar]
        
        # Add similar capitals first
        while len(options) < num_options and similar:
            option = random.choice(similar)
            if option not in options:
                options.append(option)
                similar.remove(option)
        
        # Fill with random capitals
        while len(options) < num_options and other:
            option = random.choice(other)
            if option not in options:
                options.append(option)
                other.remove(option)
        
        random.shuffle(options)
        return options
    
    def check_answer(self, answer):
        """Check if the answer is correct"""
        self.stop_timer()
        
        correct_capital = self.current_question['capital']
        is_correct = answer == correct_capital
        
        if is_correct:
            self.score += 1
            self.current_streak += 1
            if self.current_streak > self.best_streak:
                self.best_streak = self.current_streak
            
            self.update_streak_display()
            
            # Calculate points
            time_bonus = self.time_remaining if not self.practice_mode else 0
            diff_multiplier = {"easy": 1, "medium": 1.5, "hard": 2, "expert": 3}.get(self.difficulty, 1)
            points = int(10 + (time_bonus * diff_multiplier))
            
            # Show success message
            info = self.current_question
            streak_bonus = ""
            if self.current_streak >= 5:
                streak_bonus = f"\n🔥 ON FIRE! {self.current_streak} in a row!"
            
            messagebox.showinfo(
                "✅ Correct!",
                f"Excellent! +{points} points{streak_bonus}\n\n"
                f"🌍 Country: {info['name']} {info['flag']}\n"
                f"🏛️ Capital: {info['capital']}\n"
                f"👥 Population: {info['population']}\n"
                f"📅 Independence: {info['independence']}\n"
                f"👤 Leader: {info['president']}\n"
                f"💰 Currency: {info['currency']}\n"
                f"🗣️ Language: {info['language']}\n"
                f"📍 Region: {info['region']}\n"
                f"✨ Fact: {info['facts']}"
            )
        else:
            self.current_streak = 0
            self.update_streak_display()
            messagebox.showerror(
                "❌ Wrong!",
                f"Oops! The correct answer was:\n\n{correct_capital}\n\n"
                f"Keep trying! You'll get the next one! 💪"
            )
        
        # Update score
        self.score_label.config(
            text=f"Score: {self.score}/{self.total_questions} | Q: {self.total_questions}/{self.max_questions if not self.practice_mode else '∞'}"
        )
        
        # Record this question
        self.questions_answered.append({
            "country": self.current_question['name'],
            "correct": is_correct,
            "time": self.time_limit - self.time_remaining if not self.practice_mode else 0
        })
        
        # Next question
        self.next_question()
    
    def update_streak_display(self):
        """Update the streak display"""
        self.streak_label.config(text=f"🔥 Streak: {self.current_streak}")
    
    def end_game(self):
        """End the game and show results"""
        self.stop_timer()
        
        # Update statistics
        self.stats["games_played"] += 1
        self.stats["total_correct"] += self.score
        self.stats["total_questions"] += self.total_questions
        
        accuracy = (self.score / self.total_questions) * 100
        if accuracy > self.stats["best_score"]:
            self.stats["best_score"] = int(accuracy)
        
        self.save_data()
        
        # Show results screen
        self.show_results(accuracy)
    
    def show_results(self, accuracy):
        """Display game results"""
        self.clear_window()
        
        results_frame = tk.Frame(self.root, bg="#2C3E50")
        results_frame.pack(fill=tk.BOTH, expand=True)
        
        # Title
        tk.Label(
            results_frame,
            text="🎮 Game Over!",
            font=("Helvetica", 32, "bold"),
            bg="#2C3E50",
            fg="white"
        ).pack(pady=30)
        
        # Results container
        results_container = tk.Frame(results_frame, bg="white", relief=tk.RAISED, bd=3)
        results_container.pack(padx=50, pady=20, fill=tk.BOTH, expand=True)
        
        # Player name
        tk.Label(
            results_container,
            text=f"Player: {self.player_name}",
            font=("Helvetica", 16, "bold"),
            bg="white"
        ).pack(pady=10)
        
        # Score
        score_text = f"Score: {self.score} / {self.total_questions}"
        tk.Label(
            results_container,
            text=score_text,
            font=("Helvetica", 24, "bold"),
            bg="white",
            fg="#2ECC71" if accuracy >= 70 else "#E74C3C"
        ).pack(pady=10)
        
        # Accuracy
        tk.Label(
            results_container,
            text=f"Accuracy: {accuracy:.1f}%",
            font=("Helvetica", 20),
            bg="white",
            fg="#3498DB"
        ).pack(pady=5)
        
        # Best streak
        tk.Label(
            results_container,
            text=f"🔥 Best Streak: {self.best_streak}",
            font=("Helvetica", 16),
            bg="white",
            fg="#F39C12"
        ).pack(pady=5)
        
        # Performance message
        if accuracy >= 90:
            message = "🏆 Outstanding! You're an African geography expert!"
            color = "#F1C40F"
        elif accuracy >= 75:
            message = "🌟 Excellent! You know Africa very well!"
            color = "#2ECC71"
        elif accuracy >= 60:
            message = "👍 Good job! Keep learning about Africa!"
            color = "#3498DB"
        elif accuracy >= 40:
            message = "📚 Not bad! Practice more to improve!"
            color = "#E67E22"
        else:
            message = "💪 Keep practicing! You'll get better!"
            color = "#E74C3C"
        
        tk.Label(
            results_container,
            text=message,
            font=("Helvetica", 14, "italic"),
            bg="white",
            fg=color,
            wraplength=600
        ).pack(pady=20)
        
        # Buttons
        button_frame = tk.Frame(results_frame, bg="#2C3E50")
        button_frame.pack(pady=30)
        
        tk.Button(
            button_frame,
            text="🔄 Play Again",
            command=self.show_player_setup,
            font=("Helvetica", 14, "bold"),
            bg="#27AE60",
            fg="white",
            width=15,
            height=2
        ).pack(side=tk.LEFT, padx=10)
        
        tk.Button(
            button_frame,
            text="📊 View Stats",
            command=self.show_statistics,
            font=("Helvetica", 14, "bold"),
            bg="#3498DB",
            fg="white",
            width=15,
            height=2
        ).pack(side=tk.LEFT, padx=10)
        
        tk.Button(
            button_frame,
            text="🏠 Main Menu",
            command=self.show_main_menu,
            font=("Helvetica", 14, "bold"),
            bg="#95A5A6",
            fg="white",
            width=15,
            height=2
        ).pack(side=tk.LEFT, padx=10)
    
    def show_leaderboard(self):
        """Display the leaderboard"""
        self.clear_window()
        
        leaderboard_frame = tk.Frame(self.root, bg="#34495E")
        leaderboard_frame.pack(fill=tk.BOTH, expand=True)
        
        tk.Label(
            leaderboard_frame,
            text="🏆 LEADERBOARD",
            font=("Helvetica", 28, "bold"),
            bg="#34495E",
            fg="white"
        ).pack(pady=30)
        
        # Create leaderboard display
        lb_container = tk.Frame(leaderboard_frame, bg="white", relief=tk.RAISED, bd=3)
        lb_container.pack(padx=50, pady=20, fill=tk.BOTH, expand=True)
        
        # Personal best
        tk.Label(
            lb_container,
            text=f"Your Personal Best",
            font=("Helvetica", 18, "bold"),
            bg="white",
            fg="#2C3E50"
        ).pack(pady=20)
        
        stats_text = f"""
        🎯 Best Score: {self.stats['best_score']}%
        🔥 Best Streak: {self.best_streak}
        🎮 Games Played: {self.stats['games_played']}
        ✅ Total Correct: {self.stats['total_correct']}/{self.stats['total_questions']}
        """
        
        tk.Label(
            lb_container,
            text=stats_text,
            font=("Helvetica", 14),
            bg="white",
            fg="#34495E",
            justify=tk.LEFT
        ).pack(pady=10)
        
        # Back button
        tk.Button(
            leaderboard_frame,
            text="← Back to Menu",
            command=self.show_main_menu,
            font=("Helvetica", 12),
            bg="#7F8C8D",
            fg="white",
            width=20
        ).pack(pady=20)
    
    def show_statistics(self):
        """Display player statistics"""
        self.clear_window()
        
        stats_frame = tk.Frame(self.root, bg="#16A085")
        stats_frame.pack(fill=tk.BOTH, expand=True)
        
        tk.Label(
            stats_frame,
            text="📊 YOUR STATISTICS",
            font=("Helvetica", 28, "bold"),
            bg="#16A085",
            fg="white"
        ).pack(pady=30)
        
        # Stats container
        stats_container = tk.Frame(stats_frame, bg="white", relief=tk.RAISED, bd=3)
        stats_container.pack(padx=50, pady=20, fill=tk.BOTH, expand=True)
        
        # Calculate overall accuracy
        overall_accuracy = (self.stats['total_correct'] / self.stats['total_questions'] * 100) if self.stats['total_questions'] > 0 else 0
        
        stats_data = [
            ("🎮 Games Played", self.stats['games_played']),
            ("✅ Total Correct Answers", self.stats['total_correct']),
            ("❓ Total Questions Attempted", self.stats['total_questions']),
            ("📈 Overall Accuracy", f"{overall_accuracy:.1f}%"),
            ("🏆 Best Score", f"{self.stats['best_score']}%"),
            ("🔥 Best Streak", self.best_streak),
        ]
        
        for label, value in stats_data:
            stat_frame = tk.Frame(stats_container, bg="white")
            stat_frame.pack(pady=10, fill=tk.X, padx=30)
            
            tk.Label(
                stat_frame,
                text=label,
                font=("Helvetica", 14),
                bg="white",
                fg="#2C3E50",
                anchor=tk.W
            ).pack(side=tk.LEFT)
            
            tk.Label(
                stat_frame,
                text=str(value),
                font=("Helvetica", 14, "bold"),
                bg="white",
                fg="#3498DB",
                anchor=tk.E
            ).pack(side=tk.RIGHT)
        
        # Back button
        tk.Button(
            stats_frame,
            text="← Back to Menu",
            command=self.show_main_menu,
            font=("Helvetica", 12),
            bg="#7F8C8D",
            fg="white",
            width=20
        ).pack(pady=20)
    
    def show_instructions(self):
        """Display game instructions"""
        self.clear_window()
        
        instructions_frame = tk.Frame(self.root, bg="#9B59B6")
        instructions_frame.pack(fill=tk.BOTH, expand=True)
        
        tk.Label(
            instructions_frame,
            text="❓ HOW TO PLAY",
            font=("Helvetica", 28, "bold"),
            bg="#9B59B6",
            fg="white"
        ).pack(pady=30)
        
        # Instructions container
        inst_container = tk.Frame(instructions_frame, bg="white", relief=tk.RAISED, bd=3)
        inst_container.pack(padx=50, pady=20, fill=tk.BOTH, expand=True)
        
        instructions_text = """
        🎯 OBJECTIVE
        Test your knowledge of African capitals by answering as many questions correctly as possible!
        
        🎮 GAME MODES
        • Normal Mode: 10 questions with lifelines
        • Practice Mode: Unlimited questions, no timer
        • Timed Challenge: 20 questions with 15 seconds each
        
        ⚡ LIFELINES (Normal Mode Only)
        • 50-50: Remove two wrong answers (1 available)
        • Skip: Skip the current question (2 available)
        • Hint: Get helpful hints about the answer (3 available)
        
        📊 DIFFICULTY LEVELS
        • Easy: 4 options + first letter hint
        • Medium: 4 options
        • Hard: 5 options
        • Expert: 6 options
        
        🔥 STREAKS
        Get consecutive correct answers to build your streak!
        Reach 5+ streak to activate "ON FIRE" mode!
        
        🏆 SCORING
        • Base points: 10 per correct answer
        • Time bonus: Faster answers = more points
        • Difficulty multiplier: Harder difficulties = more points
        
        💡 TIPS
        • Read the question carefully
        • Use lifelines strategically
        • Practice mode helps you learn
        • Check the statistics to track your progress
        
        Good luck and have fun learning about Africa! 🌍
        """
        
        tk.Label(
            inst_container,
            text=instructions_text,
            font=("Helvetica", 12),
            bg="white",
            fg="#2C3E50",
            justify=tk.LEFT,
            wraplength=700
        ).pack(pady=20, padx=30)
        
        # Back button
        tk.Button(
            instructions_frame,
            text="← Back to Menu",
            command=self.show_main_menu,
            font=("Helvetica", 12),
            bg="#7F8C8D",
            fg="white",
            width=20
        ).pack(pady=20)


def on_closing(root):
    """Handle application closing"""
    if messagebox.askokcancel("Quit", "Do you want to exit the game?"):
        root.destroy()


if __name__ == "__main__":
    root = tk.Tk()
    app = EnhancedCapitalGame(root)
    root.protocol("WM_DELETE_WINDOW", lambda: on_closing(root))
    root.mainloop()