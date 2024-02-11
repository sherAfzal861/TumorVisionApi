from models import Users
from config import db
from werkzeug.security import generate_password_hash,check_password_hash
def get_user_by_email(email):
    user = Users.query.filter_by(email=email).first()

    # Return the user if found, otherwise return None
    return user

def check_password(password1, password2):
        return check_password_hash(password1, password2)