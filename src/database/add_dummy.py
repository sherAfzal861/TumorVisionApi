import sqlite3
from werkzeug.security import generate_password_hash

def add_dummy_users():
    # Dummy user data (replace with your own data)
    dummy_users = [
        ('John Doe', 'john@example.com', 'password123'),
        ('Jane Smith', 'jane@example.com', 'securepass'),
        ('Alice Johnson', 'alice@example.com', 'qwerty'),
    ]

    conn = sqlite3.connect('tumorvision.db')
    cursor = conn.cursor()

    # Add dummy users to the 'users' table
    for name, email, password in dummy_users:
        hashed_password = generate_password_hash(password, method='pbkdf2:sha256')
        cursor.execute('INSERT INTO users (name, email, password) VALUES (?, ?, ?)', (name, email, hashed_password))

    # Commit the changes and close the connection
    conn.commit()
    conn.close()

if __name__ == '__main__':
    add_dummy_users()
    print('Dummy users added to the database.')
