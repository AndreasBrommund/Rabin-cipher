from enum import Enum
from typing import Callable, Any
import util


class BlockCipher:
    def __init__(self, block_size: int, mode: Enum, encrypt: Callable[[Any, int, int], int],
                 decrypt: Callable[[Any, int], int]):

        self.block_size = block_size
        self.mode = mode
        self.encryption_function = encrypt
        self.decryption_function = decrypt

    def encrypt(self, message: str, public_key: int, iv: int = 0) -> [int]:

        message_int = util.string_to_int(message)
        int_blocks = util.int_to_int_blocks(message_int, self.block_size)

        if self.mode == CipheringMode.ECB:
            return CipheringMode.encrypt_ecb(int_blocks, public_key, self)
        elif self.mode == CipheringMode.CBC:
            return CipheringMode.encrypt_cbc(int_blocks, public_key, iv, self)

    def decrypt(self, cryptogram: [int], iv: int = 0) -> str:

        ans = []

        if self.mode == CipheringMode.ECB:
            ans = CipheringMode.decrypt_ecb(cryptogram, self)
        elif self.mode == CipheringMode.CBC:
            ans = CipheringMode.decrypt_cbc(cryptogram, iv, self)

        message_int = util.int_block_to_int(ans, self.block_size)
        message = util.int_to_string(message_int)

        return message


class CipheringMode(Enum):
    ECB = "Electronic Codebook"
    CBC = "Cipher Block Chaining"

    @staticmethod
    def encrypt_ecb(message_blocks: [int], public_key: int, block_cipher: BlockCipher) -> [int]:

        ans = [0] * len(message_blocks)

        for i, b in enumerate(message_blocks):
            ans[i] = block_cipher.encryption_function(b, public_key)
        return ans

    @staticmethod
    def decrypt_ecb(cipher_blocks: [int], block_cipher: BlockCipher) -> [int]:
        ans = [0] * len(cipher_blocks)

        for i, b in enumerate(cipher_blocks):
            ans[i] = block_cipher.decryption_function(b)

        return ans

    @staticmethod
    def encrypt_cbc(int_blocks: [int], public_key: int, iv: int, block_cipher: BlockCipher) -> [int]:

        ans = [0] * len(int_blocks)

        for i, b in enumerate(int_blocks):
            b = b ^ (iv & (2 ** block_cipher.block_size - 1))
            ans[i] = block_cipher.encryption_function(b, public_key)
            iv = ans[i]

        return ans

    @staticmethod
    def decrypt_cbc(cipher_blocks: [int], iv: int, block_cipher: BlockCipher) -> [int]:
        ans = [0] * len(cipher_blocks)

        for i, b in enumerate(cipher_blocks):
            ans[i] = block_cipher.decryption_function(b) ^ (iv & (2 ** block_cipher.block_size - 1))
            iv = b

        return ans
