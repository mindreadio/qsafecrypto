from Crypto.Cipher import AES
from Crypto.Random import get_random_bytes
import based58

# KEY = 32 BYTES ()
# NONCE = 12 BYTES
# TAG = 16 BYTES

# DEK - Maybe COMES FROM THE KEY RING
# SALT - Another key
# ASSOCIATED DATA - It could be anything


def encrypt(payload, key, tag):
    """
    This will encrypt the JSON Object
      Args:
        payload (string): String which needs to be encrypted
        key (string): The encryption key
        tag (string): Like Salt
    Returns:
        string: Base58 encoded ciphertext.
    """
    tag = tag.encode()
    data = payload.encode()
    key = key.encode()
    # key = dek.encode() + salt.encode()
    nonce = get_random_bytes(12)
    # print(
    #     "📣", f"DEK = {dek}, SALT = {salt}, key = {key}, tag = {tag}, nonce = {nonce}")
    cipher = AES.new(key, AES.MODE_GCM, nonce=nonce)
    cipher.update(tag)
    ciphertext, tag = cipher.encrypt_and_digest(data)

    raw = nonce+ciphertext+tag
    result = based58.b58encode(raw)

    return result


def decrypt(payload, key, tag):
    """
    This will encrypt the JSON Object
      Args:
        payload (string): Encrypted string
        key (string): The encryption key
        tag (string): Like Salt
    Returns:
        string: Decrypted ciphertext.
    """
    tag = tag.encode()
    key = key.encode()

    byte_convert = based58.b58decode(payload)
    
    r_nonce = byte_convert[0:12]  # First 4 Digit
    r_ciphertext = byte_convert[12:-16]  # Real Cipher Text
    r_tag = byte_convert[-16:]  # Real Tag

    cipher = AES.new(key, AES.MODE_GCM, nonce=r_nonce)
    cipher.update(tag)
    plaintext = cipher.decrypt_and_verify(r_ciphertext, r_tag)
    return plaintext

