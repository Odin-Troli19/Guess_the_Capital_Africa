# 🌍 African Capitals Quiz - Enhanced Edition

An engaging and educational Python quiz game to test your knowledge of African geography! Features multiple game modes, lifelines, statistics tracking, and more.

![Python](https://img.shields.io/badge/Python-3.7+-blue.svg)
![Tkinter](https://img.shields.io/badge/GUI-Tkinter-green.svg)
![License](https://img.shields.io/badge/License-MIT-yellow.svg)

## ✨ Features

### 🎮 Multiple Game Modes
- **Normal Mode**: Classic 10-question quiz with lifelines
- **Practice Mode**: Unlimited questions without timer - perfect for learning!
- **Timed Challenge**: 20 rapid-fire questions with 15-second timer

### ⚡ Lifelines System
- **50-50**: Eliminate two wrong answers (1 per game)
- **Skip**: Skip difficult questions (2 per game)
- **Hint**: Get helpful clues about the capital (3 per game)

### 🏆 Advanced Features
- **Streak Tracking**: Build consecutive correct answers
- **"On Fire" Mode**: Special recognition for 5+ streaks
- **Statistics Dashboard**: Track your performance over time
- **Leaderboard**: View your personal best scores
- **Persistent Data**: Game progress and stats are saved automatically
- **Four Difficulty Levels**: Easy, Medium, Hard, Expert

### 📊 Comprehensive Statistics
- Games played
- Total correct answers
- Overall accuracy percentage
- Best score achievement
- Best streak record

### 🎨 User Interface
- Modern, colorful design
- Smooth navigation
- Large, easy-to-read fonts
- Interactive button effects
- Real-time score and timer displays

### 📚 Educational Content
For each correct answer, learn:
- Country population
- Independence date
- Current leader
- Official language(s)
- Currency
- Geographic region
- Interesting facts
- Country flag emoji

## 🚀 Getting Started

### Prerequisites
- Python 3.7 or higher
- Tkinter (usually comes pre-installed with Python)

### Installation

1. **Clone the repository**
   ```bash
   git clone https://github.com/yourusername/african-capitals-quiz.git
   cd african-capitals-quiz
   ```

2. **Run the game**
   ```bash
   python game_enhanced.py
   ```

That's it! No additional dependencies required.

## 🎯 How to Play

### Starting the Game
1. Launch the application
2. Select a game mode from the main menu
3. Enter your name (optional)
4. Choose your difficulty level
5. Start answering questions!

### Difficulty Levels

| Level  | Options | Timer | Hints | Challenge |
|--------|---------|-------|-------|-----------|
| Easy   | 4       | 30s   | Yes   | ⭐       |
| Medium | 4       | 30s   | No    | ⭐⭐     |
| Hard   | 5       | 30s   | No    | ⭐⭐⭐   |
| Expert | 6       | 30s   | No    | ⭐⭐⭐⭐ |

### Scoring System
- **Base Points**: 10 per correct answer
- **Time Bonus**: Points based on remaining time
- **Difficulty Multiplier**: 
  - Easy: 1x
  - Medium: 1.5x
  - Hard: 2x
  - Expert: 3x

### Using Lifelines

**50-50 Lifeline** (🎯)
- Removes two incorrect options
- Use when you're unsure between multiple answers
- Available: 1 per game

**Skip Lifeline** (⏭️)
- Skip the current question without penalty
- Useful for extremely difficult questions
- Available: 2 per game

**Hint Lifeline** (💡)
- Shows the first two letters of the capital
- Displays the geographic region
- Shows the length of the capital name
- Available: 3 per game

## 📁 Project Structure

```
african-capitals-quiz/
│
├── game_enhanced.py      # Main game file with all features
├── game.py               # Original game file
├── README.md             # This file
└── game_data.json        # Auto-generated save file (created on first run)
```

## 💾 Data Persistence

The game automatically saves:
- Total games played
- Overall accuracy
- Best score
- Best streak
- Last played date

Data is stored in `game_data.json` in the same directory as the game.

## 🌍 Countries Included

The game includes 10 African countries (expandable):
- Nigeria 🇳🇬
- Egypt 🇪🇬
- South Africa 🇿🇦
- Algeria 🇩🇿
- Ethiopia 🇪🇹
- Morocco 🇲🇦
- Kenya 🇰🇪
- Tanzania 🇹🇿
- Ghana 🇬🇭
- Senegal 🇸🇳

*More countries can be easily added to the `countries` list in the code.*

## 🎨 Screenshots

### Main Menu
- Colorful, intuitive interface
- Multiple game mode options
- Quick access to statistics

### Game Screen
- Large flag display
- Clear question text
- Colorful answer buttons
- Real-time timer and score
- Lifeline buttons (when available)

### Results Screen
- Detailed performance breakdown
- Encouraging feedback messages
- Easy navigation to replay or view stats

## 🛠️ Customization

### Adding More Countries
Edit the `countries` list in `game_enhanced.py`:

```python
{
    "name": "Country Name",
    "capital": "Capital City",
    "population": "X million",
    "independence": "Date",
    "president": "Leader Name",
    "language": "Languages",
    "flag": "🏳️",
    "currency": "Currency Name",
    "facts": "Interesting fact",
    "region": "Geographic region"
}
```

### Adjusting Difficulty
Modify these values in the code:
- `self.time_limit`: Time per question (seconds)
- `self.max_questions`: Questions per game
- Number of options per difficulty level

### Changing Lifelines
Adjust the lifeline counts:
```python
self.lifelines = {
    "50-50": 1,  # Change these numbers
    "skip": 2,
    "hint": 3
}
```

## 🔧 Technical Details

- **Language**: Python 3.7+
- **GUI Framework**: Tkinter
- **Data Storage**: JSON
- **No External Dependencies**: Uses only Python standard library

## 🤝 Contributing

Contributions are welcome! Here are some ideas:
- Add more African countries
- Create new game modes
- Implement multiplayer functionality
- Add sound effects
- Create achievement system
- Add more question types (reverse: capital to country)

## 📝 Future Enhancements

- [ ] Sound effects for correct/wrong answers
- [ ] Animated transitions
- [ ] Online leaderboard
- [ ] Multiplayer mode
- [ ] Additional continents
- [ ] Mobile app version
- [ ] Achievement badges
- [ ] Daily challenges
- [ ] Difficulty adaptation based on performance

## 🐛 Known Issues

None currently! Please report any bugs you find.

## 📄 License

This project is licensed under the MIT License - feel free to use and modify as needed.

## 👏 Acknowledgments

- Flag emojis from Unicode Standard
- Country data sourced from public databases
- Inspired by geography education games

## 📞 Contact

For questions, suggestions, or feedback:
- Open an issue on GitHub
- Submit a pull request

---

**Enjoy learning about African geography!** 🌍✨

*Made with ❤️ for geography enthusiasts*