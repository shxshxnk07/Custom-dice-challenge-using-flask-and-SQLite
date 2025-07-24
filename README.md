# 🎲 Custom Dice Game (Flask + HTML/CSS/JS)

A simple web-based dice game built using **Python (Flask)** on the backend and **HTML, CSS, JavaScript** on the frontend. The game allows two players to roll dice, track game history, and determine the winner. Results are stored in a local SQLite database.

---

## 📁 Project Structure

```
custom-dice-game/
├── app.py                  # Flask application
├── database.db             # SQLite database to store game results
├── static/
│   ├── images/
│   │   ├── dice1.png
│   │   ├── dice2.png
│   │   ├── dice3.png
│   │   ├── dice4.png
│   │   ├── dice5.png
│   │   └── dice6.png
│   └── style.css           # Custom styling
├── templates/
│   └── index.html          # Main game interface
└── README.md               # Project documentation (this file)
```

---

## 🚀 Features

- 🎲 Roll animation for dice
- 👤 Custom player names
- 🏆 Automatic winner detection
- 💾 Stores results in SQLite
- 🧹 One-click **Clear History** feature

---

## ⚙️ Requirements

- Python 3.x
- Flask

Install required dependencies:

```bash
pip install flask
```

---

## ▶️ How to Run

1. Clone the repository or download the files.
2. Navigate to the project folder in terminal.
3. Run the Flask server:

```bash
python app.py
```

4. Open your browser and go to:

```
http://localhost:5000/
```

---

## 🧠 How It Works

- Users enter player names and click **Roll Dice**.
- Two random dice values are generated.
- Dice roll animation is shown using images (`dice1.png` to `dice6.png`).
- The winner is decided and stored in the SQLite database.
- You can clear all records using the **Clear Game History** button.

---

## 📸 Screenshot

![Game Interface](./static/images/sample.png)

---

## 🧼 Clear Database

To clear the database from UI:
- Click the **Clear Game History** button.

To manually clear the database:
```sql
DELETE FROM games;
```
Or from Python:
```python
import sqlite3
conn = sqlite3.connect('database.db')
conn.execute('DELETE FROM games')
conn.commit()
conn.close()
```

---

## 📌 Future Enhancements

- View game history
- Leaderboard for most wins
- Animated rolling sound
- Mobile responsiveness

---

## 👨‍💻 Developed By

**Shashank A.S**
