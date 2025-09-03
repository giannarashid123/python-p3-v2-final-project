from models import Session, User

def create_user():
    session = Session()
    username = input("Username: ")
    email = input("Email: ")

    if session.query(User).filter_by(username=username).first():
        print("Username already exists.")
        return

    user = User(username=username, email=email)
    session.add(user)
    session.commit()
    print(f"User '{username}' created.")

def login_user():
    session = Session()
    username = input("Username: ")
    user = session.query(User).filter_by(username=username).first()

    if user:
        print(f"Welcome back, {username}!")
    else:
        print("User not found.")

def update_user_email():
    session = Session()
    username = input("Username: ")
    user = session.query(User).filter_by(username=username).first()

    if not user:
        print("User not found.")
        return

    new_email = input("New email: ")
    user.email = new_email
    session.commit()
    print("Email updated.")

def delete_user():
    session = Session()
    username = input("Username to delete: ")
    user = session.query(User).filter_by(username=username).first()

    if not user:
        print("User not found.")
        return

    confirm = input(f"Delete '{username}'? (y/n): ")
    if confirm.lower() == 'y':
        session.delete(user)
        session.commit()
        print("User deleted.")
    else:
        print("Canceled.")

def exit_program():
    print("Goodbye!")
    exit()
