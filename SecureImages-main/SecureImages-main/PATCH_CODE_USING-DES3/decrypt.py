import hashlib
from Crypto.Cipher import DES3

# decryption key and initialization vector
key = hashlib.sha256(b"mysecretkey").digest()[:24]
iv = b"12345678"


with open("../Images/encrypted_image.jpg", "rb") as input_file:
    input_data = input_file.read()


cipher = DES3.new(key, DES3.MODE_CBC, iv)


padded_input_data = input_data + b"\0" * (8 - len(input_data) % 8)
decrypted_data = cipher.decrypt(padded_input_data)


with open("../Images/decrypted_image.jpg", "wb") as output_file:
    output_file.write(decrypted_data)
