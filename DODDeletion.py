import os

class DODDeletion:
    def __init__(self, logger, update_progress):
        self.logger = logger
        self.update_progress = update_progress

    def dod_3_pass(self, file_path, isUpdate=True):
        try:
            file_size = os.path.getsize(file_path)
            with open(file_path, "wb") as file:
                file.seek(0)
                file.write(b"\x00" * file_size)
                if isUpdate:
                    self.update_progress(33)
                self.logger.info(f"Pass 1/3: Overwritten with binary zeroes for {file_path}")

                file.seek(0)
                file.write(b"\xFF" * file_size)
                if isUpdate:
                    self.update_progress(66)
                self.logger.info(f"Pass 2/3: Overwritten with binary ones for {file_path}")

                file.seek(0)
                file.write(os.urandom(file_size))
                if isUpdate:
                    self.update_progress(100)
                self.logger.info(f"Pass 3/3: Overwritten with random bit pattern for {file_path}")

            return True
        except Exception as e:
            self.logger.error(f"Failed to overwrite file {file_path}: {e}")
            return False

    def dod_7_pass(self, file_path, isUpdate=True):
        try:
            file_size = os.path.getsize(file_path)
            with open(file_path, "wb") as file:
                for i in range(7):
                    file.seek(0)
                    if i in [0, 3, 4]:
                        file.write(b"\x00" * file_size)
                        self.logger.info(f"Pass {i + 1}/7: Overwritten with binary zeroes for {file_path}")
                    elif i in [1, 5]:
                        file.write(b"\xFF" * file_size)
                        self.logger.info(f"Pass {i + 1}/7: Overwritten with binary ones for {file_path}")
                    else:
                        file.write(os.urandom(file_size))
                        self.logger.info(f"Pass {i + 1}/7: Overwritten with random data for {file_path}")
                    if isUpdate:
                        self.update_progress((i + 1) / 7 * 100)
            self.logger.info(f"7-pass overwrite completed successfully for {file_path}")
            return True
        except Exception as e:
            self.logger.error(f"Failed to securely overwrite file {file_path}: {e}")
            return False


    def perform_deletion(self, path, phases):
        if not os.path.exists(path):
            self.logger.error(f"Path does not exist: {path}")
            return  # Exit the function early

        if os.path.isdir(path):
            self.update_progress(2)
            total = 1
            for root, dirs, files in os.walk(path):
                total += len(files)+len(dirs)
            completed=0
            for root, dirs, files in os.walk(path, topdown=False):
                for file in files:
                    file_path = os.path.join(root, file)
                    if phases == 3:
                        self.dod_3_pass(file_path=file_path,isUpdate=False)
                    else:
                        self.dod_7_pass(file_path=file_path,isUpdate=False)
                    os.remove(file_path)
                    completed+=1
                    self.update_progress(int((completed / total) * 100))
                    self.logger.info(f"Deleted file: {file_path}")

                for folder in dirs:
                    folder_path = os.path.join(root, folder)
                    os.rmdir(folder_path)
                    completed+=1
                    self.update_progress(int((completed / total) * 100))
                    self.logger.info(f"Deleted folder: {folder_path}")
            os.rmdir(path)
            self.logger.info(f"Deleted root folder: {path}")

        elif os.path.isfile(path):
            success = False  # Initialize success
            try:
                if phases == 3:
                    success = self.dod_3_pass(path)
                else:
                    success = self.dod_7_pass(path)

                if success:
                    os.remove(path)
                    self.logger.info(f"Deleted file: {path}")
                else:
                    self.logger.error(f"Failed to securely overwrite file: {path}")
            except Exception as e:
                self.logger.error(f"Unexpected error while deleting {path}: {e}")
        else:
            self.logger.error(f"Unsupported file type or permission issue: {path}")

            
