import getpass
from auth import authenticate, get_user_role
from rbac import check_permission
import bank_operations as ops
from util import clear_screen, wait_and_clear 

def main():
    clear_screen()
    print("=== Welcome to the International Bank System ===")
    
    # Ask for username and password
    username = input("Username: ")
    password = getpass.getpass("Password: ")

    # Authenticate user
    if not authenticate(username, password):
        return

    # Retrieve user's role
    role = get_user_role(username)

    # Define possible actions mapped by input keys
    actions = {
        "1": ("View Balance", "view_balance", ops.view_balance),
        "2": ("View Statement", "view_statement", ops.view_statement),
        "3": ("Manage Accounts", "manage_accounts", ops.manage_accounts),
        "4": ("Create User", "create_user", ops.create_user)
    }

    while True:
        print("\n=== Available Actions ===")
        for key, (description, _, _) in actions.items():
            print(f"{key}. {description}")
        print("q. Quit")

        choice = input("\nSelect an option: ")

        if choice.lower() == "q":
            print("Exiting the system. Goodbye!")
            break

        if choice not in actions:
            print("Invalid option. Please try again.")
            continue

        description, action_name, action_func = actions[choice]

        # Check if the user's role allows this action
        if check_permission(role, action_name):
            print(f"\n--- {description} ---")
            action_func()
        else:
            print("Access Denied: You don't have permission to perform this action.")
        
        wait_and_clear()

if __name__ == "__main__":
    main()