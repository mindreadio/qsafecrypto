# QSafeCrypto

QSafeCrypto is a Python package that provides encryption and decryption functions using AES-GCM-256, a quantum-safe encryption algorithm.

## Installation

You can install QSafeCrypto using pip:

```
pip install qsafecrypto
```

## Usage

Import the `encrypt` and `decrypt` functions from the QSafeCrypto package:

```python
from qsafecrypto import aes_gcm_256
```

### Encryption

Encrypt a payload using AES-GCM-256 encryption:

```python
payload = "Hello, world!"

key = "BSKAkccJe1nFCLdKEt3SupKonqZVWrCt" # 32-byte-key for example - aes_gcm_256.generate_random_key(length=32)

verification_key = "myapp" # You can generate one aes_gcm_256.generate_random_key(length=16) Length doesn't matter. Shorter = Faster

encrypted_data = aes_gcm_256.encrypt(payload, key, verification_key)

print("Encrypted payload:", encrypted_data)

# Encrypted ciphertext: nbsjJN2k9o9A1ETFHKvhzk38dnujSF45cq8fn3ozadt9dTWuTfrPaBu8
```

The `encrypt` function takes the payload, encryption key, and verification key as arguments. By default, it returns the encrypted ciphertext as a string. You can set the `decode` parameter to `False` to receive the ciphertext as bytes.

### Decryption

Decrypt a encrypted_payload using AES-GCM-256 decryption:

```python
encrypted_payload = "nbsjJN2k9o9A1ETFHKvhzk38dnujSF45cq8fn3ozadt9dTWuTfrPaBu8"
key = "BSKAkccJe1nFCLdKEt3SupKonqZVWrCt"
verification_key = "myapp"

decrypted_data = decrypt(encrypted_payload, key, verification_key)
print("Decrypted payload:", decrypted_data)

# Decrypted payload: "Hello, world!"
```

The `decrypt` function takes the ciphertext, decryption key, and verification key as arguments. By default, it returns the decrypted plaintext as a string. Setting the `decode` parameter to `False` will return the plaintext as bytes.

## Note

- AES-GCM-256 is used for encryption and decryption, as it is considered quantum-safe.
- Ensure that the same key and verification key used during encryption are provided for successful decryption.
- AES-GCM-192 and AES-GCM-128 are not supported by choice.

---

Feel free to customize the README file to add more details, such as additional examples, usage guidelines, or any other relevant information about your QSafeCrypto package.