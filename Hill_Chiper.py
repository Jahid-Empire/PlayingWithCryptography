import numpy as np

def text_to_numbers(text):
    return [ord(char) - 65 for char in text.upper()]

def numbers_to_text(numbers):
    return ''.join([chr(num + 65) for num in numbers])

def generate_key(key, n):
    key_matrix = np.array(text_to_numbers(key))
    key_matrix = key_matrix.reshape(n, n)
    return key_matrix

def mod_inverse(a, m):
    for i in range(1, m):
        if (a * i) % m == 1:
            return i
    return None

def encrypt(plaintext, key):
    n = int(np.sqrt(len(key)))
    plaintext = text_to_numbers(plaintext)
    while len(plaintext) % n != 0:
        plaintext.append(23)
    plaintext = np.array(plaintext)
    plaintext = plaintext.reshape(-1, n)
    ciphertext = ""
    for group in plaintext:
        group = np.dot(group, key) % 26
        ciphertext += numbers_to_text(group)
    return ciphertext

def decrypt(ciphertext, key):
    n = int(np.sqrt(len(key)))
    key = np.linalg.inv(key) * np.linalg.det(key) * mod_inverse(int(np.linalg.det(key)), 26)
    key = key.round() % 26
    ciphertext = text_to_numbers(ciphertext)
    ciphertext = np.array(ciphertext)
    ciphertext = ciphertext.reshape(-1, n)
    plaintext = ""
    for group in ciphertext:
        group = np.dot(group, key) % 26
        plaintext += numbers_to_text(group)
    return plaintext

key = "GYBNQKURP"
plaintext = "HELLO"
key_matrix = generate_key(key, 3)
ciphertext = encrypt(plaintext, key_matrix)
decrypted_text = decrypt(ciphertext, key_matrix)
print(decrypted_text)
