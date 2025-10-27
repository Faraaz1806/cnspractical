# Simple RSA Algorithm in Python

# Function to find gcd (Greatest Common Divisor)
def gcd(a, b):
    while b != 0:
        a, b = b, a % b
    return a

# Function to find modular inverse
def mod_inverse(e, phi):
    for d in range(2, phi):
        if (d * e) % phi == 1:
            return d
    return None

# Function to generate public and private keys
def generate_keys(p, q):
    n = p * q
    phi = (p - 1) * (q - 1)

    # Choose e such that 1 < e < phi and gcd(e, phi) = 1
    e = 2
    while e < phi:
        if gcd(e, phi) == 1:
            break
        e += 1

    # Calculate d (private key)
    d = mod_inverse(e, phi)
    return ((e, n), (d, n))  # (public_key, private_key)

# Encrypt function
def encrypt(message, public_key):
    e, n = public_key
    cipher = [(ord(char) ** e) % n for char in message]
    return cipher

# Decrypt function
def decrypt(cipher, private_key):
    d, n = private_key
    plain = [chr((char ** d) % n) for char in cipher]
    return ''.join(plain)

# -------------------------
# Main Program
# -------------------------
print("=== RSA Algorithm ===")
p = int(input("Enter first prime number (p): "))
q = int(input("Enter second prime number (q): "))

public_key, private_key = generate_keys(p, q)
print("\nPublic Key:", public_key)
print("Private Key:", private_key)

message = input("\nEnter message to encrypt: ")

cipher = encrypt(message, public_key)
print("\nEncrypted Message:", cipher)

decrypted = decrypt(cipher, private_key)
print("Decrypted Message:", decrypted)
