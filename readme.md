# Permanent Delete System

A secure file deletion application built with Python and Tkinter that performs permanent deletion using the U.S. Department of Defense (DoD) standard overwrite algorithms. It supports both 3-pass and 7-pass deletion methods to ensure that files and folders are unrecoverable.

## ✅ Features

- GUI-based application for ease of use
- Supports secure deletion of individual files and entire folders
- Implements 3-pass and 7-pass DoD overwrite algorithms
- Displays real-time progress of deletion
- Maintains logs of all deletion activities
- Select between 3-pass and 7-pass modes
- Displays detailed logs within the application

## 🔐 Overwrite Methods

### 3-Pass DoD Method

1. Overwrite with binary zeroes (`0x00`)
2. Overwrite with binary ones (`0xFF`)
3. Overwrite with random data

### 7-Pass DoD Method

1. Overwrite with binary zeroes
2. Overwrite with binary ones
3. Overwrite with random data
4. Overwrite with binary zeroes
5. Overwrite with binary ones
6. Overwrite with random data
7. Overwrite with random data

## 🚀 How to Use

1. **Launch the Application**  
   Run the script using Python 3.x:

   ```bash
   python Delete_App.py
   ```

2. **Select Files or Folders**  
   Use the **"Select Files"** or **"Select Folder"** buttons to choose what you want to permanently delete.

3. **Choose Deletion Phase**  
   Select either **3-Phase** or **7-Phase** overwrite mode.

4. **Start Deletion**  
   Click **"OK"** to begin the secure deletion process. Logs and progress will be shown in real-time.

5. **Completion**  
   A message box will confirm when the deletion is complete.

## 🧰 Requirements

- Python 3.6 or higher
- Tkinter (comes bundled with standard Python distributions)

## 📁 Project Structure

```
.
├── Delete_App.py        # Main application GUI
├── DODDeletion.py       # Core logic for secure deletion
├── deletion_log.txt     # Log file of all operations
└── README.md            # Project overview and instructions
```

## 📝 Logging

All deletion activity is logged in `deletion_log.txt`, including:

- Files/folders processed
- Overwrite passes completed
- Errors or failures (if any)

## ⚠️ Disclaimer

This tool is designed for **secure and permanent data deletion**. Once files or folders are deleted using this tool, **they cannot be recovered**. Please use responsibly.