# Password Generator + Encrypted Password Saver

This is a simple Python program that:
- Generates strong random passwords (letters + numbers + symbols)
- Checks the password contains **at least one letter, one number, and one symbol**
- Encrypts the password using **Fernet encryption**
- Saves the encrypted password to a `password.txt` file
- Lets you recall a saved password by website name and decrypt it

---

## Features
- Generate strong passwords  
- Ensures password includes letters, numbers, and symbols  
- Encrypts passwords before saving  
- Saves passwords with the website name in `password.txt`  
- Recall + decrypt saved passwords by entering the website name  

---

## Requirements
- Python 3.x  
- `cryptography` library

Install cryptography:
```bash
pip install cryptography
```