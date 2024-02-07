from Crypto.Cipher import Blowfish
from Crypto import Random

def blowfish_encrypt(plaintext, key):
    iv = Random.new().read(Blowfish.block_size)
    cipher = Blowfish.new(key, Blowfish.MODE_CBC, iv)
    return iv + cipher.encrypt(plaintext)

def blowfish_decrypt(ciphertext, key):
    iv = ciphertext[:Blowfish.block_size]
    cipher = Blowfish.new(key, Blowfish.MODE_CBC, iv)
    return cipher.decrypt(ciphertext[Blowfish.block_size:])
