# ==========================================
# SMART FILE ORGANIZER & CLEANER
# Python Automation Internship Project
# ==========================================

import os
import shutil
from datetime import datetime

# ==========================================
# LOG FUNCTION
# ==========================================

def write_log(message):
    """
    Writes operation logs into logs.txt
    """
    with open("logs.txt", "a", encoding="utf-8") as log_file:
        log_file.write(f"{datetime.now()} - {message}\n")


# ==========================================
# CREATE FOLDER IF NOT EXISTS
# ==========================================

def create_folder(folder_path):
    """
    Creates folder if it doesn't exist
    """
    if not os.path.exists(folder_path):
        os.makedirs(folder_path)
        write_log(f"Created folder: {folder_path}")


# ==========================================
# RENAME FILE FUNCTION
# ==========================================

def rename_file(file_path, count):
    """
    Renames file with numbering
    """
    folder = os.path.dirname(file_path)

    file_name = os.path.basename(file_path)
    name, extension = os.path.splitext(file_name)

    new_name = f"{name}_{count}{extension}"
    new_path = os.path.join(folder, new_name)

    os.rename(file_path, new_path)

    write_log(f"Renamed: {file_name} -> {new_name}")

    return new_path


# ==========================================
# ORGANIZE FILES FUNCTION
# ==========================================

def organize_files(folder_path):

    try:

        # Check folder exists
        if not os.path.exists(folder_path):
            print("❌ Folder does not exist!")
            write_log("ERROR: Folder does not exist")
            return

        files = os.listdir(folder_path)

        # Empty folder check
        if len(files) == 0:
            print("⚠️ Folder is empty!")
            write_log("Folder is empty")
            return

        print("\n📂 Organizing files...\n")

        count = 1

        for file in files:

            file_path = os.path.join(folder_path, file)

            # Skip folders
            if os.path.isdir(file_path):
                continue

            # Skip log file
            if file == "logs.txt":
                continue

            try:

                # Rename file
                renamed_path = rename_file(file_path, count)

                # Get new file name
                renamed_file = os.path.basename(renamed_path)

                # Get extension
                extension = renamed_file.split(".")[-1].upper()

                # Handle files without extension
                if "." not in renamed_file:
                    extension = "NO_EXTENSION"

                # Create extension folder
                extension_folder = os.path.join(folder_path, extension)

                create_folder(extension_folder)

                # Final move path
                final_path = os.path.join(extension_folder, renamed_file)

                # Move file
                shutil.move(renamed_path, final_path)

                print(f"✅ Moved: {renamed_file} --> {extension}/")

                write_log(
                    f"Moved file: {renamed_file} to folder: {extension}"
                )

                count += 1

            except Exception as file_error:

                print(f"❌ Error processing file {file}: {file_error}")

                write_log(
                    f"ERROR processing file {file}: {file_error}"
                )

        print("\n🎉 All files organized successfully!")

        write_log("All files organized successfully")

    except Exception as e:

        print(f"\n❌ Main Error: {e}")

        write_log(f"MAIN ERROR: {e}")


# ==========================================
# SORT FILES BY DATE
# ==========================================

def sort_files_by_date(folder_path, order="newest"):
    """
    Sorts files by modification date
    order: 'newest' or 'oldest'
    """
    try:
        if not os.path.exists(folder_path):
            print("❌ Folder does not exist!")
            write_log("ERROR: Folder does not exist for sorting")
            return

        files = os.listdir(folder_path)
        file_list = []

        for file in files:
            file_path = os.path.join(folder_path, file)
            if os.path.isfile(file_path):
                mod_time = os.path.getmtime(file_path)
                file_list.append((file, mod_time))

        # Sort by modification time
        file_list.sort(key=lambda x: x[1], reverse=(order == "newest"))

        print(f"\n📅 Files sorted by {order} files first:")
        for idx, (file, mod_time) in enumerate(file_list, 1):
            date_str = datetime.fromtimestamp(mod_time).strftime("%Y-%m-%d %H:%M:%S")
            print(f"  {idx}. {file} - Modified: {date_str}")

        write_log(f"Sorted files by date ({order})")

    except Exception as e:
        print(f"❌ Error sorting files: {e}")
        write_log(f"ERROR sorting files: {e}")


# ==========================================
# SORT FILES BY SIZE
# ==========================================

def sort_files_by_size(folder_path, order="largest"):
    """
    Sorts files by size
    order: 'largest' or 'smallest'
    """
    try:
        if not os.path.exists(folder_path):
            print("❌ Folder does not exist!")
            write_log("ERROR: Folder does not exist for sorting")
            return

        files = os.listdir(folder_path)
        file_list = []

        for file in files:
            file_path = os.path.join(folder_path, file)
            if os.path.isfile(file_path):
                size = os.path.getsize(file_path)
                file_list.append((file, size))

        # Sort by size
        file_list.sort(key=lambda x: x[1], reverse=(order == "largest"))

        print(f"\n📊 Files sorted by size ({order} first):")
        for idx, (file, size) in enumerate(file_list, 1):
            size_kb = size / 1024
            print(f"  {idx}. {file} - Size: {size_kb:.2f} KB")

        write_log(f"Sorted files by size ({order})")

    except Exception as e:
        print(f"❌ Error sorting files: {e}")
        write_log(f"ERROR sorting files: {e}")


# ==========================================
# CLEAN FILES - REMOVE EMPTY FILES
# ==========================================

def clean_empty_files(folder_path):
    """
    Removes empty files from folder
    """
    try:
        if not os.path.exists(folder_path):
            print("❌ Folder does not exist!")
            write_log("ERROR: Folder does not exist for cleaning")
            return

        files = os.listdir(folder_path)
        removed_count = 0

        print("\n🧹 Cleaning empty files...")

        for file in files:
            file_path = os.path.join(folder_path, file)

            if os.path.isfile(file_path) and os.path.getsize(file_path) == 0:
                try:
                    os.remove(file_path)
                    print(f"  ✅ Removed empty file: {file}")
                    write_log(f"Removed empty file: {file}")
                    removed_count += 1
                except Exception as e:
                    print(f"  ❌ Could not remove {file}: {e}")
                    write_log(f"ERROR removing {file}: {e}")

        if removed_count == 0:
            print("  ℹ️ No empty files found!")
        else:
            print(f"\n✅ Removed {removed_count} empty file(s)")

        write_log(f"Cleaned empty files - Removed {removed_count} file(s)")

    except Exception as e:
        print(f"❌ Error cleaning files: {e}")
        write_log(f"ERROR cleaning files: {e}")


# ==========================================
# CLEAN FILES - REMOVE DUPLICATES
# ==========================================

def remove_duplicates(folder_path):
    """
    Removes duplicate files based on name
    """
    try:
        if not os.path.exists(folder_path):
            print("❌ Folder does not exist!")
            write_log("ERROR: Folder does not exist for duplicate removal")
            return

        files = os.listdir(folder_path)
        seen = {}
        removed_count = 0

        print("\n🔍 Searching for duplicate files...")

        for file in sorted(files):
            file_path = os.path.join(folder_path, file)

            if os.path.isfile(file_path):
                base_name = os.path.splitext(file)[0]

                if base_name in seen:
                    try:
                        os.remove(file_path)
                        print(f"  ✅ Removed duplicate: {file}")
                        write_log(f"Removed duplicate file: {file}")
                        removed_count += 1
                    except Exception as e:
                        print(f"  ❌ Could not remove {file}: {e}")
                        write_log(f"ERROR removing duplicate {file}: {e}")
                else:
                    seen[base_name] = file

        if removed_count == 0:
            print("  ℹ️ No duplicates found!")
        else:
            print(f"\n✅ Removed {removed_count} duplicate file(s)")

        write_log(f"Removed duplicates - Deleted {removed_count} file(s)")

    except Exception as e:
        print(f"❌ Error removing duplicates: {e}")
        write_log(f"ERROR removing duplicates: {e}")


# ==========================================
# DISPLAY MENU
# ==========================================

def display_menu():
    """
    Displays user menu with all operations
    """
    print("\n" + "=" * 50)
    print("📁 SMART FILE ORGANIZER & CLEANER")
    print("=" * 50)
    print("\n🔧 Choose an operation:")
    print("  1. Organize files by extension")
    print("  2. Sort files by date (newest first)")
    print("  3. Sort files by date (oldest first)")
    print("  4. Sort files by size (largest first)")
    print("  5. Sort files by size (smallest first)")
    print("  6. Remove empty files")
    print("  7. Remove duplicate files")
    print("  8. View folder statistics")
    print("  9. Exit")
    print("=" * 50)


# ==========================================
# VIEW FOLDER STATISTICS
# ==========================================

def view_folder_stats(folder_path):
    """
    Displays statistics about folder
    """
    try:
        if not os.path.exists(folder_path):
            print("❌ Folder does not exist!")
            write_log("ERROR: Folder does not exist for statistics")
            return

        files = os.listdir(folder_path)
        total_files = len([f for f in files if os.path.isfile(os.path.join(folder_path, f))])
        total_folders = len([f for f in files if os.path.isdir(os.path.join(folder_path, f))])
        total_size = 0

        for file in files:
            file_path = os.path.join(folder_path, file)
            if os.path.isfile(file_path):
                total_size += os.path.getsize(file_path)

        print("\n📊 Folder Statistics:")
        print(f"  📄 Total Files: {total_files}")
        print(f"  📁 Total Folders: {total_folders}")
        print(f"  💾 Total Size: {total_size / (1024 * 1024):.2f} MB")

        write_log(f"Viewed folder statistics - Files: {total_files}, Folders: {total_folders}")

    except Exception as e:
        print(f"❌ Error viewing statistics: {e}")
        write_log(f"ERROR viewing statistics: {e}")


# ==========================================
# MAIN PROGRAM
# ==========================================

def main():
    """
    Main program loop with menu
    """
    try:
        write_log("=== PROGRAM STARTED ===")
        print("\n" + "=" * 50)
        print("Welcome to Smart File Organizer & Cleaner!")
        print("=" * 50)

        folder_path = input("\n📂 Enter folder path to work with: ").strip()

        if not folder_path:
            print("❌ Invalid folder path!")
            write_log("ERROR: Empty folder path provided")
            return

        while True:
            display_menu()
            choice = input("\n👉 Enter your choice (1-9): ").strip()

            if choice == "1":
                organize_files(folder_path)
            elif choice == "2":
                sort_files_by_date(folder_path, "newest")
            elif choice == "3":
                sort_files_by_date(folder_path, "oldest")
            elif choice == "4":
                sort_files_by_size(folder_path, "largest")
            elif choice == "5":
                sort_files_by_size(folder_path, "smallest")
            elif choice == "6":
                clean_empty_files(folder_path)
            elif choice == "7":
                remove_duplicates(folder_path)
            elif choice == "8":
                view_folder_stats(folder_path)
            elif choice == "9":
                print("\n✅ Thank you for using Smart File Organizer!")
                write_log("=== PROGRAM ENDED ===")
                break
            else:
                print("❌ Invalid choice! Please enter a number between 1-9.")

    except KeyboardInterrupt:
        print("\n\n⚠️ Program interrupted by user!")
        write_log("Program interrupted by user")
    except Exception as e:
        print(f"\n❌ Unexpected error: {e}")
        write_log(f"UNEXPECTED ERROR: {e}")


if __name__ == "__main__":
    main()