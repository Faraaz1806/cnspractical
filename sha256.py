import hashlib
message = input("Enter the message you want to encrypt: ")
key = input("Enter a key (it can be any text, e.g., password, PIN, or secret phrase): ")
combined = message + key
hashed = hashlib.sha256(combined.encode()).hexdigest()
print("\n Encrypted (SHA-256 Hash):")
print(hashed)