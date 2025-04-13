import os
import hashlib
import time

def get_file_hash(file_path):
    """
    Calculate the SHA-256 hash of a file.
    """
    with open(file_path, 'rb') as file:
        file_hash = hashlib.sha256()
        while True:
            data = file.read(65536)
            if not data:
                break
            file_hash.update(data)
    return file_hash.hexdigest()

def check_file_integrity(file_path, stored_hash):
    """
    Check the integrity of a file by comparing its hash with a stored hash.
    """
    current_hash = get_file_hash(file_path)
    if current_hash == stored_hash:
        print(f"File '{file_path}' is not modified.")
    else:
        print(f"File '{file_path}' has been modified!")

def store_file_hash(file_path):
    """
    Store the SHA-256 hash of a file.
    """
    file_hash = get_file_hash(file_path)
    print(f"Stored hash for '{file_path}': {file_hash}")
    return file_hash

def monitor_file_changes(file_path):
    """
    Monitor changes in a file by comparing the current hash with the previous hash.
    """
    previous_hash = None
    while True:
        current_hash = get_file_hash(file_path)
        if current_hash != previous_hash:
            if previous_hash is not None:
                print(f"File '{file_path}' has been modified!")
            previous_hash = current_hash
        else:
            print(f"File '{file_path}' is not modified.")
        time.sleep(1)  # Check every second

def monitor_directory_changes(directory_path):
    """
    Monitor changes in a directory and its subdirectories by comparing the current hashes with the previous hashes.
    """
    previous_hashes = {}
    while True:
        current_hashes = {}
        for root, dirs, files in os.walk(directory_path):
            for file in files:
                file_path = os.path.join(root, file)
                current_hashes[file_path] = get_file_hash(file_path)

        for file_path, current_hash in current_hashes.items():
            if file_path not in previous_hashes or current_hash != previous_hashes[file_path]:
                if file_path in previous_hashes:
                    print(f"File '{file_path}' has been modified!")
                else:
                    print(f"New file '{file_path}' has been added.")

        previous_hashes = current_hashes
        time.sleep(1)  # Check every second

# Main menu
while True:
    print("\nFile/Directory Integrity Checker and Monitor")
    print("1. Check File Integrity")
    print("2. Store File Hash")
    print("3. Monitor File Changes")
    print("4. Monitor Directory Changes")
    print("5. Exit")

    choice = input("Enter your choice (1-5): ")

    if choice == '1':
        file_path = input("Enter the file path: ")
        stored_hash = input("Enter the stored hash: ")
        check_file_integrity(file_path, stored_hash)
    elif choice == '2':
        file_path = input("Enter the file path: ")
        stored_hash = store_file_hash(file_path)
    elif choice == '3':
        file_path = input("Enter the file path: ")
        monitor_file_changes(file_path)
    elif choice == '4':
        directory_path = input("Enter the directory path: ")
        monitor_directory_changes(directory_path)
    elif choice == '5':
        break
    else:
        print("Invalid choice. Please try again.")
