from enum import Enum
import util


class SimpleCipher:
    @staticmethod
    def encrypt(key: int, message: str) -> int:
        return key ^ util.string_to_int(message)

    @staticmethod
    def decrypt(key: int, cryptogram: int) -> str:
        return util.int_to_string(key ^ cryptogram)


class CipheringMode(Enum):
    OFB = "Output Feedback"
    ECB = "Electronic Codebook"

    