# Secure Login System

## Description

This project is a command-line authentication system built with Python. It allows users to create accounts and securely log in using saved credentials.

Unlike a basic login system, this version improves security by **hashing passwords** before storing them. Passwords are never saved as plain text.

User information is stored locally in a `login.txt` file.

---

## Features

- Create new user accounts
- Secure password hashing using SHA-256
- Login with saved credentials
- Prevent duplicate usernames
- Password and username validation
- Three login attempt limit
- Automatic creation of required files
- Error handling for invalid file data
- Simple command-line interface

---

## Technologies Used

- Python 3
- File handling
- Dictionaries
- SHA-256 encryption hashing
- Command-line input/output

---

## Installation

### 1. Download the project

Clone the repository or download the files.

Example:

```bash
git clone <repository-url>
