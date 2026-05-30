# Number Guessing Game 🎯

A simple Python terminal game where the player tries to guess a randomly generated number within a selected range and limited number of attempts.

---

## 📌 Features

- 3 difficulty levels:
  - Easy: 1–50 (10 tries)
  - Medium: 1–100 (7 tries)
  - Hard: 1–200 (5 tries)
- Hot/Cold feedback system based on how close your guess is
- Score system (starts at 100, decreases per wrong guess)
- Input validation (handles invalid or out-of-range inputs)
- Play again loop

---

## 🧠 How It Works

1. Choose a difficulty level
2. The computer picks a random number
3. You try to guess it within the allowed attempts
4. You get hints like:
   - 🔥 Very Hot (very close)
   - 🔥 Hot
   - 😐 Warm
   - 🥶 Cold
5. Game ends when you win or run out of tries

---

## ▶️ How to Run

Make sure you have Python installed (3.x recommended).

Then run:

```bash
python your_file_name.py