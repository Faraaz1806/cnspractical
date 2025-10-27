from string import ascii_uppercase

def makematrix(key):
    key = ''.join(dict.fromkeys(key.upper().replace('J', 'I')))
    matrix = key
    for c in ascii_uppercase:
        if c not in matrix and c != 'J':
            matrix += c
    return matrix

def pos(matrix, ch):
    i = matrix.index(ch)
    return divmod(i, 5)

def prepare_txt(txt):
    txt = txt.upper().replace('J', 'I')
    result = ""
    i = 0
    while i < len(txt):
        a = txt[i]
        b = txt[i+1] if (i+1) < len(txt) else 'X'
        if a == b:
            result += a + 'X'
            i += 1
        else:
            result += a + b
            i += 2
    return result

def playfair_encrypt(txt, key):
    m = makematrix(key)
    txt = prepare_txt(txt)
    res = ''
    for i in range(0, len(txt), 2):
        a, b = txt[i], txt[i+1]
        r1, c1 = pos(m, a)
        r2, c2 = pos(m, b)
        if r1 == r2:
            res += m[r1*5 + (c1+1) % 5] + m[r2*5 + (c2+1) % 5]
        elif c1 == c2:
            res += m[((r1+1) % 5)*5 + c1] + m[((r2+1) % 5)*5 + c2]
        else:
            res += m[r1*5 + c2] + m[r2*5 + c1]
    return res

def playfair_decrypt(txt, key):
    m = makematrix(key)
    res = ''
    for i in range(0, len(txt), 2):
        a, b = txt[i], txt[i+1]
        r1, c1 = pos(m, a)
        r2, c2 = pos(m, b)
        if r1 == r2:
            res += m[r1*5 + (c1-1) % 5] + m[r2*5 + (c2-1) % 5]
        elif c1 == c2:
            res += m[((r1-1) % 5)*5 + c1] + m[((r2-1) % 5)*5 + c2]
        else:
            res += m[r1*5 + c2] + m[r2*5 + c1]
    return res

# Example usage
key = "MONARCHY"
message = "HELLO"
encrypted = playfair_encrypt(message, key)
decrypted = playfair_decrypt(encrypted, key)

print("\nPlayfair Cipher")
print("Plaintext:", message)
print("Encrypted:", encrypted)
print("Decrypted:", decrypted)
