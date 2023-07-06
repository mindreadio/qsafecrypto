import unittest
from Crypto.Cipher import AES
from qsafecrypto.aes_gcm import encrypt, decrypt


class CryptoTestCase(unittest.TestCase):
    def setUp(self):
        # Generate random values for testing
        self.dek = "32-byte-key"
        self.salt = "api-salt"
        self.associated_data = "associated-data"
        self.payload = "Hello, world!"

    def test_encrypt_decrypt(self):
        encrypted_payload = encrypt(self.payload, self.dek, self.salt, self.associated_data)
        decrypted_payload = decrypt(encrypted_payload, self.dek, self.salt, self.associated_data)
        self.assertEqual(decrypted_payload, self.payload)

    def test_aes_gcm_invalid_decrypt(self):
        encrypted_payload = encrypt(self.payload, self.dek, self.salt, self.associated_data)
        # Modify the DEK to simulate an invalid decryption
        invalid_dek = "invalid-key"
        with self.assertRaises(AES.DecryptionError):
            decrypt(encrypted_payload, invalid_dek, self.salt, self.associated_data)


if __name__ == '__main__':
    unittest.main()
