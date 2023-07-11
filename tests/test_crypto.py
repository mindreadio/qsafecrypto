import unittest
import base64
from qsafecrypto.aes_gcm_256 import encrypt, decrypt 
from qsafecrypto import util 

# Running tests: python -m unittest discover tests

class CryptoTestCase(unittest.TestCase):
    def setUp(self):
        # Generate random values for testing
        self.payload = "Hello, world!"
        self.key = util.random_key_generate(length=32) # 32-byte-key like - BSKAkccJe1nFCLdKEt3SupKonqZVWrCt
        self.verification_key = "myappnameaskey" # util.random_key_generate(length=16)
        self.decode = True
        self.length = 32

    def test_encrypt_decrypt(self):
        encrypted_payload = encrypt(self.payload, self.key, self.verification_key, self.decode)
        print("encrypted_payload", encrypted_payload)
        decrypted_payload = decrypt(encrypted_payload, self.key, self.verification_key, self.decode)
        print("decrypted_payload", decrypted_payload)
        self.assertEqual(decrypted_payload, self.payload)

    def test_aes_gcm_invalid_decrypt(self):
        encrypted_payload = encrypt(self.payload, self.key, self.verification_key, self.decode)
        # Modify the DEK to simulate an invalid decryption
        invalid_key = "XySwog4xDGfhAw2rZH2IEZMKIWpKTZcM"
        
        with self.assertRaises(ValueError):
            decrypt(encrypted_payload, invalid_key, self.verification_key, self.decode)
            
    def test_util_random_key_generate(self):
        generated_random_encryption_key = util.random_key_generate(self.length)
        print("A random key", generated_random_encryption_key)
        self.assertEqual(len(generated_random_encryption_key), self.length)
        
    def test_util_encode_file(self):
        filepath = './tests/test_crypto.py'
        encoded_file = util.encode_file(filepath)
        
        with open(filepath, "rb") as f:
            raw_encoded_file = base64.b64encode(f.read())
            
        self.assertEqual(encoded_file, raw_encoded_file)
        
    def test_util_decode_file(self):
        filepath = './tests/test_crypto.py'
        encoded_file = util.encode_file(filepath)
        decoded_file = util.decode_file(encoded_file)
        
        with open(filepath, "rb") as f:
            raw_encoded_file = f.read()
            
        self.assertEqual(decoded_file, raw_encoded_file)


if __name__ == '__main__':
    unittest.main()
