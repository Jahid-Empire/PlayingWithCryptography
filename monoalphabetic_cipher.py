def caesar_cipher(message, shift, mode='encrypt'):
    alphabet = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    result = ''
    for char in message:
        if char.isalpha():
            if mode == 'encrypt':
                result += alphabet[(alphabet.index(char.upper()) + shift) % 26]
            elif mode == 'decrypt':
                result += alphabet[(alphabet.index(char.upper()) - shift) % 26]
        else:
            result += char
    return result

plaintext = "HELLO"
shift_amount = 3
ciphertext = caesar_cipher(plaintext, shift_amount, mode='encrypt')
print("Encrypted:", ciphertext)

decrypted_text = caesar_cipher(ciphertext, shift_amount, mode='decrypt')
print("Decrypted:", decrypted_text)
