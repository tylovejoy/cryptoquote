import string
import random
from typing import NoReturn


class CryptoquoteAlreadyEncryptedError(Exception):
    """Exception for Cryptoquote that has already been encrypted."""
    pass

class ImproperKeyError(Exception):
    """Key must be 26 unique uppercase alphabetical letters."""
    pass

class Quote:
    def __init__(self, value) -> None:
        self.quote = value.upper()

    def __str__(self) -> str:
        return self.quote

    def __iter__(self) -> iter:
        return iter(self.quote)

    def __repr__(self) -> str:
        return (
            f"{self.__class__.__name__}("
            f"{self.quote!r}"
        )


class Key:
    def __init__(self, value: str = None):
        self.set_key(value)
        self.mapping = dict(zip(string.ascii_uppercase, self.key))

    def __str__(self) -> str:
        return self.key

    def __repr__(self) -> str:
        return (
            f"{self.__class__.__name__}("
            f"{self.key!r}, {self.mapping!r}"
        )
    
    def set_key(self, value: str) -> NoReturn:
        """Set Key to a random value or a given value.

        Args:
            value (str): Value for the Key to be set to.

        Raises:
            ImproperKeyError: Key must be 26 unique letters of the uppercase alphabet.

        Returns:
            str: Return the newly set key.
        """
        if value is None:
            self.key = random.sample(string.ascii_uppercase, len(string.ascii_uppercase))
            return self.key
        
        if len(value) not in [26, len(set(value))] or not all(l.isalpha() for l in value):
            raise ImproperKeyError




class Cryptoquote:
    def __init__(self, quote: Quote, key: Key) -> None:
        self.quote = quote
        self.key = key
        self.crypto = ""
        self._encrypt()

    def __str__(self) -> str:
        return self.crypto

    def __repr__(self) -> str:
        return (
            f"{self.__class__.__name__}("
            f"{self.quote!r}, {self.key!r}, {self.crypto!r}"
        )

    def _encrypt(self) -> NoReturn:
        """Create a 'encrypted' version of the Quote using Key.

        Raises:
            CryptoquoteAlreadyEncrypted: Cryptoquote can only be encrypted once.

        Returns:
            NoReturn
        """
        if self.crypto:
            raise CryptoquoteAlreadyEncryptedError

        for char in self.quote:
            if char not in string.ascii_uppercase:
                self.crypto += char
                continue
            self.crypto += self.key.mapping[char]