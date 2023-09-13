import hashlib
from Crypto.Cipher import DES3

key = hashlib.sha256(b"mysecretkey").digest()[:24]
iv = b"12345678"

with open("../Images/leonLogo.png", "rb") as input_file:
    input_data = input_file.read()

cipher = DES3.new(key, DES3.MODE_CBC, iv)

padded_input_data = input_data + b"\0" * (8 - len(input_data) % 8)
encrypted_data = cipher.encrypt(padded_input_data)

with open("../Images/encrypted_image.jpg", "wb") as output_file:
    output_file.write(encrypted_data)


# notes
# if you want to use a random key  use can use "key = os.urandom(24)" or any other method to generate radowm numbers or characters

# make sure you have stored the key to the data base if it is a random key, so as to use it do decrypt the message
