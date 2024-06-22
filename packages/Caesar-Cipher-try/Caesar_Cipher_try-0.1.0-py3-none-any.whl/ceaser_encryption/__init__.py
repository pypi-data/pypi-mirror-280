# cipher_package/__init__.py

# Print a message when the package is imported
print("cipher_package is imported. Use 'from cipher_pack.ceaser import CaesarCipher' to import the CaesarCipher class.")

# Provide a comment with instructions
"""
To use the CaesarCipher class, import it as follows:
from cipher_package.ceaser import CaesarCipher
"""

from .ceaser import CaesarCipher

__all__ = ['CaesarCipher']
