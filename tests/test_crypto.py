import unittest
# from Crypto.Cipher import AES
from qsafecrypto.aes_gcm import encrypt, decrypt

# Running tests python -m unittest discover tests

class CryptoTestCase(unittest.TestCase):
    def setUp(self):
        # Generate random values for testing
        self.payload = "Hello, world!"
        self.key = "SySwog4xDGfhAw2rZH2IEZMKIWpKTZcM" # 32-byte-key
        self.tag = "VvMtdpCusdfsdgsdgsdbsrr"

    def test_encrypt_decrypt(self):
        encrypted_payload = encrypt(self.payload, self.key, self.tag)
        print("encrypted_payload", encrypted_payload)
        decrypted_payload = decrypt(encrypted_payload, self.key, self.tag)
        print("decrypted_payload", decrypted_payload)
        self.assertEqual(decrypted_payload, self.payload.encode())

    def test_aes_gcm_invalid_decrypt(self):
        encrypted_payload = encrypt(self.payload, self.key, self.tag)
        # Modify the DEK to simulate an invalid decryption
        invalid_key = "XySwog4xDGfhAw2rZH2IEZMKIWpKTZcM"
        
        with self.assertRaises(ValueError):
            decrypt(encrypted_payload, invalid_key, self.tag)


if __name__ == '__main__':
    unittest.main()
