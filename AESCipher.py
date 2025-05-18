import secrets
from Cryptodome.Cipher import AES
from Cryptodome.Random import get_random_bytes
from base64 import b64encode, b64decode

class AESCipher:
    def __init__(self):
        # Using secrets to generate a strong random encryption key
        self.key = secrets.token_bytes(32)  # 256-bit key for AES-256

    def pad(self, data):
        """
        Pads data to ensure it's a multiple of 16 bytes (AES block size).
        """
        block_size = 16
        return data + (block_size - len(data) % block_size) * b" "

    def unpad(self, data):
        """
        Removes padding from data.
        """
        return data.rstrip(b" ")

    def encrypt(self, data):
        """
        Encrypts data using AES-GCM mode with a random nonce.
        """
        data = self.pad(data.encode())  # Ensure data is padded to be 16-byte aligned
        salt = get_random_bytes(AES.block_size)
        cipher_config = AES.new(self.key, AES.MODE_GCM)
        ciphertext, tag = cipher_config.encrypt_and_digest(data)

        # Return the encrypted data along with associated information for decryption
        return {
            'cipher_text': b64encode(ciphertext).decode('utf-8'),
            'salt': b64encode(salt).decode('utf-8'),
            'nonce': b64encode(cipher_config.nonce).decode('utf-8'),
            'tag': b64encode(tag).decode('utf-8')
        }

    def decrypt(self, encrypted_data):
        """
        Decrypts data using AES-GCM mode.
        """
        salt = b64decode(encrypted_data['salt'])
        ciphertext = b64decode(encrypted_data['cipher_text'])
        nonce = b64decode(encrypted_data['nonce'])
        tag = b64decode(encrypted_data['tag'])

        cipher = AES.new(self.key, AES.MODE_GCM, nonce=nonce)
        decrypted_data = cipher.decrypt_and_verify(ciphertext, tag)

        return self.unpad(decrypted_data).decode('utf-8')
