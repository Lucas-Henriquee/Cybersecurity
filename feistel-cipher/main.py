from sample_text import get_sample_text
from cipher_engine import feistel_encrypt, feistel_decrypt, generate_keys
from util import clear_screen, wait_and_clear

# Encrypt the input flow
def encrypt_flow(text):
    clear_screen()
    print("\nOriginal text:" + text)

    keys = generate_keys()
    encrypted = feistel_encrypt(text, keys)

    print("\n=== Encryption Result ===\n")
    print(f"Encrypted (Base64): {encrypted}")
    wait_and_clear()

# Decrypt the input flow
def decrypt_flow():
    clear_screen()
    text = input("\nEnter encrypted text (Base64): ")

    keys = generate_keys()  
    decrypted = feistel_decrypt(text, keys)

    print("\n=== Decryption Result ===\n")
    print(f"Decrypted: {decrypted}")
    wait_and_clear()

# Main menu
def show_menu():
    while True:
        print("\n=== Feistel Cipher Tool ===")
        print("1. Encrypt the default sample text")
        print("2. Encrypt your own text")
        print("3. Decrypt your own text")
        print("0. Exit")

        choice = input("Choose an option: ").strip()

        if choice == "1":
            text = get_sample_text()
            encrypt_flow(text)
        elif choice == "2":
            text = input("Enter your text: ")
            encrypt_flow(text)
        elif choice == "3":
            decrypt_flow()
        elif choice == "0":
            print("Exiting...")
            break
        else:
            print("Invalid option. Please try again.")

if __name__ == "__main__":
    show_menu()