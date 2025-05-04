from data import users

# Authenticates a user based on the username and password provided.
def authenticate(username, password):
    if username in users and users[username]["password"] == password:
        print(f"[INFO] User '{username}' authenticated successfully.")
        return True
    print(f"[WARN] Authentication failed for user '{username}'.")
    return False


# Returns the role associated with the given username.
def get_user_role(username):
    return users[username]["role"]