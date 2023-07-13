## Installation

You can install QSafeCrypto using pip:

```
pip install qsafecrypto
```

## Usage

Import the `encrypt` and `decrypt` functions from the QSafeCrypto package:

```python
from qsafecrypto.aes_gcm_256 import encrypt, decrypt
from qsafecrypto import util 
```

### Encryption

Encrypt a payload using AES-GCM-256 encryption:

```python
data = "Hello, world!"

key = "8A6KcShDcvd1jbTBBuTKQupizA7xGivh" # 32-byte-key for example - util.random_key_generate(length=32)

verification_key = "myappnameaskey" # Length & uniqueness doesn't matter.

encrypted_data = encrypt(data, key, verification_key)

print("Encrypted data:", encrypted_data)

# Encrypted data: Vu5YayfedA8NEsaLxMKzn3HNrDWzpkiM3w8VztPLHyqL3ynQSShM3Zje
```

The `encrypt` function takes the payload, encryption key, and verification key as arguments. By default, it returns the encrypted ciphertext as a string. You can set the `decode` parameter to `False` to receive the ciphertext as bytes.

### Decryption

Decrypt a encrypted_data using AES-GCM-256 decryption:

```python
# encrypted_data = "Vu5YayfedA8NEsaLxMKzn3HNrDWzpkiM3w8VztPLHyqL3ynQSShM3Zje"
# key = "8A6KcShDcvd1jbTBBuTKQupizA7xGivh"
# verification_key = "myappnameaskey"

decrypted_data = decrypt(encrypted_data, key, verification_key)

print("Decrypted data:", decrypted_data)

# Decrypted data: "Hello, world!"
```

The `decrypt` function takes the ciphertext, decryption key, and verification key as arguments. By default, it returns the decrypted plaintext as a string. Setting the `decode` parameter to `False` will return the plaintext as bytes.