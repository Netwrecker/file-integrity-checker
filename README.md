# file-integrity-checker

**COMPANY** : CODTECH IT SOLUTIONS
**NAME**  : DAMANDEEP KUMAR
**INTERN ID**  : CT6MTNGN
**DOMAIN**  : CYBER SECURITY
**DURATION**  : 6 MONTHS
**MENTOR**  : NEELA SANTOSH

# DESCRIPTION

The provided script is a file integrity checker and monitor that allows users to perform various tasks. Here's a brief description of the script:

The script provides an easy-to-use interface through a menu system, allowing users to choose from the following options:

**Check File Integrity**: Users can check the integrity of a file by providing the file path and the stored hash. The script compares the current hash of the file with the stored hash and displays a message indicating whether the file has been modified or not.

**Store File Hash**: Users can store the SHA-256 hash of a file by providing the file path. The script calculates the hash of the file and displays it to the user.

**Monitor File Changes:** Users can monitor changes in a file by providing the file path. The script continuously checks the file for changes and displays a message indicating whether the file has been modified or not.

**Monitor Directory Changes:** Users can monitor changes in a directory and its subdirectories by providing the directory path. The script continuously checks the directory and its files for changes and displays a message indicating whether a file has been modified or added.

**Exit:** Users can exit the script.

The script uses the os module to traverse directories and the hashlib module to generate SHA-256 hashes of files. The script runs in an infinite loop and checks for changes every second.


# USAGE 
Run the script using the command _python3_ _file_integrity_checker.py_, where _file_integrity_checker.py_ is the name of your Python script file.

**Choose an option from the menu:**
Enter '1' to check the integrity of a file. You will be prompted to enter the file path and the stored hash.
Enter '2' to store the hash of a file. You will be prompted to enter the file path.
Enter '3' to monitor file changes. You will be prompted to enter the file path.
Enter '4' to monitor directory changes. You will be prompted to enter the directory path.
Enter '5' to exit the script.
The script will perform the selected operation and display the result.

