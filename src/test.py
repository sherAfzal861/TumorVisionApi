# from config import app, db
# from models import Users

# def print_all_users():
#     # Query all users from the database
#     all_users = Users.query.all()
#     print(all_users)
#     # Print information of each user
#     for user in all_users:
#         print(f"User ID: {user.id}")
#         print(f"Name: {user.name}")
#         print(f"Email: {user.email}")
#         print("")

# if __name__ == "__main__":
#     # Ensure the database is initialized
#     with app.app_context():
#         # db.create_all()

#         # Print all users
#         print("All Users:")
#         print("-" * 20)
#         print_all_users()

from werkzeug.security import generate_password_hash
from models import Users
from config import db,app

def add_user(username, email, password):
    # Hash the password
    hashed_password = generate_password_hash(password)

    # Create a new user instance
    new_user = Users(name=username, email=email, password=hashed_password)

    # Add the user to the session and commit
    db.session.add(new_user)
    db.session.commit()

    print(f"User '{username}' with email '{email}' added successfully.")

def get_user_by_email(email):
    # Query the database to find the user by email
    user = Users.query.filter_by(email=email).first()

    # Return the user if found, otherwise return None
    return user

# Example usage
if __name__ == "__main__":
    # Provide the email to search for
    email = "john@example.com"

    # Get the user by email
    with app.app_context():
        user = get_user_by_email(email)

        # Print the user information if found
        if user:
            print(f"User found with email '{email}':")
            print(f"ID: {user.id}")
            print(f"Name: {user.name}")
            print(f"Email: {user.email}")
            print(f"Password: {user.password}")
        else:
            print(f"No user found with email '{email}'.")

        # Provide sample user data
        # username = "hashimkhan"
        # email = "hashim@example.com"
        # password = "password123"

        # # Add the user
        # add_user(username, email, password)
