import os
import shutil
import subprocess
from pathlib import Path
import logging
from datetime import datetime
import argparse

class FileOrganizerBot:
    """A bot to organize files in a folder into categories"""

    def __init__(self, folder_path=None, dry_run=False):
        self.folder_path = folder_path or str(Path.home() / "Downloads")
        self.dry_run = dry_run
        self.setup_logging()

        # File categories and extensions
        self.categories = {
            'Images': ['.jpg', '.jpeg', '.png', '.gif', '.bmp', '.svg', '.webp', '.tiff', '.ico'],
            'Videos': ['.mp4', '.avi', '.mov', '.wmv', '.flv', '.webm', '.mkv', '.m4v', '.3gp'],
            'Documents': ['.pdf', '.doc', '.docx', '.txt', '.rtf', '.odt', '.xls', '.xlsx', '.ppt', '.pptx'],
            'Audio': ['.mp3', '.wav', '.aac', '.flac', '.ogg', '.m4a', '.wma'],
            'Archives': ['.zip', '.rar', '.7z', '.tar', '.gz', '.dmg', '.pkg'],
            'Programming': ['.py', '.js', '.html', '.css', '.java', '.cpp', '.c', '.php', '.json', '.xml'],
            'Executables': ['.exe', '.msi', '.dmg', '.pkg', '.deb', '.rpm', '.apk'],
            'Torrents': ['.torrent'],
            'Others': []
        }

        # Stats tracking
        self.stats = {'total_files': 0, 'moved_files': 0, 'skipped_files': 0, 'errors': 0}

    def setup_logging(self):
        logging.basicConfig(
            level=logging.INFO,
            format='%(asctime)s - %(levelname)s - %(message)s',
            handlers=[logging.FileHandler('file_organizer.log'), logging.StreamHandler()]
        )
        self.logger = logging.getLogger(__name__)

    def check_folder(self):
        if not os.path.exists(self.folder_path):
            self.logger.error(f"Folder not found: {self.folder_path}")
            return False
        return True

    def get_file_category(self, extension):
        for category, extensions in self.categories.items():
            if extension.lower() in extensions:
                return category
        return 'Others'

    def create_category_folders(self):
        for category in self.categories.keys():
            category_path = os.path.join(self.folder_path, category)
            if not os.path.exists(category_path) and not self.dry_run:
                os.makedirs(category_path)
                self.logger.info(f"Created folder: {category}")
            elif self.dry_run:
                self.logger.info(f"[Dry-run] Would create folder: {category}")

    def safe_move_file(self, source_path, dest_folder):
        filename = os.path.basename(source_path)
        dest_path = os.path.join(dest_folder, filename)

        # Conflict resolution
        if os.path.exists(dest_path):
            name, ext = os.path.splitext(filename)
            timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
            filename = f"{name}_{timestamp}{ext}"
            dest_path = os.path.join(dest_folder, filename)
            self.logger.warning(f"File exists, renaming to: {filename}")

        if self.dry_run:
            self.logger.info(f"[Dry-run] Would move: {source_path} → {dest_folder}")
            return True

        try:
            shutil.move(source_path, dest_path)
            return True
        except Exception as e:
            self.logger.error(f"Error moving {filename}: {str(e)}")
            return False

    def organize_files(self):
        if not self.check_folder():
            return False

        self.logger.info(f"Starting organization of: {self.folder_path}")
        self.create_category_folders()
        self.stats = {'total_files': 0, 'moved_files': 0, 'skipped_files': 0, 'errors': 0}

        for filename in os.listdir(self.folder_path):
            file_path = os.path.join(self.folder_path, filename)

            if os.path.isdir(file_path) or filename.startswith('.'):
                continue

            self.stats['total_files'] += 1
            extension = os.path.splitext(filename)[1]
            category = self.get_file_category(extension)
            category_path = os.path.join(self.folder_path, category)

            if os.path.dirname(file_path) == category_path:
                self.stats['skipped_files'] += 1
                continue

            if self.safe_move_file(file_path, category_path):
                self.stats['moved_files'] += 1
                self.logger.info(f"Moved: {filename} → {category}/")
            else:
                self.stats['errors'] += 1

        self.logger.info("File organization completed!")
        self.print_stats()
        return True

    def print_stats(self):
        print("\n" + "="*50)
        print("📊 ORGANIZATION STATISTICS")
        print("="*50)
        print(f"📁 Total files processed: {self.stats['total_files']}")
        print(f"✅ Files moved: {self.stats['moved_files']}")
        print(f"⏭️ Files skipped: {self.stats['skipped_files']}")
        print(f"❌ Errors: {self.stats['errors']}")
        print("="*50)

    def list_files_by_category(self):
        if not self.check_folder():
            return

        print("\n📂 FILES BY CATEGORY:")
        print("="*40)
        for category in self.categories.keys():
            category_path = os.path.join(self.folder_path, category)
            if os.path.exists(category_path):
                files = os.listdir(category_path)
                if files:
                    print(f"\n{category.upper()} ({len(files)} files):")
                    for file in files[:10]:
                        print(f"  📄 {file}")
                    if len(files) > 10:
                        print(f"  ... and {len(files)-10} more files")

def main():
    parser = argparse.ArgumentParser(description="Python File Organizer Bot")
    parser.add_argument('-f', '--folder', type=str, help="Folder path to organize")
    parser.add_argument('-d', '--dry-run', action='store_true', help="Simulate actions without moving files")
    parser.add_argument('-q', '--quick', action='store_true', help="Quick organization without menu")
    args = parser.parse_args()

    organizer = FileOrganizerBot(folder_path=args.folder, dry_run=args.dry_run)

    if args.quick:
        print("🚀 Quick organizing...")
        organizer.organize_files()
    else:
        while True:
            print("\n" + "="*60)
            print("🤖 FILE ORGANIZER BOT")
            print("="*60)
            print("1. 🗂️  Organize Folder")
            print("2. 📊  Show File Categories")
            print("3. 📈  Show Statistics")
            print("4. 🚪  Exit")
            print("="*60)

            choice = input("Enter your choice (1-4): ").strip()

            if choice == '1':
                organizer.organize_files()
            elif choice == '2':
                organizer.list_files_by_category()
            elif choice == '3':
                organizer.print_stats()
            elif choice == '4':
                print("👋 Exiting File Organizer Bot!")
                break
            else:
                print("❌ Invalid choice! Try again.")

if __name__ == "__main__":
    main()
