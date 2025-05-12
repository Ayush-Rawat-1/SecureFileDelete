import os
import logging
import tkinter as tk
from tkinter import filedialog, messagebox, ttk
from tkinter.scrolledtext import ScrolledText
import DODDeletion as DOD
import CryptographicErasure as CE

class PermanentDeleteSystem:
    def __init__(self, root):
        self.root = root
        self.root.title("Permanent Delete System")
        self.root.geometry("600x600")

        # Logging setup
        self.logger = self.setup_logging()

        # DODDeletion instance
        self.deletion_handler = DOD.DODDeletion(self.logger, self.update_progress)

        # File selection
        self.file_paths = []
        self.file_label = tk.Label(root, text="No files selected", fg="blue", cursor="hand2")
        self.file_label.pack(pady=10)

        self.select_button = tk.Button(root, text="Select Files", command=self.select_files)
        self.select_button.pack(pady=5)

        self.select_folder_button = tk.Button(root, text="Select Folder", command=self.select_folder)
        self.select_folder_button.pack(pady=5)

        # Phase selection
        self.phase_var = tk.IntVar(value=3)  # Default to 3-phase
        self.phase_label = tk.Label(root, text="Select Deletion Method:")
        self.phase_label.pack(pady=5)

        self.phase_3 = tk.Radiobutton(root, text="DoD 3-Pass", variable=self.phase_var, value=3)
        self.phase_3.pack()

        self.phase_7 = tk.Radiobutton(root, text="DoD 7-Pass", variable=self.phase_var, value=7)
        self.phase_7.pack()

        self.phase_crypto = tk.Radiobutton(root, text="Cryptographic Erasure", variable=self.phase_var, value=0)
        self.phase_crypto.pack()

        # Progress bar
        self.progress = ttk.Progressbar(root, orient="horizontal", length=400, mode="determinate")
        self.progress.pack(pady=10)

        # Log display
        self.log_label = tk.Label(root, text="Logs:")
        self.log_label.pack(pady=5)

        self.log_text = ScrolledText(root, height=10)
        self.log_text.pack(fill="both", expand=True)

        # OK button
        self.ok_button = tk.Button(root, text="OK", command=self.perform_deletion)
        self.ok_button.pack(pady=20)

    def setup_logging(self):
        logging.basicConfig(
            filename="deletion_log.txt",
            level=logging.INFO,
            format="%(asctime)s - %(message)s",
        )
        return logging.getLogger()

    def select_files(self):
        self.file_paths = filedialog.askopenfilenames(title="Select files to delete")
        if self.file_paths:
            self.file_label.config(text=f"Selected {len(self.file_paths)} file(s)")

    def select_folder(self):
        folder_path = filedialog.askdirectory(title="Select folder to delete")
        if folder_path:
            self.file_paths.append(folder_path)
            self.file_label.config(text=f"Selected folder: {folder_path}")

    def update_progress(self, value):
        self.progress["value"] = value
        self.root.update_idletasks()

    def log_message(self, message):
        self.log_text.config(state="normal")
        self.log_text.insert(tk.END, message + "\n")
        self.log_text.config(state="disabled")
        self.log_text.yview(tk.END)

    def perform_deletion(self):
        if not self.file_paths:
            messagebox.showwarning("No Files", "Please select files first.")
            return

        phases = self.phase_var.get()
        crypto_handler = CE.CryptographicErasure(self.logger, self.update_progress)

        for file_path in self.file_paths:
            self.log_message(f"Processing: {file_path}")

            try:
                if os.path.isdir(file_path) or os.path.isfile(file_path):
                    if phases == 0:
                        crypto_handler.perform_deletion(file_path)
                    else:
                        self.deletion_handler.perform_deletion(file_path, phases)

                    self.logger.info(f"Completed deletion for: {file_path}")
                    self.log_message(f"Successfully deleted: {file_path}")
                else:
                    self.log_message(f"Invalid path or file already deleted: {file_path}")
            except Exception as e:
                self.logger.error(f"Error during deletion of {file_path}: {e}")
                self.log_message(f"Error during deletion of {file_path}: {e}")

        self.update_progress(0)
        self.file_paths = []
        self.file_label.config(text="No files selected")
        messagebox.showinfo("Success", "Deletion process completed!")

if __name__ == "__main__":
    root = tk.Tk()
    app = PermanentDeleteSystem(root)
    root.mainloop()
