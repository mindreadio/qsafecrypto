# QSafeCrypto

QSafeCrypto is a Python package that provides encryption and decryption functions using AES-GCM-256, a quantum-safe encryption algorithm.

## Documentation

Find more in the - [Documentations](https://github.com/mindreadio/qsafecrypto/blob/main/documentations) 🧮

## Installation

You can install QSafeCrypto using pip:

```
pip install qsafecrypto
```

## Usage

Import the `encrypt` and `decrypt` functions from the QSafeCrypto package:

```python
from qsafecrypto.aes_gcm_256 import encrypt, decrypt # Imported AES_GCM_256 algorithoms for encrypting and decrypting
from qsafecrypto.random import key_generate # Imported support for generating random key
```

### Encryption

Encrypt a payload using AES-GCM-256 encryption:

```python
data = "Hello, world!"

key = "8A6KcShDcvd1jbTBBuTKQupizA7xGivh" # 32-byte-key for example - key_generate(length=32)

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

## Note

- AES-GCM-256 is used for encryption and decryption, as it is considered quantum-safe.
- Ensure that the same key and verification key used during encryption are provided for successful decryption.
- AES-GCM-192 and AES-GCM-128 are not supported by choice.

## Contribution

🧵 This package is developed by [Md Fazlul Karim](https://www.linkedin.com/in/fazlulkarimweb/), co-founder of Mindread.io. Special thanks to him for his valuable contributions to this project.

If you would like to contribute to this project, please feel free to submit a pull request or open an issue. We welcome any suggestions, bug reports, or enhancements.

Please make sure to update tests as appropriate.

## License

[MIT](https://github.com/mindreadio/qsafecrypto/blob/main/LICENSE)