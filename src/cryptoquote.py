from dataclasses import dataclass
import string
import random
from typing import NoReturn


class CryptoquoteAlreadyEncrypted(Exception):
    """Exception for Cryptoquote that has already been encrypted."""
    pass


class Quote:
    def __init__(self, value) -> None:
        self.value = value.upper()

    def __str__(self) -> str:
        return self.value

    def __iter__(self) -> iter:
        return iter(self.value)

    def __repr__(self) -> str:
        return (
            f"{self.__class__.__name__}("
            f"{self.value!r}"
        )


class Key:
    def __init__(self, value: str = None):
        if self.value is None:
            self.value = random.sample(string.ascii_uppercase, len(string.ascii_uppercase))
        self.mapping = dict(zip(string.ascii_uppercase, self.value))

    def __str__(self) -> str:
        return self.value

    def __repr__(self) -> str:
        return (
            f"{self.__class__.__name__}("
            f"{self.value!r}, {self.mapping!r}"
        )

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
            raise CryptoquoteAlreadyEncrypted

        for char in self.quote:
            if char not in string.ascii_uppercase:
                self.crypto += char
                continue
            self.crypto += self.key.mapping[char]