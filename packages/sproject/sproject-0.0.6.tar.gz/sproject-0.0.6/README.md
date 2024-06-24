# API for finding same type of files and copy in a specific path

[![forthebadge made-with-python](http://ForTheBadge.com/images/badges/made-with-python.svg)](https://www.python.org/)                 
[![Python 3.12](https://img.shields.io/badge/python-3.12-blue.svg)](https://www.python.org/downloads/release/python-360/)   

[Follow Doveloper](https://www.instagram.com/nicky_connects/?next=%2F)
## Functionality of the Library

- Copy/Move Files Recursively.
- zip/unzip Files Recursively.
- List all the files and folders and subfolders of given path.
- In google drive you cannot directly see the size of the folder which is possible with sproject.
- count the number of files/folders and subfolders recursively
- Encrypt and Decrypt the files using AES algorithm.(Better results with Minimum of 8GB RAM)
- You can Split and Merge the large file into Smaller Chunks and viceversa.
- Automatically Playing in Queue
- Play Selected song from Playlist

## Usage

- Make sure you have Python installed in your system.
- Run Following command in the CMD.
 ```
  pip install sproject
 ```
 ```
  pip install pycryptodome
 ```
## Example

 ```
from sproject import file_organizer as f
  ```
## Functions
```
f.list_files(source_dir : str, keyword=None)

f.copy_files(path_to_sourcedir : str,path to destination dir : str)

f.move_files(source_dir : str, destination_dir : str, keyword=None)

f.delete_files(source_dir : str, keyword=None, colab=None)

f.get_folder_details(folder_path: str,colab = False)

f.zip_files(input_folder: str, zip_filename: str)

f.unzip_files(zip_filename: str, extract_dir: str)

f.encrypt(filename : str,encrypt_filepath : str,key_path : str)

f.decrypt(filename : str, key_file : str)

f.generate_key(key_file : str,show_key = False)
```
## Output 
- x files copied
- No files found with the extension

## Note 
- I have tried to implement all the functionality, it might have some bugs also. Ignore that or please try to solve that bug.
# Release 0.0.6
* Improved code functionality.
* solved page crash in colab while getting large folder details.
* Added progress bar for unzip files for easy tracking.
* you can generate your own random key using `generate_key(key_file : str,show_key = False)` Function.







