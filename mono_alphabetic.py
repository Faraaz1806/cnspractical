# Basic Monoalphabetic Cipher using a key

def encrypt(text, key):
    alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    text = text.upper()
    result = ""
    for ch in text:
        if ch in alphabet:
            result += key[alphabet.index(ch)]
        else:
            result += ch
    return result

def decrypt(cipher, key):
    alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    result = ""
    for ch in cipher:
        if ch in key:
            result += alphabet[key.index(ch)]
        else:
            result += ch
    return result

# Example key (you can change it)
key = "QWERTYUIOPASDFGHJKLZXCVBNM"  # 26 letters, scrambled

# Example usage
plain = "HELLO WORLD"
cipher = encrypt(plain, key)
decoded = decrypt(cipher, key)

print("Key:       ", key)
print("Plaintext: ", plain)
print("Encrypted: ", cipher)
print("Decrypted: ", decoded)
