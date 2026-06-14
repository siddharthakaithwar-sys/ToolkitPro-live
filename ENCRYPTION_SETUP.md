# 🔐 App.py Encryption Setup Guide

## Overview
Your `app.py` is now encrypted using **Fernet (AES-128) encryption**. This protects your source code and API keys.

---

## Step 1: Install Dependencies

```bash
pip install -r requirements.txt
```

This installs the `cryptography` library needed for encryption.

---

## Step 2: Encrypt Your App

```bash
python encrypt_app.py
```

**Output:**
```
🔑 Generating new encryption key...
✓ Encryption key saved to: secret.key
⚠️  KEEP THIS FILE SAFE! Anyone with this key can decrypt your code.

============================================================
✓ ENCRYPTION SUCCESSFUL!
============================================================
✓ Original file: app.py
✓ Encrypted binary: app_encrypted.bin
✓ Encryption key: secret.key

File sizes:
  - Original: 1316 bytes
  - Encrypted: 1408 bytes

📝 To run encrypted app: python run_encrypted_app.py
============================================================
```

**Files Created:**
- `app_encrypted.bin` - Your encrypted code (binary format)
- `secret.key` - Encryption key (KEEP SAFE!)

---

## Step 3: Run Encrypted App

```bash
python run_encrypted_app.py
```

**Output:**
```
🔓 Decrypting app...
✓ Decrypted successfully!
▶️  Starting Flask server...

 * Running on http://0.0.0.0:5000
```

---

## Files Explained

| File | Purpose |
|------|----------|
| `encrypt_app.py` | Encrypts `app.py` → `app_encrypted.bin` |
| `run_encrypted_app.py` | Decrypts and runs the encrypted app |
| `app_encrypted.bin` | Your encrypted code (binary) |
| `secret.key` | Encryption key (DO NOT SHARE!) |
| `app.py` | Original source (keep for backups) |

---

## Security Tips ⚠️

### 1. **Protect Your Encryption Key**
```bash
# Add to .gitignore (don't commit secret.key)
echo "secret.key" >> .gitignore
echo "app_encrypted.bin" >> .gitignore
```

### 2. **Move API Key to Environment Variable**

**Before (UNSAFE):**
```python
api_key = "nvapi-nhApfX2jtIEVrGgWe5Cc"
```

**After (SAFE):**
```python
import os
api_key = os.getenv("NVIDIA_API_KEY")
```

Run with:
```bash
export NVIDIA_API_KEY="your-key-here"
python run_encrypted_app.py
```

### 3. **Backup Your Key**
```bash
# Store secret.key in a safe place
cp secret.key ~/backups/secret.key.backup
```

---

## Deployment

### Option A: Deploy with Encrypted App (Recommended)
```bash
# Deploy these files:
# - run_encrypted_app.py
# - app_encrypted.bin
# - secret.key (in secure location/env var)
# - requirements.txt

# On server:
pip install -r requirements.txt
export NVIDIA_API_KEY="your-key"
python run_encrypted_app.py
```

### Option B: PyInstaller Standalone
```bash
pip install pyinstaller
pyinstaller --onefile --hidden-import=cryptography run_encrypted_app.py
# Creates: dist/run_encrypted_app (standalone executable)
```

---

## FAQ

**Q: Can someone still see my API key?**
A: Only if they have your `secret.key`. Encrypt it separately or use environment variables.

**Q: What if I lose secret.key?**
A: You won't be able to decrypt `app_encrypted.bin`. Keep backups!

**Q: Is Fernet encryption secure?**
A: Yes! It uses AES-128 in CBC mode with HMAC authentication.

**Q: Can I decrypt without the key?**
A: No. The encryption is mathematically secure. You must have the key.

---

## Quick Reference

```bash
# First time setup
pip install -r requirements.txt
python encrypt_app.py

# Run encrypted app
python run_encrypted_app.py

# Protect your key
echo "secret.key" >> .gitignore
```

✅ **Your app is now encrypted and ready to use!**
