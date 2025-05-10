import sqlite3
from sqlite3 import Error


def init_db():
    conn = sqlite3.connect("data/metadata.db")
    cursor = conn.cursor()
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS images (
            id TEXT PRIMARY KEY,
            image_path TEXT NOT NULL,
            mask_path TEXT,
            resolution INTEGER,
            split_group TEXT  # train/test/val
        )
    """)
    conn.commit()
    conn.close()


if __name__ == "__main__":
    init_db()
