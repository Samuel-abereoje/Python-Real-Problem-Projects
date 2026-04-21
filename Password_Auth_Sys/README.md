Password Authentication System (Python)

OVERVIEW

This project is a command-line password authentication system built with Python. It simulates a basic login workflow with input validation, password strength analysis, and controlled access attempts.

The goal is to demonstrate core Python concepts including:

Functions
Loops
Exception handling
Input validation
Conditional logic


FEATURES

Maximum login attempts limit
Password strength checker (Weak → Very Strong)
Input validation (prevents empty or invalid entries)
Exception handling
Clear user feedback on each attempt

HOW IT WORKS

User is prompted to enter a password.
Input is validated to ensure it is not empty or whitespace.
Password strength is analyzed and displayed.
System compares input with the stored password.
Access is granted if correct.
After 3 failed attempts, access is denied.


CONFIGURATION

You can modify the following variables in the script:

MAX_ATTEMPTS = 3
PASSWORD = "python123"

HOW TO RUN

Clone the repository:
git clone https://github.com/your-username/password-auth-system.git
Navigate into the project folder:
cd password-auth-system
Run the script:
python main.py


By building this project, you gain hands-on experience in:

Writing clean and modular Python code
Handling user input safely
Designing basic authentication logic
Structuring beginner-friendly backend systems

LICENSE

This project is open-source and available for learning and educational use.
This project is for learning purposes only and is not production-readY because it has its limitations.