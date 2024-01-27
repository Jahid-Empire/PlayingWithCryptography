import random

def generate_key(message_length):
    return [random.randint(0, 255) for _ in range(message_length)]

def encrypt(message, key):
    return bytes([ord(message[i]) ^ key[i] for i in range(len(message))])

def decrypt(encrypted_message, key):
    return ''.join([chr(encrypted_message[i] ^ key[i]) for i in range(len(encrypted_message))])

def main():
    message = "Hello, World!"
    message_bytes = message.encode('utf-8')
    key = generate_key(len(message_bytes))
    encrypted_message = encrypt(message_bytes, key)
    decrypted_message = decrypt(encrypted_message, key)
    print("Encrypted message:", encrypted_message)
    print("Decrypted message:", decrypted_message)

if __name__ == "__main__":
    main()
