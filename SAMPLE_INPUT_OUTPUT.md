# Python Automation Script - Sample Input/Output

## 📋 Overview
This is a Smart File Organizer & Cleaner automation script that handles various file operations with proper logging and exception handling.

---

## ✨ Features Implemented

✅ **OS Module Usage** - Uses `os`, `shutil`, `datetime` modules  
✅ **Exception Handling** - Try-except blocks throughout  
✅ **Logging System** - All operations logged to `logs.txt`  
✅ **User Input Support** - Interactive menu with multiple options  
✅ **File Operations** - Organize, sort, clean, rename files  

---

## 🎯 Sample Scenarios

### **Scenario 1: Organizing Files by Extension**

**INPUT:**
```
Welcome to Smart File Organizer & Cleaner!
==================================================

📂 Enter folder path to work with: C:\Users\Documents\TestFolder

==================================================
📁 SMART FILE ORGANIZER & CLEANER
==================================================

🔧 Choose an operation:
  1. Organize files by extension
  2. Sort files by date (newest first)
  3. Sort files by date (oldest first)
  4. Sort files by size (largest first)
  5. Sort files by size (smallest first)
  6. Remove empty files
  7. Remove duplicate files
  8. View folder statistics
  9. Exit
==================================================

👉 Enter your choice (1-9): 1
```

**OUTPUT:**
```
📂 Organizing files...

✅ Moved: document_1.pdf --> PDF/
✅ Moved: image_2.jpg --> JPG/
✅ Moved: spreadsheet_3.xlsx --> XLSX/
✅ Moved: video_4.mp4 --> MP4/
✅ Moved: readme_5.txt --> TXT/

🎉 All files organized successfully!
```

**LOG ENTRY (logs.txt):**
```
2026-05-16 14:23:45.123456 - Created folder: C:\Users\Documents\TestFolder\PDF
2026-05-16 14:23:45.234567 - Renamed: document.pdf -> document_1.pdf
2026-05-16 14:23:45.345678 - Moved file: document_1.pdf to folder: PDF
2026-05-16 14:23:46.456789 - Created folder: C:\Users\Documents\TestFolder\JPG
... (similar entries for other files)
2026-05-16 14:23:50.123456 - All files organized successfully
```

---

### **Scenario 2: Sorting Files by Date**

**INPUT:**
```
👉 Enter your choice (1-9): 2
```

**OUTPUT:**
```
📅 Files sorted by newest files first:
  1. report_new.docx - Modified: 2026-05-16 10:30:00
  2. budget_2026.xlsx - Modified: 2026-05-15 09:15:00
  3. notes.txt - Modified: 2026-05-14 16:45:00
  4. archive_old.zip - Modified: 2026-05-10 12:00:00
```

---

### **Scenario 3: Sorting Files by Size**

**INPUT:**
```
👉 Enter your choice (1-9): 4
```

**OUTPUT:**
```
📊 Files sorted by size (largest first):
  1. video_file.mp4 - Size: 450.25 KB
  2. presentation.pptx - Size: 125.75 KB
  3. document.pdf - Size: 45.50 KB
  4. notes.txt - Size: 2.10 KB
```

---

### **Scenario 4: Removing Empty Files**

**INPUT:**
```
👉 Enter your choice (1-9): 6
```

**OUTPUT:**
```
🧹 Cleaning empty files...
  ✅ Removed empty file: temp_file.tmp
  ✅ Removed empty file: cache.dat
  ✅ Removed empty file: empty.txt

✅ Removed 3 empty file(s)
```

**LOG ENTRY:**
```
2026-05-16 14:30:15.123456 - Removed empty file: temp_file.tmp
2026-05-16 14:30:15.234567 - Removed empty file: cache.dat
2026-05-16 14:30:15.345678 - Removed empty file: empty.txt
2026-05-16 14:30:15.456789 - Cleaned empty files - Removed 3 file(s)
```

---

### **Scenario 5: Removing Duplicates**

**INPUT:**
```
👉 Enter your choice (1-9): 7
```

**OUTPUT:**
```
🔍 Searching for duplicate files...
  ✅ Removed duplicate: report_1.txt
  ✅ Removed duplicate: image_2.jpg

✅ Removed 2 duplicate file(s)
```

---

### **Scenario 6: Viewing Folder Statistics**

**INPUT:**
```
👉 Enter your choice (1-9): 8
```

**OUTPUT:**
```
📊 Folder Statistics:
  📄 Total Files: 15
  📁 Total Folders: 3
  💾 Total Size: 2.45 MB
```

---

### **Scenario 7: Exit Program**

**INPUT:**
```
👉 Enter your choice (1-9): 9
```

**OUTPUT:**
```
✅ Thank you for using Smart File Organizer!
```

---

## 🛡️ Error Handling Examples

### **Non-existent Folder:**
```
📂 Enter folder path to work with: C:\NonExistent\Path

🔧 Choose an operation:
...

👉 Enter your choice (1-9): 1

❌ Folder does not exist!
```

### **Invalid Choice:**
```
👉 Enter your choice (1-9): 15

❌ Invalid choice! Please enter a number between 1-9.
```

### **Empty Folder:**
```
📂 Organizing files...

⚠️ Folder is empty!
```

---

## 📝 Log File Example (logs.txt)

```
2026-05-16 14:00:00.123456 - === PROGRAM STARTED ===
2026-05-16 14:00:15.234567 - Created folder: C:\Users\Documents\TestFolder\PDF
2026-05-16 14:00:15.345678 - Renamed: document.pdf -> document_1.pdf
2026-05-16 14:00:15.456789 - Moved file: document_1.pdf to folder: PDF
2026-05-16 14:00:16.567890 - Created folder: C:\Users\Documents\TestFolder\JPG
2026-05-16 14:00:16.678901 - Renamed: image.jpg -> image_2.jpg
2026-05-16 14:00:16.789012 - Moved file: image_2.jpg to folder: JPG
2026-05-16 14:00:17.890123 - All files organized successfully
2026-05-16 14:30:15.123456 - Sorted files by date (newest)
2026-05-16 14:30:45.234567 - Removed empty file: temp.tmp
2026-05-16 14:30:45.345678 - Cleaned empty files - Removed 1 file(s)
2026-05-16 14:45:00.456789 - === PROGRAM ENDED ===
```

---

## 🚀 How to Run

### **Windows:**
```bash
python "Python Automation Script.py"
```

### **Linux/Mac:**
```bash
python3 "Python Automation Script.py"
```

---

## 📋 Requirements Met

| Requirement | Status | Details |
|---|---|---|
| Use OS module & exception handling | ✅ | `os`, `shutil` modules used; Try-except in all functions |
| Generate logs for operations | ✅ | `write_log()` function creates logs.txt with timestamps |
| Add user input support | ✅ | Interactive menu with 9 different operations |
| File operations | ✅ | Organize, rename, sort, clean, remove duplicates |
| Sample input/output | ✅ | Multiple scenarios documented above |

---

## 🎓 Key Functions

1. **`write_log(message)`** - Logs operations with timestamp
2. **`create_folder(folder_path)`** - Creates folder if not exists
3. **`rename_file(file_path, count)`** - Renames file with numbering
4. **`organize_files(folder_path)`** - Organizes by extension
5. **`sort_files_by_date(folder_path, order)`** - Sorts by modification date
6. **`sort_files_by_size(folder_path, order)`** - Sorts by file size
7. **`clean_empty_files(folder_path)`** - Removes empty files
8. **`remove_duplicates(folder_path)`** - Removes duplicate files
9. **`view_folder_stats(folder_path)`** - Shows folder statistics
10. **`main()`** - Main program loop with menu

---

## 💡 Notes

- All operations are logged to `logs.txt` for audit trail
- Exception handling prevents script from crashing on errors
- User can perform multiple operations in single session
- Logs include timestamps for all operations
- Safe file handling with proper error messages
