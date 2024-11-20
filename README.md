# Password Strength Checker

## Overview

The Password Strength Checker is a Python application designed to evaluate and categorize passwords based on various strength criteria. The tool checks for the following features:

- Length of the password
- Presence of uppercase and lowercase letters
- Use of digits and special characters

The application helps users create more secure passwords by providing them with feedback and suggestions on improving their password strength.

## Key Features

### Password Strength Evaluation:
- Categorizes passwords as **Weak**, **Moderate**, or **Strong** based on criteria like length and character variety.

### Suggestions for Improvement:
- The tool offers suggestions for users to strengthen weak passwords.

### Save and Load Passwords:
- Allows users to save tested passwords and load previously saved passwords from a file.

### Interactive Text-Based Interface:
- The app provides a simple and intuitive menu-based interface for users to interact with.

## Technical Details

### Password Class:
The core component of this project is the `Password` class that handles password evaluation.

#### Attributes:
- **`__password`**: A private attribute that stores the password.
- **`length`**: A public attribute that stores the length of the password.
- **`strength`**: A public attribute that stores the password's strength ("Weak," "Moderate," "Strong").

#### Methods:
- **`evaluate_strength()`**: This method evaluates the password’s strength based on length and character variety.
- **`__str__()`**: This method returns a string representation of the password, including its length and strength.
- **`__eq__()`**: This method compares two password objects for equality.

## Python Constructs Used

- **Lists, Tuples, Sets, Dictionaries**: Used to manage password criteria and feedback messages.
- **Iteration & Conditionals**: Utilized loops and `if` statements to evaluate passwords against various conditions.
- **Exception Handling**: A `try` block is included to handle errors such as file reading errors when loading passwords.
- **File I/O**: Users can save passwords to a file and retrieve them later.

## Unit Tests

To ensure the Password Strength Checker works correctly, unit tests were written to validate the strength evaluation logic.

### Test Cases:
- **Weak Password Test**: Checks that a password like "123" is categorized as **Weak**.
- **Strong Password Test**: Ensures that a password like "StrongPass1!" is categorized as **Strong**.

## How to Run

1. Clone the repository:
   ```bash
   git clone https://github.com/khudeja0208/password-strength-checker/tree/main/kbegum_final_project
