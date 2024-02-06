import sqlite3
from werkzeug.security import generate_password_hash,check_password_hash
def get_user_by_email(email):
    conn = sqlite3.connect('tumorvision.db')
    cursor = conn.cursor()
    print(email)
    cursor.execute('SELECT * FROM users WHERE email = ?', (email,))
    user = cursor.fetchone()

    conn.close()
    print(user)
    return user

def check_password(password1, password2):
        return check_password_hash(password1, password2)