import hashlib
import os


FILE_NAME = "login.txt"


# ----------------------------
# Password Security
# ----------------------------

def hash_password(password):
    """Encrypt password using SHA-256."""
    return hashlib.sha256(password.encode()).hexdigest()


# ----------------------------
# File Handling
# ----------------------------

def create_file():
    """Create login file if it doesn't exist."""
    if not os.path.exists(FILE_NAME):
        open(FILE_NAME, "w").close()


def load_users():
    """Load users from file into a dictionary."""
    users = {}

    with open(FILE_NAME, "r") as file:
        for line in file:
            try:
                username, password = line.strip().split(",")
                users[username] = password
            except ValueError:
                continue

    return users


def save_user(username, password):
    """Save a new user to the file."""
    with open(FILE_NAME, "a") as file:
        file.write(f"{username},{password}\n")


# ----------------------------
# Account Functions
# ----------------------------

def create_account(users):
    print("\n--- Create Account ---")

    username = input("Create username: ").strip()

    if username in users:
        print("Username already exists.")
        return

    if len(username) < 3:
        print("Username must be at least 3 characters.")
        return

    password = input("Create password: ").strip()

    if len(password) < 5:
        print("Password must be at least 5 characters.")
        return

    hashed_password = hash_password(password)

    save_user(username, hashed_password)
    users[username] = hashed_password

    print("Account created successfully!")


def login(users):
    print("\n--- Login ---")

    attempts = 3

    while attempts > 0:
        username = input("Username: ").strip()
        password = input("Password: ").strip()

        hashed_password = hash_password(password)

        if username in users and users[username] == hashed_password:
            print(f"\nWelcome, {username}!")
            print("Login successful.")
            return True

        attempts -= 1
        print(f"Incorrect username or password. Attempts left: {attempts}")

    print("Too many failed attempts.")
    return False


# ----------------------------
# Main Program
# ----------------------------

def main():

    create_file()

    users = load_users()

    while True:

        print("""
=====================
   LOGIN SYSTEM
=====================

1. Login
2. Create Account
3. Exit
""")

        choice = input("Choose: ")

        if choice == "1":
            login(users)

        elif choice == "2":
            create_account(users)

        elif choice == "3":
            print("Goodbye!")
            break

        else:
            print("Invalid choice.")


main()






    







