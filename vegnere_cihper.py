def encrypt_vigenere(plaintext, key):
    encrypted_text = ""
    key_length = len(key)

    for i in range(len(plaintext)):
        key_char = key[i % key_length]
        encrypted_char = chr((ord(plaintext[i]) + ord(key_char)) % 26 + ord('A'))
        encrypted_text += encrypted_char

    return encrypted_text

def decrypt_vigenere(encrypted_text, key):
    decrypted_text = ""
    key_length = len(key)

    for i in range(len(encrypted_text)):
        key_char = key[i % key_length]
        decrypted_char = chr((ord(encrypted_text[i]) - ord(key_char) + 26) % 26 + ord('A'))
        decrypted_text += decrypted_char

    return decrypted_text

def main():
    plaintext = "HELLOWORLD"
    key = "KEY"

    encrypted_text = encrypt_vigenere(plaintext, key)
    decrypted_text = decrypt_vigenere(encrypted_text, key)

    print("Plaintext:", plaintext)
    print("Encrypted Text:", encrypted_text)
    print("Decrypted Text:", decrypted_text)

if __name__ == "__main__":
    main()
