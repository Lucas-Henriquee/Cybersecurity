import os

def clear_screen():
    os.system("cls" if os.name == "nt" else "clear")

def wait_and_clear():
    input("\nPress Enter to continue...")
    clear_screen()