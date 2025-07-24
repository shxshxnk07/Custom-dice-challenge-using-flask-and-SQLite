from flask import Flask, render_template, request, jsonify
import sqlite3
from datetime import datetime

app = Flask(__name__)

def init_db():
    conn = sqlite3.connect('database.db')
    c = conn.cursor()
    c.execute('''
        CREATE TABLE IF NOT EXISTS games (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            player1 TEXT,
            dice1 INTEGER,
            player2 TEXT,
            dice2 INTEGER,
            winner TEXT,
            timestamp TEXT
        )
    ''')
    conn.commit()
    conn.close()

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/api/games", methods=["POST"])
def save_game():
    data = request.get_json()

    player1 = data.get("player1")
    dice1 = data.get("dice1")
    player2 = data.get("player2")
    dice2 = data.get("dice2")
    winner = data.get("winner")
    timestamp = datetime.now().isoformat()

    if not all([player1, isinstance(dice1, int), player2, isinstance(dice2, int), winner]):
        return jsonify({"status": "error", "message": "Invalid input"}), 400

    conn = sqlite3.connect('database.db')
    c = conn.cursor()
    c.execute('''
        INSERT INTO games (player1, dice1, player2, dice2, winner, timestamp)
        VALUES (?, ?, ?, ?, ?, ?)
    ''', (player1, dice1, player2, dice2, winner, timestamp))
    conn.commit()
    conn.close()

    return jsonify({"status": "success", "message": "Game saved!"})

@app.route("/clear", methods=["POST"])
def clear_database():
    conn = sqlite3.connect('database.db')
    c = conn.cursor()
    c.execute("DELETE FROM games")  # Clears all rows
    conn.commit()
    conn.close()
    return jsonify({"status": "success", "message": "Database cleared!"})


if __name__ == "__main__":
    init_db()
    app.run(debug=True)
