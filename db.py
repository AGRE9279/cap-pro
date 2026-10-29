"""Base de données locale (SQLite). Sera remplacée par Supabase à une étape suivante."""
import hashlib
import hmac
import os
import sqlite3

DB_PATH = os.getenv("DB_PATH", "eleves.db")


def _conn():
    conn = sqlite3.connect(DB_PATH)
    conn.row_factory = sqlite3.Row
    return conn


def init():
    with _conn() as c:
        c.executescript(
            """
            CREATE TABLE IF NOT EXISTS users (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                username TEXT UNIQUE NOT NULL,
                nom TEXT NOT NULL,
                salt TEXT NOT NULL,
                password_hash TEXT NOT NULL,
                filiere TEXT DEFAULT '',
                created_at TEXT DEFAULT CURRENT_TIMESTAMP
            );
            CREATE TABLE IF NOT EXISTS scores (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                user_id INTEGER NOT NULL,
                filiere TEXT NOT NULL,
                score INTEGER NOT NULL,
                total INTEGER NOT NULL,
                created_at TEXT DEFAULT CURRENT_TIMESTAMP
            );
            CREATE TABLE IF NOT EXISTS ai_usage (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                user_id INTEGER NOT NULL,
                created_at TEXT DEFAULT CURRENT_TIMESTAMP
            );
            """
        )


def _hash(password, salt):
    return hashlib.pbkdf2_hmac("sha256", password.encode(), bytes.fromhex(salt), 200_000).hex()


def create_user(username, nom, password, filiere=""):
    """Retourne None si le nom d'utilisateur existe déjà."""
    username = username.strip().lower()
    salt = os.urandom(16).hex()
    try:
        with _conn() as c:
            c.execute(
                "INSERT INTO users (username, nom, salt, password_hash, filiere) VALUES (?,?,?,?,?)",
                (username, nom.strip(), salt, _hash(password, salt), filiere),
            )
        return check_login(username, password)
    except sqlite3.IntegrityError:
        return None


def check_login(username, password):
    with _conn() as c:
        row = c.execute("SELECT * FROM users WHERE username=?", (username.strip().lower(),)).fetchone()
    if row and hmac.compare_digest(row["password_hash"], _hash(password, row["salt"])):
        return {"id": row["id"], "username": row["username"], "nom": row["nom"], "filiere": row["filiere"]}
    return None


def save_score(user_id, filiere, score, total):
    with _conn() as c:
        c.execute(
            "INSERT INTO scores (user_id, filiere, score, total) VALUES (?,?,?,?)",
            (user_id, filiere, score, total),
        )


def get_scores(user_id):
    with _conn() as c:
        rows = c.execute(
            "SELECT filiere, score, total, created_at FROM scores WHERE user_id=? ORDER BY id DESC",
            (user_id,),
        ).fetchall()
    return [dict(r) for r in rows]


def count_ai_today(user_id):
    with _conn() as c:
        row = c.execute(
            "SELECT COUNT(*) AS n FROM ai_usage WHERE user_id=? AND date(created_at)=date('now')",
            (user_id,),
        ).fetchone()
    return row["n"]


def add_ai_usage(user_id):
    with _conn() as c:
        c.execute("INSERT INTO ai_usage (user_id) VALUES (?)", (user_id,))
