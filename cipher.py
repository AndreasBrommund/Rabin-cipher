from enum import Enum

class SimpleCipher:
    def encrypt(self,key: int, message: str) -> int:

        return 0

    def decrypt(self,key: int, cryptogram: int) -> str:
        return ""

class CipheringMode(Enum):
    OFB = "Output Feedback"
    ECB = "Electronic Codebook"
