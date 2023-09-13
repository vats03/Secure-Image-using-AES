from Crypto.Cipher import AES

BLOCK_SIZE = 16

with open('output_image.enc', 'rb') as infile:
    iv = infile.read(BLOCK_SIZE)
    ciphertext = infile.read()
key = b'\x81\x07P\xe8\x11\x93\xee\xbf\xea,\x08]\xad\xc7A\x7f' 
cipher = AES.new(key, AES.MODE_CBC, iv)

plaintext = cipher.decrypt(ciphertext)

padding_size = plaintext[-1]
plaintext = plaintext[: -padding_size]


# the path of the encrytpete mesage
with open('decrypted_image.jpg', 'wb') as outfile:
    outfile.write(plaintext)
