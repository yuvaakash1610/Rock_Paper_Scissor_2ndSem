# ✊✋✌️ Rock, Paper & Scissors Game

A simple command-line Rock, Paper, Scissors game built with Python where you play against a bot.

---

## 📋 Description

This is a terminal-based game where the player competes against a randomly-choosing bot. The game keeps track of both the player's and bot's scores across multiple rounds, and continues until the player chooses to stop.

---

## 🚀 How to Run

Make sure you have **Python 3** installed, then run:

```bash
python rock_paper_scissors.py
```

---

## 🎮 How to Play

1. Run the program.
2. You'll be shown three options:
   - `1` → Rock
   - `2` → Paper
   - `3` → Scissors
3. Enter your choice (1, 2, or 3).
4. The bot picks randomly — the winner of the round is announced.
5. Scores are updated and displayed after each round.
6. After each round, you'll be asked: **"Do you want to continue? (Y/N)"**
   - Enter `Y` to play another round.
   - Enter `N` to quit.

---

## 🧠 Game Rules

| Player   | Bot      | Result     |
|----------|----------|------------|
| Rock     | Scissors | Player wins ✅ |
| Rock     | Paper    | Bot wins ❌ |
| Paper    | Rock     | Player wins ✅ |
| Paper    | Scissors | Bot wins ❌ |
| Scissors | Paper    | Player wins ✅ |
| Scissors | Rock     | Bot wins ❌ |
| Any      | Same     | Tie 🤝 |

---

## 📁 Project Structure

```
rock_paper_scissors.py   # Main game file
README.md                # Project documentation
```

---

## 🛠️ Requirements

- Python 3.x
- No external libraries needed (only uses the built-in `random` module)

---

## 📌 Example Output

<img width="550" height="987" alt="image" src="https://github.com/user-attachments/assets/ae0fbdd8-6283-4a17-8e24-43aa732d4ad1" />


---

## 👤 Author

> K Yuvaakash 

---

## 📄 License

This project is open source and available under the [MIT License](LICENSE).
