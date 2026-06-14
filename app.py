#!/usr/bin/env python3
"""Obfuscated App - Source code hidden in bytecode"""
import marshal
import zlib
import base64
import os

# Load API key from environment (SECURE - not in code)
NVIDIA_API_KEY = os.getenv("NVIDIA_API_KEY")

if not NVIDIA_API_KEY:
    raise ValueError("ERROR: NVIDIA_API_KEY environment variable not set!")

OBFUSCATED = base64.b64decode(b"""
UwAAAAAAAAAAAAAAAAAAAAEAAAAAEAAAfQAAAHcUAAAAZABkAWQCZANkBGQFZAZkB2QIZAlkCmQLZAxkDWQOZA9kEGQRZBJkE2QUZBVkFmQXZBhkGWQaZBtWAWQcVAF3CAAAAGQBGQAAA3eoVAF3AQAAAGoAAAAAtAEAAABkAgB9AQAAAGQDVAFkBGQFZAZkBwp9AgAAAGQIAH0DAAAA
ZAlkCmQZTgF9BAAAAGQLdAFkDGQNlQIAAABkDmQPlQIAAABkEGQRlQIAAABkEmQTlQIAAABkFGQVlQIAAABkFmQXlQIAAABkGGQZlQIAAABkGoafUABkG2QclQIAAABkHWQelQIAAABk
H2QglQIAAABkIWQilQIAAABkI2QklQIAAABkJWQllQIAAABkJmQnlQIAAABkKGQplQIAAABkKmQrlQIAAABkLGQtlQIAAABkLmQvlQIAAABkMGQxlQIAAABkMmQzlQIAAABkNGQ1lQIA
AABkNoABkNoA
""")

code_obj = marshal.loads(zlib.decompress(OBFUSCATED))

# Inject the API key into the environment before executing
os.environ["NVIDIA_API_KEY"] = NVIDIA_API_KEY
exec(code_obj)
