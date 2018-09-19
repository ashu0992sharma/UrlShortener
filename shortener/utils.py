import string
import random
import re


def gen_hash(seed):
    """
    :param seed: seed for random generation
    :return: hash key
    """""
    base = string.ascii_letters + string.digits  # Output hash base: all alphabets and digits
    random.seed(seed)  # Input string as the random seed
    hash_value = ""
    for i in range(8):
        # Generate a 8-character hash by randomly select characters from base
        hash_value += random.choice(base)
    return hash_value


def validate_url(url):
    """
    validating a url
    :param url: url to be validated
    :return: true if url is valid else false
    """
    regex = re.compile(
        r'^(?:http|ftp)s?://'  # http:// or https://
        r'(?:(?:[A-Z0-9](?:[A-Z0-9-]{0,61}[A-Z0-9])?\.)+(?:[A-Z]{2,6}\.?|[A-Z0-9-]{2,}\.?)|'  # domain...
        r'localhost|'  # localhost...
        r'\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3})'  # ...or ip
        r'(?::\d+)?'  # optional port
        r'(?:/|[/]\S+)$', re.IGNORECASE)
    return regex.match(url)


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



