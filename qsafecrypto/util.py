from Crypto.Random import get_random_bytes
import based58
import base64

def random_key_generate(length=32):
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

# Encode a file to base64
def encode_file(filepath):
    """
    Generate a base64 version of a given file

    Args:
        filepath (str): filepath for the given file

    Returns:
        bytes: A random encryption key.

    Note:
        Generates a base64 version of a file.
    """
    with open(filepath, "rb") as f:
        encoded_file = base64.b64encode(f.read())
    return encoded_file

# Decode base64 to an file
def decode_file(encoded_file, output_path=False):
    """
    Generate a decoded version of a given file

    Args:
        encoded_file (bytes): Give the file you encoded with base64 or util.encode_file() function
        output_path (str): If you give a path, it will return the string and rewrite a file in given output path

    Returns:
        bytes: base64 decoded version

    Note:
        Decode a base64 version of a file.
    """
    
    if output_path:
        with open(output_path, "wb") as f:
            f.write(base64.b64decode(encoded_file))
        return base64.b64decode(encoded_file)
    else:
        return base64.b64decode(encoded_file)