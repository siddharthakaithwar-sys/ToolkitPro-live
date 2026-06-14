#!/usr/bin/env python3
"""
Run the encrypted app.py
Decrypts and executes the code in memory
"""

import os
import sys
from cryptography.fernet import Fernet

KEY_FILE = "secret.key"
ENCRYPTED_FILE = "app_encrypted.bin"

def load_key():
    """Load encryption key"""
    if not os.path.exists(KEY_FILE):
        print(f"❌ Error: {KEY_FILE} not found!")
        print("\nTo create encrypted app:")
        print("  1. pip install -r requirements.txt")
        print("  2. python encrypt_app.py")
        print("  3. python run_encrypted_app.py")
        sys.exit(1)
    
    with open(KEY_FILE, "rb") as key_file:
        return key_file.read()

def run_encrypted():
    """Decrypt and run the encrypted app"""
    try:
        # Check if encrypted file exists
        if not os.path.exists(ENCRYPTED_FILE):
            print(f"❌ Error: {ENCRYPTED_FILE} not found!")
            print(f"\nRun: python encrypt_app.py")
            sys.exit(1)
        
        print("🔓 Decrypting app...")
        
        # Read encrypted binary
        with open(ENCRYPTED_FILE, "rb") as f:
            encrypted_code = f.read()
        
        # Load key and decrypt
        key = load_key()
        cipher = Fernet(key)
        decrypted_code = cipher.decrypt(encrypted_code).decode()
        
        print("✓ Decrypted successfully!")
        print("▶️  Starting Flask server...\n")
        print("="*60)
        
        # Execute the decrypted code
        exec(decrypted_code)
        
    except Exception as e:
        print(f"❌ Error: {e}")
        sys.exit(1)

if __name__ == "__main__":
    run_encrypted()
