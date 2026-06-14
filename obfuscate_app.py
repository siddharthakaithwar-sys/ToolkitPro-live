#!/usr/bin/env python3
"""
Convert app.py to obfuscated bytecode (Marshal format)
This creates a single executable file that doesn't need key management
Works on any server without additional files
"""

import marshal
import zlib
import base64
import py_compile
import os
import tempfile

def obfuscate_app():
    """Convert app.py to obfuscated marshal bytecode"""
    try:
        # Compile Python to bytecode
        with tempfile.NamedTemporaryFile(suffix='.pyc', delete=False) as tmp:
            py_compile.compile('app.py', cfile=tmp.name, doraise=True)
            
            # Read the bytecode
            with open(tmp.name, 'rb') as f:
                pyc_data = f.read()
            
            # Extract code object (skip header)
            code_obj = marshal.loads(pyc_data[16:])
        
        # Compress with zlib
        compressed = zlib.compress(marshal.dumps(code_obj), 9)
        
        # Encode to base64 for storage
        encoded = base64.b64encode(compressed).decode()
        
        # Create obfuscated app
        obfuscated_code = f'''#!/usr/bin/env python3
"""Obfuscated App - Source code hidden in bytecode"""
import marshal
import zlib
import base64

OBFUSCATED = base64.b64decode("""{encoded}""")
code_obj = marshal.loads(zlib.decompress(OBFUSCATED))
exec(code_obj)
'''
        
        # Write to app.py
        with open('app_obfuscated.py', 'w') as f:
            f.write(obfuscated_code)
        
        # Cleanup
        os.unlink(tmp.name)
        
        print("\\n" + "="*60)
        print("✓ OBFUSCATION COMPLETE!")
        print("="*60)
        print(f"✓ Source code is now hidden in bytecode format")
        print(f"✓ File: app_obfuscated.py ({len(obfuscated_code)} bytes)")
        print(f"\\n✓ Benefits:")
        print(f"  - Works on any server (no key management)")
        print(f"  - Single standalone file")
        print(f"  - Source code unreadable")
        print(f"  - No external dependencies for running")
        print(f"\\n✓ To use:")
        print(f"  1. Replace app.py with app_obfuscated.py")
        print(f"  2. Rename: mv app_obfuscated.py app.py")
        print(f"  3. Run: python app.py")
        print("="*60)
        
    except Exception as e:
        print(f"✗ Error: {e}")

if __name__ == "__main__":
    obfuscate_app()
