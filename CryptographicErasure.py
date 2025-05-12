import os
import secrets
from base64 import b64decode
from AESCipher import AESCipher

class CryptographicErasure:
    def __init__(self, logger, update_progress):
        self.aes_cipher = AESCipher()
        self.logger = logger
        self.update_progress = update_progress

    def erase_file(self, file_path, isUpdate=True):
        try:
            self.logger.info(f"Starting cryptographic erasure for file: {file_path}")
            with open(file_path, 'rb') as f:
                data = f.read()

            encrypted_data = self.aes_cipher.encrypt(data.decode(errors='ignore'))
            with open(file_path, 'wb') as f:
                f.write(b64decode(encrypted_data['cipher_text']))

            if isUpdate:
                self.update_progress(60)
            os.remove(file_path)
            if isUpdate:
                self.update_progress(100)
            self.logger.info(f"Successfully erased and deleted file: {file_path}")
        except Exception as e:
            self.logger.error(f"Failed to erase file {file_path}: {e}")

    def erase_folder(self, folder_path):
        try:
            self.logger.info(f"Starting cryptographic erasure for folder: {folder_path}")
            self.update_progress(2)
            total = 1
            for root, dirs, files in os.walk(folder_path):
                total+=len(files)+len(dirs)
            completed=0
            for root, dirs, files in os.walk(folder_path, topdown=False):
                for file in files:
                    file_path = os.path.join(root, file)
                    self.erase_file(file_path=file_path,isUpdate=False)
                    completed += 1
                    self.update_progress(int((completed / total) * 100))

                for folder in dirs:
                    subfolder_path = os.path.join(root, folder)
                    os.rmdir(subfolder_path)
                    completed += 1
                    self.update_progress(int((completed / total) * 100))
                    self.logger.info(f"Deleted subfolder: {folder_path}")

            os.rmdir(folder_path)
            self.update_progress(100)
            self.logger.info(f"Deleted root folder: {folder_path}")
        except Exception as e:
            self.logger.error(f"Failed to erase folder {folder_path}: {e}")

    def perform_deletion(self, path):
        if not os.path.exists(path):
            self.logger.error(f"Path does not exist: {path}")
            return

        if os.path.isfile(path):
            self.erase_file(path)
        elif os.path.isdir(path):
            self.erase_folder(path)
        else:
            self.logger.error(f"Unsupported path type: {path}")
