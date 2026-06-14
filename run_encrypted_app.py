import os
from cryptography.fernet import Fernet

# Load the encryption key
KEY_FILE = "secret.key"

def load_key():
    """Load encryption key"""
    if not os.path.exists(KEY_FILE):
        print("❌ Error: secret.key not found!")
        print("Run: python encrypt_app.py first")
        exit(1)
    with open(KEY_FILE, "rb") as key_file:
        return key_file.read()

# Read encrypted binary file
with open("app_encrypted.bin", "rb") as f:
    encrypted_code = f.read()

# Decrypt the code
key = load_key()
cipher = Fernet(key)
decrypted_code = cipher.decrypt(encrypted_code).decode()

print("✓ Decrypted and executing encrypted app...")
print("=" * 50)

# Execute the decrypted code
exec(decrypted_code)
