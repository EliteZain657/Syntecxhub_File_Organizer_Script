File Organizer Bot (Python Automation Script)

A Python script that automatically organizes files in a folder based on file types. Designed for automation, QA, and DevOps tasks, with optional dry-run mode and command-line interface (CLI) for flexibility.

Features

Organize files by category (Images, Videos, Documents, Audio, Archives, Programming, Executables, Torrents, Others)

Dry-run mode: Simulate file moves without modifying files

CLI support: Specify folder, quick execution, or dry-run from the command line

Quick organization: Run script without interactive menu

Statistics tracking: Shows total files processed, moved, skipped, and errors

List files by category: Preview organized files

Cross-platform: Works on Windows, Linux, and macOS

Requirements

Python 3.8+

Standard libraries only (os, shutil, pathlib, logging, argparse, subprocess, datetime)

Works on Windows PowerShell, Command Prompt, and Linux/macOS terminals

Installation / Setup

Clone or download the project:

git clone <repository_url>


Navigate to the project folder in terminal or PowerShell:

cd "D:\INTERNSHIP\SyntecxHub\TASK 2"


Make sure your script file ends with .py (e.g., File_Organizer_modified_version.py)

Usage
Run interactive menu
python "File_Organizer_modified_version.py"


Navigate the menu to organize files, list categories, and see stats.

Quick organize (without menu)
python "File_Organizer_modified_version.py" --quick

Organize a specific folder
python "File_Organizer_modified_version.py" --folder "C:\Users\Zain\Desktop\Projects" --quick

Dry-run mode (simulate file moves)
python "File_Organizer_modified_version.py" --folder "C:\Users\Zain\Downloads" --dry-run --quick


Files remain untouched; logs show what would be moved.

Command-line arguments
Argument	Description
--folder <path>	Specify folder to organize (default: Downloads)
--dry-run	Simulate actions without moving files
--quick	Run script directly without interactive menu
File Categories
Category	Extensions
Images	.jpg, .jpeg, .png, .gif, .bmp, .svg, .webp, .tiff, .ico
Videos	.mp4, .avi, .mov, .wmv, .flv, .webm, .mkv, .m4v, .3gp
Documents	.pdf, .doc, .docx, .txt, .rtf, .odt, .xls, .xlsx, .ppt, .pptx
Audio	.mp3, .wav, .aac, .flac, .ogg, .m4a, .wma
Archives	.zip, .rar, .7z, .tar, .gz, .dmg, .pkg
Programming	.py, .js, .html, .css, .java, .cpp, .c, .php, .json, .xml
Executables	.exe, .msi, .dmg, .pkg, .deb, .rpm, .apk
Torrents	.torrent
Others	Unknown extensions
Logging

All actions are logged to file_organizer.log in the project directory.

Dry-run actions are also logged for verification.

Example Dry-Run Output
[Dry-run] Would move: report.pdf → Documents/
[Dry-run] Would move: photo.jpg → Images/
File organization completed!
📊 ORGANIZATION STATISTICS
📁 Total files processed: 12
✅ Files moved: 12
⏭️ Files skipped: 0
❌ Errors: 0

Benefits / Use Cases

QA Automation: Simulate file organization safely before executing changes.

DevOps / System Admin: Integrate script into cron jobs or Task Scheduler for scheduled folder cleanup.

Personal Automation: Keep Downloads or project folders organized automatically
