from Crypto.Cipher import AES
from Crypto.Random import get_random_bytes
import based58

# KEY = 32 BYTES (27 BYTES: Original DEK, 5 Bytes: API Sequence Based )
# NONCE = 12 BYTES
# TAG = 16 BYTES

# DEK - Maybe COMES FROM THE KEY RING
# SALT - Another key
# ASSOCIATED DATA - It could be anything


def encrypt(payload, dek, salt, associated_data):
    """
    This will encrypt the JSON Object
      Args:
        payload (string): The JSON
        dek (string): The DEK
        associated_data (string): Like Salt
        salt (string): Comes from the api
    Returns:
        string: Base58 encoded ciphertext.
    """
    associated_data = associated_data.encode()
    data = payload.encode()
    key = f'{dek}{salt}'.encode()
    # key = dek.encode() + salt.encode()
    nonce = get_random_bytes(12)
    # print(
    #     "📣", f"DEK = {dek}, SALT = {salt}, key = {key}, associated_data = {associated_data}, nonce = {nonce}")
    cipher = AES.new(key, AES.MODE_GCM, nonce=nonce)
    cipher.update(associated_data)
    ciphertext, tag = cipher.encrypt_and_digest(data)

    raw = nonce+ciphertext+tag
    result = based58.b58encode(raw)

    return result


def decrypt(payload, dek, salt, associated_data):
    """
    This will encrypt the JSON Object
      Args:
        payload (string): The JSON
        dek (string): The DEK
        associated_data (string): Like Salt
        salt (string): Comes from the api
    Returns:
        string: Decrypted ciphertext.
    """
    associated_data = associated_data.encode()
    key = f'{dek}{salt}'.encode()

    byte_convert = based58.b58decode(payload)
    
    r_nonce = byte_convert[0:12]  # First 4 Digit
    r_ciphertext = byte_convert[12:-16]  # Real Cipher Text
    r_tag = byte_convert[-16:]  # Real Tag

    cipher = AES.new(key, AES.MODE_GCM, nonce=r_nonce)
    cipher.update(associated_data)
    plaintext = cipher.decrypt_and_verify(r_ciphertext, r_tag)
    return plaintext

