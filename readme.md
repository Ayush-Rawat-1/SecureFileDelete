# 🔒 Permanent Delete System

A secure file sanitization and deletion tool built with **Python**. It supports both **DoD overwrite algorithms** (3-pass and 7-pass) and **AES-256 Cryptographic Erasure** to ensure that files and folders are permanently unrecoverable.

---

## ✅ Features

* GUI-based application for ease of use
* Supports secure deletion of individual files and entire folders
* Implements **DoD 3-Pass and 7-Pass overwrite algorithms**
* Implements **AES-256 Cryptographic Erasure** (new)
* Displays real-time progress of deletion
* Maintains logs of all activities
* Select between overwrite or encryption-based erasure modes
* Displays detailed logs within the application

---

## 🔐 Deletion Methods

### DoD 3-Pass Method

1. Overwrite with binary zeroes (`0x00`)
2. Overwrite with binary ones (`0xFF`)
3. Overwrite with random data

### DoD 7-Pass Method

1. Overwrite with binary zeroes
2. Overwrite with binary ones
3. Overwrite with random data
4. Overwrite with binary zeroes
5. Overwrite with binary ones
6. Overwrite with random data
7. Overwrite with random data

### AES-256 Cryptographic Erasure (New)

* Encrypts file contents using **AES-256 in GCM mode** with a random key.
* The encrypted data is then written back to disk and securely deleted.
* Provides modern, cryptographic-grade sanitization, especially useful for SSDs where overwriting may not reliably erase data.

---

## 🔐 Use Cases

### 🟢 DoD 3-Pass Method

* Best for **regular users** who want strong but **fast** secure deletion
* Suitable for **non-sensitive personal files** (documents, images, temporary files)
* Provides a good balance between speed and security

---

### 🟡 DoD 7-Pass Method

* Recommended for **highly sensitive data** where stronger sanitization is required
* Common in **corporate or government environments** with strict data policies
* Ideal for **HDDs (magnetic drives)** where overwriting is very effective
* More secure than 3-pass but slower

---

### 🔴 AES-256 Cryptographic Erasure

* Best for **modern storage devices (SSDs/Flash memory)** where overwriting may not be reliable
* Suitable for **confidential files** such as legal, financial, or healthcare data
* Provides **cryptographic-grade sanitization** — recovery is computationally infeasible
* Faster than multi-pass overwriting on large SSDs
* Highly suitable for cloud storage, where physical overwrite methods cannot be guaranteed

---

## 🚀 How to Use

1. **Launch the Application**
   Run the script using Python 3.11+:

   ```bash
   python Delete_App.py
   ```

2. **Select Files or Folders**
   Use the **"Select Files"** or **"Select Folder"** buttons to choose what you want to erase.

3. **Choose Erasure Method**

   * **DoD 3-Pass**
   * **DoD 7-Pass**
   * **Cryptographic Erasure (AES-256)**

4. **Start Deletion**
   Click **"OK"** to begin the process. Logs and progress will be shown in real-time.

5. **Completion**
   A message box will confirm when the deletion is complete.

---

## 🧰 Requirements

* Python 3.11 or higher
* Tkinter (bundled with Python standard library)
* PyCryptodome (`pip install pycryptodome`)

---

## 📁 Project Structure

```
.
├── Delete_App.py            # Main application GUI
├── DODDeletion.py           # Core logic for DoD overwrite deletion
├── CryptographicErasure.py  # AES-256 Cryptographic Erasure handler
├── AESCipher.py             # AES-256 encryption/decryption implementation
├── deletion_log.txt         # Log file of all operations
└── README.md                # Project overview and instructions
```

---

## 📝 Logging

All deletion/encryption activity is logged in `deletion_log.txt`, including:

* Files/folders processed
* Overwrite/encryption passes completed
* Errors or failures (if any)

---

## ⚠️ Disclaimer

This tool is designed for **secure and permanent data deletion**. Once files or folders are deleted using this tool, **they cannot be recovered**. Please use responsibly.

---

