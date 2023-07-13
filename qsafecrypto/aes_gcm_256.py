from Crypto.Cipher import AES
from Crypto.Random import get_random_bytes
import based58

# AES has never been cracked yet and it would take large amounts of computational power to crack this key.

def encrypt(payload, key, verification_key, decode=True):
    """
    Encrypts the given data payload using AES-GCM-256 encryption.

    Args:
        payload (str | bytes): The data to be encrypted, either as a string or bytes.
        key (str): The encryption key must be 32 bytes in length.
        verification_key (str): A verification key or salt. It can be any length, but 16 bytes is preferable.
        decode (bool): If True, the encrypted ciphertext is returned as a string. If False, it is returned as bytes.

    Returns:
        str | bytes: The encrypted ciphertext.

    Raises:
        ValueError: If the key length is not 32 bytes.

    Note:
        AES-GCM-256 is used for encryption as it is considered quantum-safe. 
        AES-GCM-192 and AES-GCM-128 are not supported.
    """
    
    if len(key) != 32:
        raise ValueError("Incorrect AES-GCM-256 key length ({0} bytes). Only 32-byte key length is supported for 256-bit encryption. Qsafecrypto currently supports only AES-GCM-256 as it is deemed to be quantum-safe. AES-GCM-192 & AES-GCM-128 are not supported by choice.".format(len(key)))

    data = payload.encode() if isinstance(payload, str) else payload

    nonce = get_random_bytes(12)
    
    ciphertext, verification_key = AES.new(key.encode(), AES.MODE_GCM, nonce=nonce).update(verification_key.encode()).encrypt_and_digest(data)
    
    if decode:
        return based58.b58encode(nonce+ciphertext+verification_key).decode()
    else:
        return based58.b58encode(nonce+ciphertext+verification_key)


def decrypt(payload, key, verification_key, decode=True):
    """
    Decrypts the given ciphertext using AES-GCM-256 decryption.

    Args:
        payload (str | bytes): The ciphertext to be decrypted, either as a string or bytes.
        key (str): The decryption key. It must be 32 bytes in length.
        verification_key (str): A verification key or salt. It can be any length, but 16 bytes is preferable.
        decode (bool): If True, the decrypted plaintext is returned as a string. If False, it is returned as bytes.

    Returns:
        str | bytes: The decrypted plaintext.

    Raises:
        ValueError: If the key length is not 32 bytes.

    Note:
        AES-GCM-256 is used for decryption. Ensure that the same key and verification key used during encryption are provided for successful decryption.
        AES-GCM-192 and AES-GCM-128 are not supported.
    """

    if len(key) != 32:
        raise ValueError("Incorrect AES-GCM-256 key length ({0} bytes). Only 32-byte key length is supported for 256-bit encryption. Qsafecrypto currently supports only AES-GCM-256 as it is deemed to be quantum-safe. AES-GCM-192 & AES-GCM-128 are not supported by choice.".format(len(key)))

    byte_convert = based58.b58decode(payload.encode() if isinstance(payload, str) else payload)
 
    if decode:
        return AES.new(key.encode(), AES.MODE_GCM, nonce=byte_convert[0:12]).update(verification_key.encode()).decrypt_and_verify(byte_convert[12:-16], byte_convert[-16:]).decode()
    else:
        return AES.new(key.encode(), AES.MODE_GCM, nonce=byte_convert[0:12]).update(verification_key.encode()).decrypt_and_verify(byte_convert[12:-16], byte_convert[-16:])

