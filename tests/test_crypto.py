import unittest
from qsafecrypto import aes_gcm_256, random

# Running tests: python -m unittest discover tests

class CryptoTestCase(unittest.TestCase):
    def setUp(self):
        # Generate random values for testing
        self.payload = "Hello, world!"
        self.key = random.key_generate(length=32) # 32-byte-key like - BSKAkccJe1nFCLdKEt3SupKonqZVWrCt
        self.verification_key = "myappnameaskey" # random.key_generate(length=16)
        self.decode = True
        self.length = 32

    def test_encrypt_decrypt(self):
        encrypted_payload = aes_gcm_256.encrypt(self.payload, self.key, self.verification_key, self.decode)
        print("encrypted_payload", encrypted_payload)
        decrypted_payload = aes_gcm_256.decrypt(encrypted_payload, self.key, self.verification_key, self.decode)
        print("decrypted_payload", decrypted_payload)
        self.assertEqual(decrypted_payload, self.payload)

    def test_aes_gcm_invalid_decrypt(self):
        encrypted_payload = aes_gcm_256.encrypt(self.payload, self.key, self.verification_key, self.decode)
        # Modify the DEK to simulate an invalid decryption
        invalid_key = "XySwog4xDGfhAw2rZH2IEZMKIWpKTZcM"
        
        with self.assertRaises(ValueError):
            aes_gcm_256.decrypt(encrypted_payload, invalid_key, self.verification_key, self.decode)
            
    def test_aes_gcm_random_key_generate(self):
        generated_random_encryption_key = random.key_generate(self.length)
        print("A random key", generated_random_encryption_key)
        print("Random key length", len(generated_random_encryption_key))
        self.assertEqual(len(generated_random_encryption_key), self.length)


if __name__ == '__main__':
    unittest.main()
