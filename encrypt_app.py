#!/usr/bin/env python3
"""
Encrypt app.py using Fernet (AES-128) encryption
This creates an encrypted binary version of your code
"""

import os
from cryptography.fernet import Fernet

# Generate encryption key
KEY_FILE = "secret.key"

def generate_key():
    """Generate and save encryption key"""
    key = Fernet.generate_key()
    with open(KEY_FILE, "wb") as key_file:
        key_file.write(key)
    print(f"✓ Encryption key saved to: {KEY_FILE}")
    print(f"⚠️  KEEP THIS FILE SAFE! Anyone with this key can decrypt your code.")
    return key

def encrypt_app():
    """Encrypt the app.py file"""
    try:
        # Read original app.py
        with open("app.py", "r") as f:
            original_code = f.read()
        
        # Generate or load key
        if not os.path.exists(KEY_FILE):
            print("🔑 Generating new encryption key...")
            key = generate_key()
        else:
            with open(KEY_FILE, "rb") as f:
                key = f.read()
            print(f"✓ Using existing key from: {KEY_FILE}")
        
        # Encrypt the code
        cipher = Fernet(key)
        encrypted_code = cipher.encrypt(original_code.encode())
        
        # Save encrypted binary
        with open("app_encrypted.bin", "wb") as f:
            f.write(encrypted_code)
        
        print("\n" + "="*60)
        print("✓ ENCRYPTION SUCCESSFUL!")
        print("="*60)
        print(f"✓ Original file: app.py")
        print(f"✓ Encrypted binary: app_encrypted.bin")
        print(f"✓ Encryption key: {KEY_FILE}")
        print(f"\nFile sizes:")
        print(f"  - Original: {os.path.getsize('app.py')} bytes")
        print(f"  - Encrypted: {os.path.getsize('app_encrypted.bin')} bytes")
        print(f"\n📝 To run encrypted app: python run_encrypted_app.py")
        print("="*60)
        
    except FileNotFoundError:
        print("❌ Error: app.py not found in current directory")
    except Exception as e:
        print(f"❌ Encryption failed: {e}")

if __name__ == "__main__":
    encrypt_app()
