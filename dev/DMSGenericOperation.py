from pathlib import Path
from typing import List
import os

class DMSGenericOperation:

    def get_path_directory(self) -> str:
        return Path(__file__).parent.resolve()

    def create_folder(self, folder_name: str) -> bool:
        current_directory = self.get_path_directory()
        return Path(f"{current_directory/folder_name}").mkdir(parents=True, exist_ok=True)

    def get_filepaths(self, directory: str) -> List:
        file_paths = [] 

        for root, _, files in os.walk(directory):
            for filename in files:
                filepath = os.path.join(root, filename)
                file_paths.append(filepath) 
            file_paths.append(root) 
            
        file_paths = file_paths.remove(directory)
        return file_paths 

    def remove_element(self, file_path: str) -> bool:
        if os.path.isfile(file_path):
            return os.remove(file_path)
        
    def rename_path(self, file_path: str, new_filename: str) -> bool: 
        current_directory = self.get_path_directory()
        if os.path.exists(file_path):
            return os.rename(file_path, f"{current_directory}/{new_filename}")