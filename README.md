XOR Encryption and Verification
This project demonstrates how to encrypt two text files (Beyond.txt and Ethics.txt) using the same keystream, XOR the ciphertexts, and verify that the XOR of the ciphertexts is equivalent to the XOR of the original plaintext files. The process consists of two separate programs:

Program 1: XOR the original plaintext books and save the result.
Program 2: Encrypt both books using the same keystream, XOR the ciphertexts, and verify that the XOR of the ciphertexts matches the XOR of the plaintexts.
Requirements
Python 3.x
Files
xor_plaintext.py: XORs the plaintext contents of Beyond.txt and Ethics.txt and saves the result in xor_plaintext.txt.
xor_ciphertext.py: Encrypts the files using the same keystream, XORs the resulting ciphertexts, and verifies the result against the XOR of the plaintexts.
Beyond.txt: The first text file to encrypt and XOR.
Ethics.txt: The second text file to encrypt and XOR.
Instructions
Step 1: XOR the Plaintext Files
Place the two text files Beyond.txt and Ethics.txt in the same directory as the scripts.

Run xor_plaintext.py to XOR the contents of the plaintext files:

bash
Copy code
python3 xor_plaintext.py
This will create a file named xor_plaintext.txt which contains the XOR of the two plaintext files.

Step 2: Encrypt the Files, XOR the Ciphertexts, and Verify
After XORing the plaintexts, run xor_ciphertext.py to encrypt the files, XOR the ciphertexts, and verify that the XOR result matches the XOR of the original plaintexts:

bash
Copy code
python3 xor_ciphertext.py
This script will:

Encrypt both Beyond.txt and Ethics.txt using the same keystream.
XOR the resulting ciphertexts and save the result to xor_ciphertext.txt.
Compare the XOR of the ciphertexts with xor_plaintext.txt.
Print a confirmation message if the two XOR results match.
Outputs
xor_plaintext.txt: Contains the XOR of the plaintext files (Beyond.txt and Ethics.txt).
xor_ciphertext.txt: Contains the XOR of the ciphertexts after both files are encrypted using the same keystream.
Verification
The XOR of the plaintexts and the XOR of the ciphertexts should be identical. This demonstrates that when using the same keystream to encrypt both files, XORing the ciphertexts is equivalent to XORing the original plaintexts.

