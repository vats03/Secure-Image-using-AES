# SecureImages

This is a Python project that demonstrates how to encrypt and decrypt image files using the AES algorithm.

## Installation

<ul>
<li>Clone this repository:
<pre>
<code>
git clone git@github.com:leonTech254/SecureImages.git
</code>
</pre>
</li>
<li>Navigate to the project directory:
<pre>
<code> cd secure-images</code>
</pre>

</li>
<li>Install the required dependencies: 
<pre>
<code>
pip install -r requirements.txt
</code>
</pre>
</li>

</ul>

## Usage

### Encryption

<ol>
<li>
Run main.py
<pre>
<code>
python main.py
</code>
</pre>
<ul>
To change the image to be encrypted update the image path to match your pat <br>
"path/to/your/image"
<pre>
<code>
with open('./Images/leonLogo.png', 'rb') as infile:
</code>
</pre>
</ul>
</li>
<li>The encrypted image file output_image.enc will be generated on the same path, and the key used to encrypt the image will be printed on the termina</li>

</ol>

### Decryption

<ol>
<li>
Open decrypt.py. By default, output_image.enc file will be generated on the same path after running main.py.
</li>
<li>Copy the key from the terminal and update the key variable in decrypt.py
<pre>
<code>
with open('output_image.enc', 'rb') as infile:
    iv = infile.read(BLOCK_SIZE)
    ciphertext = infile.read()
key = b'\x81\x07P\xe8\x11\x93\xee\xbf\xea,\x08]\xad\xc7A\x7f' #you will update the key here
</code>
</pre>
</li>
<li>The Encrypted image will be decrypted and saved as decrypted_image.jpg.
<pre>
<code>python decrypt.py</code>
</pre>

</li>
</ol>

## Developers

<ol>
<li>vatsalworks331@gmail.com</li>
</ol>
