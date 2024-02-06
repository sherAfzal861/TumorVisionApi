import sqlite3
from werkzeug.security import generate_password_hash

def add_user(username, email, password):
    conn = sqlite3.connect('tumorvision.db')
    cursor = conn.cursor()

    # Hash the password before storing it in the database
    hashed_password = generate_password_hash(password, method='pbkdf2:sha256')

    # Insert the new user into the 'users' table
    cursor.execute('INSERT INTO users (name, email, password) VALUES (?, ?, ?)', (username, email, hashed_password))

    conn.commit()
    conn.close()