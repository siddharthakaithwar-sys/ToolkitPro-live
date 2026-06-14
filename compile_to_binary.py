#!/usr/bin/env python3
"""
Script to convert app.py to compiled binary format
This protects your code from easy reverse engineering
"""

import py_compile
import os
import sys

def compile_to_binary():
    """Compile app.py to .pyc (bytecode) format"""
    try:
        # Compile app.py to bytecode
        py_compile.compile('app.py', cfile='app.pyc', doraise=True)
        print("✓ Successfully compiled app.py to app.pyc (binary format)")
        print(f"✓ Binary file location: {os.path.abspath('app.pyc')}")
        
        # Optional: Create binary executable (requires PyInstaller)
        print("\n--- To create a standalone executable, run: ---")
        print("pip install pyinstaller")
        print("pyinstaller --onefile --hidden-import=flask --hidden-import=flask_cors --hidden-import=openai app.py")
        
    except Exception as e:
        print(f"✗ Error: {e}")
        sys.exit(1)

if __name__ == "__main__":
    compile_to_binary()
