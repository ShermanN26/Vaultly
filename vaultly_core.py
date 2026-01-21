import json
import datetime
from cryptography.fernet import Fernet
import os

class VaultlyBank:
    def __init__(self, filename="vault_encrypted.dat", key_file="vault.key"):
        self.filename = filename
        self.key_file = key_file
        self.key = self.load_key()
        self.fernet = Fernet(self.key)
        self.accounts = self.load_data()

    def load_key(self):
        if os.path.exists(self.key_file):
            with open(self.key_file, "rb") as f:
                return f.read()
        key = Fernet.generate_key()
        with open(self.key_file, "wb") as f:
            f.write(key)
        return key

    def load_data(self):
        if not os.path.exists(self.filename):
            return {}
        try:
            with open(self.filename, "rb") as f:
                encrypted_data = f.read()
            decrypted_data = self.fernet.decrypt(encrypted_data)
            return json.loads(decrypted_data.decode())
        except Exception:
            return {}

    def save_data(self):
        data_str = json.dumps(self.accounts).encode()
        encrypted_data = self.fernet.encrypt(data_str)
        with open(self.filename, "wb") as f:
            f.write(encrypted_data)

    def signup(self):
        name = input("Enter Name: ")
        pin = input("Create 4-digit PIN: ")
        self.accounts[name] = {"pin": pin, "balance": 0.0, "history": []}
        self.save_data()
        print("Account secured and saved!")

# Usage
bank = VaultlyBank()
bank.signup()
