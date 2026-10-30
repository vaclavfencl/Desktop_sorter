import os
import shutil
from datetime import datetime

# Set this to the full path of the folder you want to organize.
# Replace YOUR_USERNAME with your Windows username, or enter another folder.
# Keep the r before the quotes so Windows backslashes are handled correctly.
SOURCE_DIRECTORY = r'C:\Users\YOUR_USERNAME\Desktop'

def move_files(source_dir, target_dir, file_extensions, moved_files):
    if not os.path.exists(target_dir):
        os.makedirs(target_dir)
    for file in os.listdir(source_dir):
        if file.lower().endswith(file_extensions):
            full_file_path = os.path.join(source_dir, file)
            shutil.move(full_file_path, target_dir)
            moved_files.append(file)
    return moved_files

def log_moved_files(moved_files, log_filename, list_filename):
    now = datetime.now()
    date_str = now.strftime("%Y%m%d%H%M%S")
    list_file_path = f'{list_filename}_{date_str}.txt'

    with open(list_file_path, 'w', encoding='utf-8') as f:
        for file in moved_files:
            f.write(file + '\n')

    with open(log_filename, 'a', encoding='utf-8') as f:
        log_entry = f"{now.strftime('%Y-%m-%d %H:%M:%S')}, {len(moved_files)} files\n"
        f.write(log_entry)

def main():
    if not os.path.isabs(SOURCE_DIRECTORY) or not os.path.isdir(SOURCE_DIRECTORY):
        raise SystemExit(
            "Set SOURCE_DIRECTORY at the top of DesktopSorter.py "
            "to the full path of an existing folder before running."
        )

    categories = {
        'Obrázky': ('.png', '.jpg', '.jpeg', '.gif', '.bmp'),
        r'Dokumenty\Dokumenty': ('.txt', '.doc', '.docx', '.pdf'),
        r'Dokumenty\Rar': ('.rar', '.zip', '.7z'),
        'Programy': ('.exe','lnk')
    }

    all_moved_files = []

    for category, extensions in categories.items():
        target_directory = os.path.join(SOURCE_DIRECTORY, category.replace('\\', os.sep))
        move_files(SOURCE_DIRECTORY, target_directory, extensions, all_moved_files)

    log_moved_files(all_moved_files, 'log.txt', 'list')

if __name__ == "__main__":
    main()
