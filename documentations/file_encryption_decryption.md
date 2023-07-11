# You can decrypt any file with quantam safe guarantee

This example shows how to encrypt and decrypt a file using the QSafeCrypto library.

## Importing the libraries

```python
import base64
from qsafecrypto.aes_gcm_256 import encrypt, decrypt # Imported AES_GCM_256 algorithoms for encrypting and decrypting
from qsafecrypto.random import key_generate # Imported support for generating random key

# Encode an image to base64
def image_to_base64(image_path):
    with open(image_path, "rb") as image_file:
        encoded_string = base64.b64encode(image_file.read()).decode('utf-8')
    return encoded_string

# Decode base64 to an image
def base64_to_image(encoded_string, output_path):
    decoded_image = base64.b64decode(encoded_string)
    with open(output_path, "wb") as image_file:
        image_file.write(decoded_image)

# Example usage
image_path = "logo.png"
output_path = "logo_converted.jpg"

# Convert image to base64
encoded_image = image_to_base64(image_path)

# Declare the key
key = "8A6KcShDcvd1jbTBBuTKQupizA7xGivh" # 32-byte-key for example - key_generate(length=32)

verification_key = "myappnameaskey"

# Now encrypt the base64 version of the image. 
# You can convert any file like this. Just convert it to base64 version.
encrypted_image = encrypt(encoded_image, key, verification_key, decode=False)

print("Encrypted Image: \n", encrypted_image)

# Now decrypt and get the bas64 encoded version
decrypted_image = decrypt(encrypted_image, key, verification_key,  decode=False)

# Decode base64 to image and lave it in the output path. Voile same image is restored!
base64_to_image(decrypted_image, output_path)
```

## Conclusion

This example shows how to encrypt and decrypt files or images using the QSafeCrypto library. The QSafeCrypto library provides a secure and quantum-safe way to encrypt data.
