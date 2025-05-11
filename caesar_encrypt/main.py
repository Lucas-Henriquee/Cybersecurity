from sample_text import get_sample_text
from encrypt import caesar_encrypt, caesar_decrypt
from analysis import frequency_analysis
from util import clear_screen, wait_and_clear

def encrypt_flow(text):
    clear_screen()
    
    print("Original text:\n" + text)

    # Ask user for the Caesar shift value
    k = int(input("\nEnter shift value (key k): "))
    
    # Encrypt the input text using Caesar cipher
    encrypted = caesar_encrypt(text, k)

    clear_screen()

    print(f"\n=== Encryption Result with shift value {k} ===")
    print(f"Original : {text}\n")
    print(f"Encrypted: {encrypted}")

    print("\n---")
    print("1. Frequency analysis")
    print("2. Return to menu")

    choice = input("Choose an option: ").strip()

    if choice == "1":
        frequency_analysis(encrypted)

    wait_and_clear()

def decrypt_flow():
    clear_screen()
    
    text = input("Enter encrypted text: ")
    k = int(input("Enter shift value (key k) used to encrypt: "))

    # Decrypt using the Caesar cipher
    decrypted = caesar_decrypt(text, k)

    clear_screen()
    print(f"\n=== Decryption Result with shift value {k} ===")
    print(f"Encrypted: {text}\n")
    print(f"Decrypted: {decrypted}")

    print("\n---")
    print("1. Frequency analysis")
    print("2. Return to menu")

    choice = input("Choose an option: ").strip()

    if choice == "1":
        frequency_analysis(decrypted)

    wait_and_clear()

def show_menu():
    while True:
        print("\n=== Caesar Cipher Tool ===")
        print("1. Encrypt sample text")
        print("2. Encrypt your own text")
        print("3. Decrypt your own text")
        print("0. Exit")

        choice = input("Choose an option: ").strip()
            
        # Load sample text and start encryption
        if choice == "1":
            text = get_sample_text()
            encrypt_flow(text)
        
        # Let user input their own text
        elif choice == "2":
            text = input("Enter your text: ")
            encrypt_flow(text)

        # Start decryption flow
        elif choice == "3":
            decrypt_flow()
        
        elif choice == "0":
            print("Exiting...")
            break
        
        else:
            print("Invalid option. Try again.")

if __name__ == "__main__":
    show_menu()