import string
import random
import re


def gen_hash():
    """
    :return: hash key
    """
    base = string.ascii_letters + string.digits  # Output hash base: all alphabets and digits
    # random.seed(seed)  # Input string as the random seed
    hash_value = ""
    for i in range(8):
        # Generate a 8-character hash by randomly select characters from base
        hash_value += random.choice(base)
    return hash_value


def validate_hash(hashed_url):
    """
    validating a hashed url
    :param hashed_url: hashed url to be validated
    :return: true if valid else false
    """
    regex = re.compile(
        r'[\w+]{8}$', re.IGNORECASE
    )
    return regex.match(hashed_url)



