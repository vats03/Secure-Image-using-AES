from Crypto.Cipher import AES
import os

BLOCK_SIZE = 16
key = os.urandom(BLOCK_SIZE)
iv = os.urandom(BLOCK_SIZE)


cipher = AES.new(key, AES.MODE_CBC, iv)
with open('./Images/leonLogo.png', 'rb') as infile:
    plaintext = infile.read()

padding_size = BLOCK_SIZE - len(plaintext) % BLOCK_SIZE
plaintext += bytes([padding_size]) * padding_size
ciphertext = cipher.encrypt(plaintext)
with open('output_image.enc', 'wb') as outfile:
    outfile.write(iv + ciphertext)


# print the ley or store it in the database so as to use thhe same key to decrypt the Images

print(key)
