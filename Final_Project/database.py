import sqlite3
import os

DB_FOLDER = 'db'
DB_NAME = 'app_data.db'

def get_db_connection():
    if not os.path.exists(DB_FOLDER):
        os.makedirs(DB_FOLDER)
    
    conn = sqlite3.connect(os.path.join(DB_FOLDER, DB_NAME))
    return conn

def initialize_db():
    """Creates the Users table if it doesn't exist."""
    conn = get_db_connection()
    cursor = conn.cursor()
    
    # Create Users Table
    # We store the salt and the hash separately for security
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS users (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            username TEXT UNIQUE NOT NULL,
            password_hash TEXT NOT NULL,
            salt TEXT NOT NULL
        )
    ''')
    
    conn.commit()
    conn.close()