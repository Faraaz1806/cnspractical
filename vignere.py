def generate_key(text, key):
    key = key.upper()
    key = (key * (len(text) // len(key) + 1))[:len(text)]
    return key

def encrypt_vigenere(plaintext, key):
    plaintext = plaintext.upper()
    key = generate_key(plaintext, key)
    ciphertext = ''
    for p, k in zip(plaintext, key):
        if p.isalpha():
            shift = (ord(p) - 65 + ord(k) - 65) % 26
            ciphertext += chr(shift + 65)
        else:
            ciphertext += p
    return ciphertext

def decrypt_vigenere(ciphertext, key):
    ciphertext = ciphertext.upper()
    key = generate_key(ciphertext, key)
    plaintext = ''
    for c, k in zip(ciphertext, key):
        if c.isalpha():
            shift = (ord(c) - 65 - (ord(k) - 65)) % 26
            plaintext += chr(shift + 65)
        else:
            plaintext += c
    return plaintext

# Example usage
message = "HELLO WORLD"
key = "KEY"
encrypted = encrypt_vigenere(message, key)
decrypted = decrypt_vigenere(encrypted, key)

print("Vigenere Cipher")
print("Plaintext:", message)
print("Encrypted:", encrypted)
print("Decrypted:", decrypted)
