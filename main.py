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
    return "\n".join([f"{user}: {bio if bio else 'No bio available'}" for user, bio in profiles.items()]) or "No profiles available."

def post_question(forums, username, question):
    forums.append({"user": username, "question": question, "responses": []})
    return "Question posted!"

def respond_to_question(forums, question_index, response):
    if 0 <= question_index < len(forums):
        forums[question_index]["responses"].append(response)
        return "Response added!"
    return "Invalid question number."

def view_questions(forums):
    if not forums:
        return "No questions available."
    result = []
    for i, q in enumerate(forums):
        result.append(f"Q{i+1} by {q['user']}: {q['question']}")
        for j, r in enumerate(q["responses"]):
            result.append(f"  - Response {j+1}: {r}")
    return "\n".join(result)

# Initialize data
users = {"admin": "password123", "user": "mypassword"}
profiles = {user: "" for user in users}
forums = []

# Main menu loop
while True:
    print("\n1. Login\n2. Create Account\n3. Add/Update Bio\n4. View Profiles\n5. Questions/Forums\n6. Exit")
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
        print("\n1. Post a Question\n2. Respond to a Question\n3. View Questions")
        forum_choice = input("Choose an option: ")
        if forum_choice == "1":
            username = input("Username: ")
            if username in users:
                question = input("Enter your question: ")
                print(post_question(forums, username, question))
            else:
                print("Username not found. Please log in or create an account first.")
        elif forum_choice == "2":
            print(view_questions(forums))
            try:
                question_index = int(input("Enter the question number to respond to: ")) - 1
                response = input("Enter your response: ")
                print(respond_to_question(forums, question_index, response))
            except ValueError:
                print("Invalid input. Please enter a valid question number.")
        elif forum_choice == "3":
            print(view_questions(forums))
        else:
            print("Invalid choice. Try again.")
    elif choice == "6":
        print("Goodbye!")
        break
    else:
        print("Invalid choice. Try again.")