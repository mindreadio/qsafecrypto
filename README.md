# QSafeCrypto

QSafeCrypto is a Python package that provides encryption and decryption functions using AES-GCM-256, a quantum-safe encryption algorithm.

### Why QSafeCrypto?

Cryptography is easy to implement but challenging to implement properly. There are only a few correct ways to do it, but many ways to make mistakes. Additionally, the threat of quantum computers is becoming increasingly evident. Quantum computers have the potential to decipher most existing encryptions through sheer computing power. In this new brave world, we must be prepared. It's time to adopt quantum-safe encryption everywhere, from databases to user confidential information. Everything needs to be encrypted.

Brilliant minds in the world have developed algorithms that are deemed safe against quantum computers for the foreseeable future. AES-GCM-256 is one such algorithm.

This is why QSafeCrypto embarks on its journey. Although we started with only one algorithm, our goal is to expand our algorithm list.

### Why I built QSafeCrypto or reinvented the wheel?

A few years ago, when I started coding for my startup, Mindread.io, I quickly realized the necessity of using an encryption algorithm to secure customer data. However, I found it very challenging to use existing solutions. Extensive theoretical knowledge was required, and another popular solution, Pycryptodome, also had its complications.

During my research, I discovered the Google TINK cryptography library, which was incredibly helpful. However, it still involved substantial theoretical understanding and installation hurdles. Additionally, there was a potential vendor lock-in risk. Most of the time, developers had to be knowledgeable about what they were doing.

Finally, I made the difficult decision to build QSafeCrypto from scratch. Since then, the library has been used in production and has successfully encrypted millions of bytes of data with lower latency and improved ease of use. Now, as a time-tested program, I wanted to make it open source.

### What is the idea and requirement?

The idea is quite simple, but I have four specific requirements:

1. The library must include two functions: one for encryption and another for decryption.
2. A key will be necessary, stored either in the environment variable or in the Key Management System (KMS), which will be used for encryption and decryption.
3. The library must be performant and quantum-safe.
4. It should be designed in a way that even developers cannot easily make errors. Additionally, it should have an aesthetically pleasing appearance.

### How I distilled all the complexities, theories, and parameters into two simple functions?

I drew inspiration from Google Tink and followed best practices while adhering to my four golden requirements. I did not deviate from them.

For example, in AES-GCM-256, each operation requires a unique "nonce" key that must be remembered and provided for decryption. To simplify this process, I merged it with the encrypted key and later extracted the relevant portion when needed.

Secondly, there must be associated data or tags for verification. By merging this data, we can easily verify if the data is from the original source or not.

Lastly, base64 encoded data can be visually unappealing, often including trailing equal signs. To address this, I made the key base58 encoded, resembling a Bitcoin wallet address. This visual enhancement is pleasing to the eye.

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