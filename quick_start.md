# 🚀 Quick Setup Guide

## For Complete Beginners

### Step 1: Check Python Installation
Open your terminal/command prompt and type:
```bash
python --version
```
or
```bash
python3 --version
```

You should see something like: `Python 3.7.0` or higher

**Don't have Python?** Download it from: https://www.python.org/downloads/

---

### Step 2: Download the Game Files
Download these files to a folder on your computer:
- ✅ `game_enhanced.py` (main game file)
- ✅ `README.md` (documentation)
- ✅ `CHANGELOG.md` (version history)
- ✅ `requirements.txt` (dependencies info)

---

### Step 3: Run the Game

#### On Windows:
1. Open Command Prompt
2. Navigate to the game folder:
   ```cmd
   cd C:\path\to\game\folder
   ```
3. Run the game:
   ```cmd
   python game_enhanced.py
   ```

#### On Mac/Linux:
1. Open Terminal
2. Navigate to the game folder:
   ```bash
   cd /path/to/game/folder
   ```
3. Run the game:
   ```bash
   python3 game_enhanced.py
   ```

---

### Step 4: Play!
The game window will open automatically. Enjoy! 🎮

---

## Troubleshooting

### Problem: "python is not recognized"
**Solution**: Python is not installed or not in PATH
- Windows: Reinstall Python and check "Add to PATH" during installation
- Mac/Linux: Try `python3` instead of `python`

### Problem: "No module named 'tkinter'"
**Solution**: Tkinter is not installed
- **Ubuntu/Debian**: 
  ```bash
  sudo apt-get install python3-tk
  ```
- **Fedora**: 
  ```bash
  sudo dnf install python3-tkinter
  ```
- **Mac**: Tkinter comes with Python
- **Windows**: Tkinter comes with Python

### Problem: Game window doesn't open
**Solution**: Check your display settings
- Make sure you're not running in a headless environment
- Try running from a desktop environment, not SSH

---

## Features Quick Reference

### 🎮 Main Menu Options
1. **Start Game** - Normal mode with lifelines
2. **Practice Mode** - Learn without pressure
3. **Timed Challenge** - Test your speed
4. **Leaderboard** - View your best scores
5. **Statistics** - Track your progress
6. **How to Play** - Game instructions
7. **Exit** - Close the game

### ⚡ Lifelines (Normal Mode)
- **50-50**: Press to remove 2 wrong answers
- **Skip**: Press to skip the current question
- **Hint**: Press to get helpful clues

### 🎯 Tips for High Scores
1. Answer quickly for time bonuses
2. Use lifelines strategically
3. Build streaks for recognition
4. Try higher difficulties for multipliers
5. Practice mode helps learning

---

## First Time Setup

### When you first run the game:
1. The game will create `game_data.json` automatically
2. This file stores your statistics
3. Don't delete it unless you want to reset stats
4. It's safe to backup this file

### Recommended First Steps:
1. Start with **How to Play** to learn the rules
2. Try **Practice Mode** to learn the capitals
3. Then play **Normal Mode** for the full experience
4. Check **Statistics** to track improvement
5. Challenge yourself with **Timed Challenge**

---

## System Requirements

### Minimum:
- Python 3.7 or higher
- 512 MB RAM
- 50 MB disk space
- Any operating system (Windows, Mac, Linux)

### Recommended:
- Python 3.8 or higher
- 1 GB RAM
- 100 MB disk space
- Display resolution: 1024x768 or higher

---

## File Descriptions

| File | Size | Purpose |
|------|------|---------|
| `game_enhanced.py` | ~38 KB | Main game code |
| `README.md` | ~7 KB | Documentation |
| `CHANGELOG.md` | ~3 KB | Version history |
| `requirements.txt` | ~1 KB | Dependency info |
| `game_data.json` | < 1 KB | Your saved stats (auto-created) |

---

## Quick Commands Cheat Sheet

### Windows Command Prompt
```cmd
# Navigate to folder
cd C:\Users\YourName\Downloads\game

# Run game
python game_enhanced.py

# Check Python version
python --version
```

### Mac/Linux Terminal
```bash
# Navigate to folder
cd ~/Downloads/game

# Run game
python3 game_enhanced.py

# Check Python version
python3 --version

# Make executable (optional)
chmod +x game_enhanced.py
```

---

## Getting Help

### In-Game Help
- Press the **"❓ How to Play"** button in the main menu
- Read the instructions screen
- Check the statistics to track progress

### External Help
1. Read the full `README.md` file
2. Check `CHANGELOG.md` for latest features
3. Review `FEATURE_COMPARISON.md` for details
4. Open an issue on GitHub (if available)

---

## Customization Quick Start

### Want to add more countries?
1. Open `game_enhanced.py` in a text editor
2. Find the `countries` list (starts around line 8)
3. Copy an existing country entry
4. Modify the details for your new country
5. Save and run!

Example:
```python
{
    "name": "Your Country",
    "capital": "Capital City",
    "population": "X million",
    "independence": "Date",
    "president": "Leader",
    "language": "Language",
    "flag": "🏳️",  # Find emoji flag
    "currency": "Currency",
    "facts": "Fun fact",
    "region": "Region"
}
```

### Want to change difficulty?
Look for these values in the code:
- `self.time_limit = 30` - Time per question
- `self.max_questions = 10` - Questions per game
- Lifeline counts in `self.lifelines` dictionary

---

## Safety & Privacy

✅ **This game is safe:**
- No internet connection required
- No personal data collected online
- No ads or tracking
- Open source code (you can read it!)
- Data stays on your computer

📁 **What data is stored locally:**
- Your game statistics only
- No personal information
- Stored in `game_data.json`
- Can be deleted anytime

---

## Next Steps

After playing a few games:

1. 📖 Read the full README.md for all features
2. 📊 Check your statistics regularly
3. 🎯 Set personal goals (e.g., 90% accuracy)
4. 🔥 Try to beat your best streak
5. 🌍 Challenge friends and family
6. 💡 Consider adding more countries
7. 🎨 Customize if you know Python

---

## One-Line Install & Run

For advanced users, here's a quick copy-paste command:

**Windows:**
```cmd
cd path\to\game && python game_enhanced.py
```

**Mac/Linux:**
```bash
cd path/to/game && python3 game_enhanced.py
```

---

## Support

**Having issues?**
1. Check the Troubleshooting section above
2. Ensure Python 3.7+ is installed
3. Make sure tkinter is available
4. Try running from a terminal/command prompt
5. Check for error messages

**Need more help?**
- Check Python documentation: https://docs.python.org/3/
- Tkinter tutorial: https://docs.python.org/3/library/tkinter.html

---

## Enjoy the Game! 🌍🎉

Thank you for playing African Capitals Quiz - Enhanced Edition!

**Remember:** The goal is to learn and have fun. Don't worry about scores at first - focus on learning the capitals!

---

*Last updated: November 17, 2025*
*Version: 2.0.0 - Enhanced Edition*