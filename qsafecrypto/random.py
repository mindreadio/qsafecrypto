from Crypto.Random import get_random_bytes
import based58

def key_generate(length=32):
    """
    Generate a random encryption key.

    Args:
        length (int): Length of the random key desired.

    Returns:
        str: A random encryption key.

    Note:
        Generates a secure random key.
    """
    random_bytes = get_random_bytes(length)
    random_key = based58.b58encode(random_bytes).decode()[:length]
    return random_key