import unittest
# from Crypto.Cipher import AES
from qsafecrypto.aes_gcm_256 import encrypt, decrypt, generate_random_key

# Running tests python -m unittest discover tests

class CryptoTestCase(unittest.TestCase):
    def setUp(self):
        # Generate random values for testing
        self.payload = "Hello, world!"
        self.key = generate_random_key(length=32) # 32-byte-key like - BSKAkccJe1nFCLdKEt3SupKonqZVWrCt
        self.verification_key = generate_random_key(length=16)
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
            
    def test_aes_gcm_generate_random_key(self):
        generated_random_encryption_key = generate_random_key(self.length)
        print("A random key", generated_random_encryption_key)
        print("Random key length", len(generated_random_encryption_key))
        self.assertEqual(len(generated_random_encryption_key), self.length)


if __name__ == '__main__':
    unittest.main()
