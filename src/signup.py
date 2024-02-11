from models import Users
from config import db
from werkzeug.security import generate_password_hash

def add_user(username, email, password):

    # Hash the password before storing it in the database
    hashed_password = generate_password_hash(password, method='pbkdf2:sha256')

    new_user = Users(name=username, email=email, password=hashed_password)

    # Add the user to the session and commit
    db.session.add(new_user)
    db.session.commit()