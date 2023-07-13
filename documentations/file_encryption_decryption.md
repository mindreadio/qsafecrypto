# You can decrypt any file or image with quantam safe guarantee

This example shows how to encrypt and decrypt a file or image using the QSafeCrypto library.

## Importing the libraries

```python
import base64
from qsafecrypto.aes_gcm_256 import encrypt, decrypt # Imported AES_GCM_256 algorithoms for encrypting and decrypting
from qsafecrypto.util import random_key_generate, encode_file, decode_file

# Example usage
input_path = "logo.png"
output_path = "logo_converted.jpg"

# Convert image to base64
encoded_image = encode_file(input_path)

# Declare the key
key = "8A6KcShDcvd1jbTBBuTKQupizA7xGivh" # 32-byte-key for example - random_key_generate(length=32)
verification_key = "myappnameaskey"

# Now encrypt the base64 version of the image. 
# You can convert any file like this. Just convert it to base64 version.
encrypted_image = encrypt(encoded_image, key, verification_key, decode=False)

print("Encrypted Image: \n", encrypted_image)

# Now decrypt and get the bas64 encoded version
# Decode false meaning he result will be in bytes
decrypted_image = decrypt(encrypted_image, key, verification_key,  decode=False)

# Decode base64 to image and save it in the output path. Voile same image is restored!
# If you don't want to sae it in your filesystem after decoding just don't give output_path
decode_file(decrypted_image, output_path)
```

## Conclusion

This example shows how to encrypt and decrypt files or images using the QSafeCrypto library. The QSafeCrypto library provides a secure and quantum-safe way to encrypt data.
