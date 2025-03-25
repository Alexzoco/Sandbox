def login(username, password, user_data):
    """
    Function to validate username and password.

    Args:


        username (str): The username input.
        password (str): The password input.
        user_data (dict): A dictionary containing usernames as keys and passwords as values.

    Returns:
        bool: True if login is successful, False otherwise.
    """
    if username in user_data and user_data[username] == password:
        print("Login successful!")
        return True
    else:
        print("Invalid username or password.")
        return False

# Example usage
if __name__ == "__main__":
    # Example user data
    user_data = {
        "user1": "password123",
        "admin": "adminpass",
        "guest": "guestpass"
    }

    # Input from user
    username = input("Enter your username: ")
    password = input("Enter your password: ")

    # Call the login function
    login(username, password, user_data)