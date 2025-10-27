# Simple DES Encryption & Decryption
# By Mohammad Huzaifa :)

from pyDes import des, CBC, PAD_PKCS5
import binascii

# Function to encrypt text
def encrypt_text(text, key):
    des_cipher = des(key, CBC, key, pad=None, padmode=PAD_PKCS5)
    encrypted_text = des_cipher.encrypt(text)
    return binascii.b2a_hex(encrypted_text).decode()

# Function to decrypt text
def decrypt_text(encrypted_text, key):
    des_cipher = des(key, CBC, key, pad=None, padmode=PAD_PKCS5)
    decrypted_text = des_cipher.decrypt(binascii.a2b_hex(encrypted_text))
    return decrypted_text.decode()

# -------------------------
# Main Program
# -------------------------
text = input("Enter the message: ")
key = input("Enter 8-character key: ")

if len(key) != 8:
    print("Key must be exactly 8 characters long!")
else:
    encrypted = encrypt_text(text, key)
    print("\nEncrypted Text:", encrypted)

    decrypted = decrypt_text(encrypted, key)
    print("Decrypted Text:", decrypted)
