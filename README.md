# Python Desktop Sorter

A simple Python script that organizes desktop items into folders by file extension and records what it moved.

## Setup

Requires Python 3. The script uses only the Python standard library, so no additional packages need to be installed.

Open `DesktopSorter.py` in a text editor and change `SOURCE_DIRECTORY` near the top to the full path of the folder you want to organize. Replace `YOUR_USERNAME` with your Windows username, or enter a different folder:

```python
SOURCE_DIRECTORY = r'C:\Users\YOUR_USERNAME\Desktop'
```

Keep the `r` before the quotes when using Windows paths, then save the script. The folder must already exist; an invalid or relative path produces a setup message before anything is moved.

You can keep this project anywhere on your computer. It organizes the configured folder regardless of where the script is stored, and no separate config file is needed.

## Usage

Open a terminal in this project folder and run:

```sh
python DesktopSorter.py
```

The script immediately moves matching items into the category folders below, creating those folders as needed. It scans the source folder's immediate entries without recursively scanning subfolders. Extension matching is case-insensitive.

| Destination folder | File types |
| --- | --- |
| `Obrázky` | `.png`, `.jpg`, `.jpeg`, `.gif`, `.bmp` |
| `Dokumenty\Dokumenty` | `.txt`, `.doc`, `.docx`, `.pdf` |
| `Dokumenty\Rar` | `.rar`, `.zip`, `.7z` |
| `Programy` | `.exe`, `.lnk` shortcuts |

Other entries remain in the source folder. If an item with the same name already exists in its destination, the move fails and the script stops; earlier moves remain completed.

## Logs

After sorting completes, the script writes two files in the terminal's current working folder:

- `log.txt`: appends the run's date, time, and number of moved items.
- `list_YYYYMMDDHHMMSS.txt`: lists the names of the items moved during that run.

## Customize categories

Edit the `categories` dictionary in `DesktopSorter.py` to change folder names or supported extensions. Destination folders are created inside `SOURCE_DIRECTORY`.
