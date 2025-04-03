def login(users, username, password):
    return f"Welcome, {username}!" if users.get(username) == password else "Invalid username or password."

def create_account(users, username, password):
    if username in users:
        return "Username already exists."
    users[username] = password
    profiles[username] = ""  # Create an empty profile for the new user
    return "Account created successfully!"

def add_bio(profiles, username, bio):
    profiles[username] = bio
    return "Bio updated!"

def view_profiles(profiles):
    if not profiles:
        return "No profiles available."
    return "\n".join([f"{user}: {bio if bio else 'No bio available'}" for user, bio in profiles.items()])

users = {"admin": "password123", "user": "mypassword"}
profiles = {user: "" for user in users}  # Initialize profiles for all users

print("DEBUG: Program started")  # Debugging line

while True:
    print("DEBUG: Loop is running")  # Debugging line
    print("\n1. Login\n2. Create Account\n3. Add/Update Bio\n4. View Profiles\n5. Exit")
    choice = input("Choose an option: ")

    if choice == "1":
        print(login(users, input("Username: "), input("Password: ")))
    elif choice == "2":
        print(create_account(users, input("New Username: "), input("New Password: ")))
    elif choice == "3":
        username = input("Username: ")
        if username in users:
            print(add_bio(profiles, username, input("Enter your bio: ")))
        else:
            print("Username not found. Please log in or create an account first.")
    elif choice == "4":
        print(view_profiles(profiles))
    elif choice == "5":
        print("Goodbye!")
        break
    else:
        print("Invalid choice. Try again.")