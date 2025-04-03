def login(users, username, password):
    if username in users and users[username] == password:
        return f"Welcome, {username}!"
    else:
        return "Invalid username or password."

def create_account(users, username, password):
    if username in users:
        return "Username already exists. Please choose a different username."
    else:
        users[username] = password
        return "Account created successfully!"


users = {
    "admin": "password123",
    "user": "mypassword"
}

while True:
    print("\n1. Login")
    print("2. Create Account")
    print("3. Exit")
    choice = input("Choose an option: ")

    if choice == "1":
        username = input("Enter username: ")
        password = input("Enter password: ")
        print(login(users, username, password))
    elif choice == "2":
        username = input("Enter a new username: ")
        password = input("Enter a new password: ")
        print(create_account(users, username, password))
    elif choice == "3":
        print("Goodbye!")
        break
    else:
        print("Please try again.")