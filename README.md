# Random Password Generator

A command-line tool that generates secure, random passwords of a user-chosen length. 

## Features

- Asks the user for a password length and validates the input
- Enforces a minimum length of 8 characters
- Generates passwords from letters (a-z, A-Z) and digits (0-9)
- Optionally includes symbols (`!@#$%^&*` and other punctuation)
- Uses `secrets.choice()` for cryptographically secure selection
- Builds the password with `''.join()` for linear O(N) efficiency
- Displays the password's entropy in bits

## Requirements

- Python **3.6 or higher** (the `secrets` module was introduced in 3.6)
- No external packages needed. Only the standard library is used (`secrets`, `string`, `math`).

## How to Run

1. Save the code as `password_generator.py`.
2. Open a terminal in the same folder.
3. Run: python password_generator.py

## Example Output

Enter password length (min 8): 12
Include symbols? (y/n): y
Password: q#R8m!Zx2@Lp
Entropy: 78.7 bits

Without symbols:

Enter password length (min 8): 12
Include symbols? (y/n): n
Password: k7Qx2mZ9aR4b
Entropy: 71.5 bits

Invalid input is handled gracefully:

Enter password length (min 8): abc
Please enter a whole number.
Enter password length (min 8): 5
Too short. Use at least 8 characters.
Enter password length (min 8): 16

### Entropy formula

E = L x log2(R)

- **E**: entropy in bits
- **L**: password length
- **R**: size of the character pool

A higher value means the password is harder to guess or brute-force.

## File structure
random-password-generator/
├── password_generator.py   # Main program (your code)
└──   README.md               # Project documentation

## Author:
Muhammad Khan