class CryptoquoteAlreadyEncryptedError(Exception):
    """Exception for Cryptoquote that has already been encrypted."""
    pass


class ImproperKeyError(Exception):
    """Key must be 26 unique uppercase alphabetical letters."""
    pass