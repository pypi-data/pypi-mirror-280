import os
import shutil
from typing import List

class FolderError(Exception):
    """Custom exception for folder management errors."""
    pass

class Folder:
    def __init__(self, path: str):
        self.path = os.path.abspath(path)

    def create_folder(self) -> bool:
        """Create a new folder at the specified path."""
        try:
            os.makedirs(self.path, exist_ok=True)
            return True
        except OSError as e:
            raise FolderError(f"Error creating folder: {e}")

    def list_files(self) -> List[str]:
        """List all files in the folder."""
        try:
            return os.listdir(self.path)
        except OSError as e:
            raise FolderError(f"Error listing files: {e}")

    def count_files(self) -> int:
        """Count the number of files in the folder."""
        try:
            return len(os.listdir(self.path))
        except OSError as e:
            raise FolderError(f"Error counting files: {e}")

    def create_file(self, file_name: str, content: str = "") -> bool:
        """Create a new file with the specified content."""
        try:
            with open(os.path.join(self.path, file_name), 'w') as file:
                file.write(content)
            return True
        except OSError as e:
            raise FolderError(f"Error creating file '{file_name}': {e}")

    def delete_file(self, file_name: str) -> bool:
        """Delete the specified file."""
        try:
            os.remove(os.path.join(self.path, file_name))
            return True
        except OSError as e:
            raise FolderError(f"Error deleting file '{file_name}': {e}")

    def delete_folder(self) -> bool:
        """Delete the folder and all its contents."""
        try:
            shutil.rmtree(self.path)
            return True
        except OSError as e:
            raise FolderError(f"Error deleting folder '{self.path}': {e}")

    def folder_exists(self) -> bool:
        """Check if the folder exists."""
        return os.path.exists(self.path)

    def file_exists(self, file_name: str) -> bool:
        """Check if a file exists in the folder."""
        return os.path.isfile(os.path.join(self.path, file_name))

# Example usage:
if __name__ == "__main__":
    folder = Folder("/path/to/folder")
    if folder.create_folder():
        print("Folder created successfully.")
