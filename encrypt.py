from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC
import os

# Function to encrypt the file using ChaCha20
def encrypt_file(input_file, output_file, key, nonce):
    # Read the content of the input file
    with open(input_file, 'rb') as f:
        plaintext = f.read()

    # Create a ChaCha20 cipher
    algorithm = algorithms.ChaCha20(key, nonce)
    cipher = Cipher(algorithm, mode=None, backend=default_backend())
    encryptor = cipher.encryptor()

    # Encrypt the content
    ciphertext = encryptor.update(plaintext)

    # Write the ciphertext to the output file
    with open(output_file, 'wb') as f:
        f.write(ciphertext)

# Function to derive a key from a password
def derive_key_from_password(password, salt):
    # PBKDF2 key derivation function
    kdf = PBKDF2HMAC(
        algorithm=hashes.SHA256(),
        length=32,  # ChaCha20 requires a 256-bit key
        salt=salt,
        iterations=100000,
        backend=default_backend()
    )
    key = kdf.derive(password.encode())
    return key

# Example usage
def main():
    files_to_encrypt = [
        ('Beyond.txt', 'encrypted_Beyond.txt'),
        ('Ethics.txt', 'encrypted_Ethics.txt')
    ]

    # Use a strong password and salt to derive the key
    password = 'strongpassword'
    salt = os.urandom(16)  # Generate a random salt
    key = derive_key_from_password(password, salt)

    # Nonce for ChaCha20 (12 bytes)
    nonce = os.urandom(16)

    # Encrypt each file with the same key and nonce
    for input_file, output_file in files_to_encrypt:
        encrypt_file(input_file, output_file, key, nonce)
        print(f"File '{input_file}' has been encrypted as '{output_file}' with the same keystream.")

if __name__ == "__main__":
    main()
