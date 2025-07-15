from cryptography.fernet import Fernet
import os

# Generate key and save it
def generate_key():
    key = Fernet.generate_key()
    with open("secret.key", "wb") as key_file:
        key_file.write(key)
    print("🔐 Key generated and saved as secret.key")

# Load key
def load_key():
    return open("secret.key", "rb").read()

# Encrypt file
def encrypt_file(filename):
    key = load_key()
    f = Fernet(key)

    with open(filename, "rb") as file:
        file_data = file.read()

    encrypted_data = f.encrypt(file_data)

    with open(filename, "wb") as file:
        file.write(encrypted_data)

    print(f"✅ File '{filename}' encrypted successfully.")

# Decrypt file
def decrypt_file(filename):
    key = load_key()
    f = Fernet(key)

    with open(filename, "rb") as file:
        encrypted_data = file.read()

    decrypted_data = f.decrypt(encrypted_data)

    with open(filename, "wb") as file:
        file.write(decrypted_data)

    print(f"✅ File '{filename}' decrypted successfully.")

# Menu UI
def menu():
    while True:
        print("\n===== Advanced Encryption Tool =====")
        print("1. Generate Key")
        print("2. Encrypt a File")
        print("3. Decrypt a File")
        print("4. Exit")
        choice = input("Enter your choice: ")

        if choice == "1":
            generate_key()
        elif choice == "2":
            filename = input("Enter the filename to encrypt (with extension): ")
            encrypt_file(filename)
        elif choice == "3":
            filename = input("Enter the filename to decrypt (with extension): ")
            decrypt_file(filename)
        elif choice == "4":
            print("Exiting the program.")
            break
        else:
            print("Invalid choice. Try again.")

menu()
