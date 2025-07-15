# ADVANCED-ENCRYPTION-TOOL

*COMPANY*: CODTECH IT SOLUTIONS

*NAME*: TANUSHREE PATRA

*INTERN ID*: CT08DG608

*DOMAIN*: CYBER SECURITY & ETHICAL HACKING

*DURATION*: 8 WEEKS

*MENTOR*: NEELA SANTOSH KUMAR

*DESCRIPTION*:

The objective of this task was to develop a robust encryption and decryption tool capable of securing files using an advanced cryptographic algorithm. The primary goal was to ensure confidentiality by building a user-friendly application that allows the encryption of sensitive files and their subsequent decryption when needed. The algorithm chosen for implementation was AES-256 (Advanced Encryption Standard), known for its strong security and efficiency.

To build this tool, I used Python as the programming language and incorporated the cryptography library, which offers a high-level interface for secure encryption operations. I started by installing the cryptography package using the pip module in the VS Code terminal. Then I created a dedicated project folder and added the Python script file named encryption_tool.py.

The tool is modular and operates via a simple menu-driven interface, providing the following functionalities:

Key Generation:
The tool generates a symmetric encryption key using Fernet.generate_key() and saves it in a file named secret.key. This key is crucial, as it is used for both encryption and decryption operations.

File Encryption:
When the user selects this option, they are prompted to enter the filename (with extension) of the file they want to encrypt. The tool reads the file in binary mode, loads the key from secret.key, and uses the AES encryption mechanism (via Fernet) to encrypt the file content. The encrypted data is then written back to the same file.

File Decryption:
This option allows users to decrypt a previously encrypted file. Again, the filename is taken as input, the file is read, and the data is decrypted using the same key. The original content is restored in the file after successful decryption.

The menu is designed in a loop, allowing users to perform multiple operations without restarting the program. All file operations are handled securely using binary read/write modes to ensure compatibility with different file types.

To test the tool, I created a sample .txt file and performed both encryption and decryption operations. The encryption successfully obscured the readable content, and the decryption restored the original message, verifying the correctness of the logic.

Technologies & Libraries Used:
Language: Python 

Libraries: cryptography (includes Fernet, cffi, pycparser)

Development Environment: Visual Studio Code

Interface: Command-line (menu-driven)

Overall, the tool meets the requirement of being both secure and user-friendly, with minimal input needed from the user. The key-based symmetric encryption method ensures that the files are safe from unauthorized access, provided the key remains confidential.

*OUTPUT*:

