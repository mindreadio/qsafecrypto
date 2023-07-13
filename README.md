![Qsafecrypto Logo](https://github.com/mindreadio/qsafecrypto/blob/main/documentations/qsafecrypto_logo.png)


# QSafeCrypto

Utilizing cryptography in your application shouldn't be an intimidating and challenging task. Lets simplify cryptography in your app with QSafeCrypto. It offers easy AES-GCM-256 encryption and decryption, ensuring quantum-safe security.

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
from qsafecrypto.aes_gcm_256 import encrypt, decrypt
from qsafecrypto import util 
```

### Encryption

Encrypt a payload using AES-GCM-256 encryption:

```python
data = "Hello, world!"

key = "8A6KcShDcvd1jbTBBuTKQupizA7xGivh" # A 32-byte-key. To generate one use util.random_key_generate(length=32)

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

## File encyption and decyption

You can import these two utility function to encode and decode files easily.

```python
from qsafecrypto.util import encode_file, decode_file
```

Example and usage : [File Encryption & Decryption](https://github.com/mindreadio/qsafecrypto/blob/main/documentations/file_encryption_decryption.md)

## Note

- AES-GCM-256 is used for encryption and decryption, as it is considered quantum-safe.
- Ensure that the same key and verification key used during encryption are provided for successful decryption.
- AES-GCM-192 and AES-GCM-128 are not supported by choice.


### Why QSafeCrypto?

Cryptography is easy to implement but challenging to implement properly. There are only a few correct ways to do it, but many ways to make mistakes. Additionally, the threat of quantum computers is becoming increasingly evident. Quantum computers have the potential to decipher most existing encryptions through sheer computing power. In this new brave world, we must be prepared. It's time to adopt quantum-safe encryption everywhere, from databases to user confidential information. Everything needs to be encrypted.

Brilliant minds in the world have developed algorithms that are deemed safe against quantum computers for the foreseeable future. AES-GCM-256 is one such algorithm.

This is why QSafeCrypto embarks on its journey. Although we started with only one algorithm, our goal is to expand our algorithm list.

## Why I built and use QSafeCrypto, and why you should use it

I was coding for my startup, Mindread.io. I was storing the data in key-value pairs in memory to get the fastest possible results. I received the data in JSON format and stored it as a single string after stringifying it. As a SaaS, I don't have the luxury of sending user data to other vendor-provided databases that are encrypted at rest. I have to do it myself. I felt the need to encrypt and decrypt user data. So, how could I encrypt and decrypt it? I started by searching Google for best practices.

There is a simple approach: encrypt it with a key, and then decrypt it with the same key. However, I came across a talk by an industry veteran who urged everyone to use quantum-safe encryption to store user data, especially important data. Why? Because in 4-5 years, quantum computers will be able to crack these encryption methods.

I thought, "That's not my problem." There's a term in chess: "Never defend your pieces early against possible attacks." So, it will happen in 4-5 years, and then I'll re-encrypt everything.

Then, he dropped another bombshell. He said that big hackers are collecting encrypted data in the air and hoarding it en masse. They believe that once quantum computers can crack it, they will be able to see the data. Many data sets will not become stale and will remain relevant. For example, a customer's name, gender, age, and email address. These data sets could be leaked and pose a serious threat.

Hmmm... That's pretty concerning. So, what should we do? The protagonist then said, "Just start implementing quantum-safe encryption from now on. It's the safest bet."

So, I started researching how to implement quantum-safe encryption. First, I had to find which encryption algorithms are safe from quantum attack. I found a debatable list. NIST has not yet released an official list, but researchers have found a few that are relatively safe.

However, I found it very challenging to use existing solutions. Extensive theoretical knowledge was required, and another popular solution, Pycryptodome, also had its complications.

During my research, I discovered the Google TINK cryptography library, which was incredibly helpful. However, it still involved substantial theoretical understanding and installation hurdles. Additionally, there was a potential vendor lock-in risk. Most of the time, developers had to be knowledgeable about what they were doing and not "shoot themselves in the foot." Finally, I made the difficult decision to build QSafeCrypto from scratch. After a long research and reading a gazillion amount of internet resources and Stack Overflow questions, I finally implemented it.

`Since then, the library has been used in production and has successfully encrypted millions of megabytes of data with lower latency and improved ease of use. Now, as a time-tested program, I wanted to make it open source.`

As I am working with a team, lecturing CS theories like proper nonce and associated tag bytes to make them understand the thing seems difficult. So, I wrapped everything in a simple package and told them to just use the encrypt() and decrypt() functions.

I had four requirements for developing it. I followed them religiously.

1. The library must include two functions: one for encryption and another for decryption.
2. A key will be necessary, stored either in the environment variable or in the Key Management System (KMS), which will be used for encryption and decryption.
3. The library must be performant and quantum-safe.
4. It should be designed in a way that even developers cannot easily make errors. Additionally, the encrypted keys should have an aesthetically pleasing appearance.

I chose AES-GCM-256 for four reasons as well:

1. It's never been cracked while being quantum-safe!
2. Companies like Signal are using it in their chatting app. Google's Tink library also chooses this algorithm. Big tech are 3. already using it. There is enough social proof.
3. It's fast because there is chip-level support provided by major vendors for this particular algorithm.
4. There is already a supporting Python library with first-class support.

Use it to get quantum-safe encryption and decryption from today, easily.

### How I distilled all the complexities, theories, and parameters into two simple functions?

I took inspiration from Google Tink and followed best practices, sticking to my four core requirements without compromise.

For AES-GCM-256, each operation requires a unique "nonce" key for decryption. To simplify this, I dynamically generate the nonce and merge it with the encrypted key. Developers are relieved from handling the nonce or determining its byte sizes. This approach, inspired by Google TINK, streamlines the process.

To ensure verification and authenticity, associated data or tags are crucial. I merge this data into the key, making it easy to verify the data's origin.

Overall, my implementation simplifies the handling of nonces and associated data, thanks to the ideas and practices employed by Google Tink.

On the other hand to enhance visual appeal, I transformed the key into base58 encoding, resembling a crypto wallet address. This eliminates trailing equal signs commonly found in base64 encoded data. The process relies on a RUST-based library for efficient base58 encoding. Enjoy a visually pleasing key representation without any trailing equal signs.

For example:
Same 
BASE58 = `Vu5YayfedA8NEsaLxMKzn3HNrDWzpkiM3w8VztPLHyqL3ynQSShM3Zje`
BASE64 = `KVx4OTJjXHgwM1xuhjMFx4ZmJceGMwXHhlZUxceGNidVBceDhXHhYQ==`

## Contribution

🧵 This package is developed by [Md Fazlul Karim](https://www.linkedin.com/in/fazlulkarimweb/), co-founder of Mindread.io. Special thanks to him for his valuable contributions to this project.

If you would like to contribute to this project, please feel free to submit a pull request or open an issue. We welcome any suggestions, bug reports, or enhancements.

Please make sure to update tests as appropriate.

## License

[MIT](https://github.com/mindreadio/qsafecrypto/blob/main/LICENSE)

<!-- RUN TESTS -->
<!-- python -m unittest discover tests -->
<!-- Building wheel -->
<!-- python setup.py sdist bdist_wheel -->
<!-- Uploading to Pypi -->
<!-- twine upload dist/* -->