import sqlite3

def create_database():
    # Connect to the SQLite database (or create it if it doesn't exist)
    conn = sqlite3.connect('tumorvision.db')
    cursor = conn.cursor()

    # Create 'users' table
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS users (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            email TEXT NOT NULL UNIQUE,
            password TEXT NOT NULL
        )
    ''')

    # Create 'images' table with foreign key to 'users' table
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS images (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            user_id INTEGER NOT NULL,
            path TEXT NOT NULL,
            upload_date DATETIME DEFAULT CURRENT_TIMESTAMP,
            prediction_results TEXT,
            confidence REAL,
            prediction_date DATETIME,
            FOREIGN KEY (user_id) REFERENCES users(id)
        )
    ''')

    # Create 'reports' table with foreign keys to 'users' and 'images' tables
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS reports (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            user_id INTEGER NOT NULL,
            image_id INTEGER NOT NULL,
            report_date DATETIME DEFAULT CURRENT_TIMESTAMP,
            report_text TEXT NOT NULL,
            FOREIGN KEY (user_id) REFERENCES users(id),
            FOREIGN KEY (image_id) REFERENCES images(id)
        )
    ''')

    # Commit the changes and close the connection
    conn.commit()
    conn.close()

if __name__ == '__main__':
    create_database()
    print('Database "tumorvision.db" with tables and relationships created successfully.')
