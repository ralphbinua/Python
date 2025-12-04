import hashlib
import os
from .database import get_db_connection

def register_user(username, password):
    conn = get_db_connection()
    cursor = conn.cursor()

    # Check if user exists
    cursor.execute("SELECT * FROM users WHERE username = ?", (username,))
    if cursor.fetchone():
        conn.close()
        return False, "Username already exists!"

    # Generate a random salt (32 bytes)
    salt = os.urandom(32)

    # Hash the password with the salt
    # PBKDF2_HMAC is safer than simple sha256
    key = hashlib.pbkdf2_hmac(
        'sha256',
        password.encode('utf-8'),
        salt,
        100000
    )

    # Store salt and key as Hex strings
    salt_hex = salt.hex()
    key_hex = key.hex()

    cursor.execute("INSERT INTO users (username, password_hash, salt) VALUES (?, ?, ?)",
                   (username, key_hex, salt_hex))
    conn.commit()
    conn.close()
    return True, "Registration Successful!"

def login_user(username, password):
    conn = get_db_connection()
    cursor = conn.cursor()

    cursor.execute("SELECT password_hash, salt FROM users WHERE username = ?", (username,))
    data = cursor.fetchone()
    conn.close()

    if data:
        stored_hash = data[0]
        stored_salt = data[1]

        # Convert hex salt back to bytes
        salt_bytes = bytes.fromhex(stored_salt)

        # Hash the input password with the retrieved salt
        new_key = hashlib.pbkdf2_hmac(
            'sha256',
            password.encode('utf-8'),
            salt_bytes,
            100000
        )

        # Compare the new hash with the stored hash
        if new_key.hex() == stored_hash:
            return True, "Login Successful"

    return False, "Invalid Username or Password"