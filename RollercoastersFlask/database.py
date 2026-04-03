import sqlite3
from pathlib import Path

DB_PATH = "coasters.db"

# ---------- Create a data base for favorite Coasters ---------- #
def init_db():
    """Create the database and table if they do not exist."""
    if not Path(DB_PATH).exists():
        conn = sqlite3.connect(DB_PATH)
        cur = conn.cursor()
        cur.execute("""
            CREATE TABLE favorites (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                coaster_name TEXT NOT NULL,
                added_at DATETIME NOT NULL
            )
        """)
        conn.commit()
        conn.close()

# ---------- Prevents database overflows by allowing a maximum of 5 coasters ---------- #
def enforce_limit():
    conn = sqlite3.connect(DB_PATH)
    cur = conn.cursor()
    cur.execute("""
        DELETE FROM favorites
        WHERE id NOT IN (
            SELECT id FROM favorites ORDER BY added_at DESC LIMIT 5
        )
    """)
    conn.commit()
    conn.close()


# ---------- Responsible for what is included in the list, these are the time and the name of the coaster ---------- #
def add_coaster_to_db(name):
    conn = sqlite3.connect(DB_PATH)
    cur = conn.cursor()
    cur.execute(
        "INSERT INTO favorites (coaster_name, added_at) VALUES (?, datetime('now'))",
        (name,)
    )
    conn.commit()
    conn.close()

    enforce_limit()


# ---------- Responsible for showing te list of favorite coasters ---------- #
def get_all_coasters():
    """Return all saved coasters."""
    conn = sqlite3.connect(DB_PATH)
    cur = conn.cursor()
    cur.execute("SELECT coaster_name, added_at FROM favorites ORDER BY added_at DESC")
    rows = cur.fetchall()
    conn.close()
    return rows
