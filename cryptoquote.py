from dataclasses import dataclass
import string
import random


class CryptoquoteAlreadyEncrypted(Exception):
    pass


class Quote:
    def __init__(self, value) -> None:
        self.value = value.upper()

    def __str__(self) -> str:
        return self.value

    def __iter__(self) -> iter:
        return iter(self.value)


class Key:
    def __init__(self):
        self.value = random.sample(string.ascii_uppercase, len(string.ascii_uppercase))
        self.mapping = dict(zip(string.ascii_uppercase, self.value))



class Cryptoquote:
    def __init__(self, quote: Quote, key: Key) -> None:
        self.quote = quote
        self.key = key
        self.crypto = ""

    def encrypt(self):
        if self.crypto:
            raise CryptoquoteAlreadyEncrypted

        for char in self.quote:
            if char not in string.ascii_uppercase:
                self.crypto += char
                continue
            self.crypto += self.key.mapping[char]



    
if "__main__" == __name__:
    q = Quote("This is a quote.")
    k = Key()
    print(k.value)
    c = Cryptoquote(q, k)
    print(c.quote)
    c.encrypt()
    print(c.crypto)


