import pathlib
import shutil
import os,time,zipfile
from tqdm import tqdm
from Crypto.Cipher import AES
from Crypto.Random import get_random_bytes
from Crypto.Util.Padding import pad, unpad
from os import scandir
from pathlib import Path
def delete_files(source_dir:str, keyword=None, colab=None):
  files_count = 0
  folders_count = 0
  for root, _, files in os.walk(source_dir):
    for file in files:
      # Construct the full file path
      file_path = os.path.join(root, file)
      if not os.path.exists('/content/drive/MyDrive/Trash'):
        os.makedirs('/content/drive/MyDrive/Trash')
      # Apply keyword filter if provided
      if keyword and keyword.lower() not in file.lower():
        continue
      # Delete the file
      file_name = os.path.basename(file_path)
      if colab:
        try:
          os.rename(file_path,f'/content/drive/MyDrive/Trash/{file_name}')
          print(f"Deleted: {file_path}")
          files_count += 1
        except Exception as e:
          print(f"Error deleting file: {e}")
      else:
        try:
          os.remove(file_path)
          print(f"Deleted: {file_path}")
          files_count += 1
        except Exception as e:
          print(f"Error deleting file: {e}")
    # After deleting files, check if the directory is empty
    if not os.listdir(root):
      # If empty, remove the directory
      try:
        os.rmdir(root)
        print(f"Deleted directory: {root}")
        folders_count += 1
      except Exception as e:
        print(f"Error deleting directory: {e}")
  print(f'{files_count} Files and {folders_count} Folders Deleted')
def list_files(source_dir, keyword=None):
  # Check if source directory exists
  if not os.path.exists(source_dir):
    print(f"Error: Source directory '{source_dir}' does not exist.")
    return
  # Loop through files in the source directory
  for filename in os.listdir(source_dir):
    if keyword:
      # Filter based on keyword (lowercase for case-insensitivity)
      if keyword.lower() not in filename.lower():
        continue
    file_size = os.path.getsize(filename)
    print(filename,file_size)
def copy_files(source_dir, destination_dir, keyword=None, skip_if_exists=False):
        count = 0
        files_count = count_files_recursively(source_dir)
        for root, dirs, files in os.walk(source_dir):
    # Construct the corresponding subdirectory in the destination
            relative_path = os.path.relpath(root, source_dir)
            dest_subdirectory = os.path.join(destination_dir, relative_path)
    # Create the subdirectory in the destination if it doesn't exist
            if not os.path.exists(dest_subdirectory):
                os.makedirs(dest_subdirectory)
            for file in files:
                source_path = os.path.join(root, file)
                file_size = os.path.getsize(source_path)
                destination_path = os.path.join(dest_subdirectory, file)
            # Apply keyword filter if provided
                if keyword and keyword.lower() not in file.lower():
                    continue
                # Copy the file
                if os.path.exists(destination_path) and skip_if_exists:
                      count += 1
                      print(f'{destination_path} Already Exists')
                      continue
                try:
                    shutil.copy2(source_path, destination_path)
                    print(f"Copied: '{source_path}' to '{destination_path}' size = {(file_size/1024)/1024}MB")
                    count += 1
                    print(f"Copied {count}/{files_count} Files")
                except Exception as e:
                    print(f"Error copying file: {e} size = {(file_size/1024)/1024}MB")
        print(f'{count} Files Copied')
def move_files(source_dir, destination_dir, keyword=None):
        files_count = 0
        folders_count = 0
        for root, dirs, files in os.walk(source_dir):
    # Construct the corresponding subdirectory in the destination
            relative_path = os.path.relpath(root, source_dir)
            dest_subdirectory = os.path.join(destination_dir, relative_path)
    # Create the subdirectory in the destination if it doesn't exist
            if not os.path.exists(dest_subdirectory):
                os.makedirs(dest_subdirectory)
            for file in files:
                source_path = os.path.join(root, file)
                file_size = os.path.getsize(source_path)
                destination_path = os.path.join(dest_subdirectory, file)
            # Apply keyword filter if provided
                if keyword and keyword.lower() not in file.lower():
                    continue
                # Copy the file
                try:
                    os.rename(source_path, destination_path)
                    files_count += 1
                    print(f"Moved: '{source_path}' to '{destination_path}' size = {(file_size/1024)/1024}MB")
                except Exception as e:
                    print(f"Error moving file: {e} size = {(file_size/1024)/1024}MB")
            if not os.listdir(root):
            # If empty, remove the directory
              try:
                os.rmdir(root)
                folders_count += 1
                print(f"Deleted directory: {root}")
              except Exception as e:
                print(f"Error deleting directory: {e}")
        print(f'{files_count} Files and {folders_count} Folders Moved')
def greet(name : str) -> str:
    print(f'Hey {name}!')
def get_folder_details(folder_path: str,colab = False):
  if not colab:
    total_size = 0
    files_count = 0
    folders_count = 0
    for root, dirs, files in os.walk(folder_path):
        for file in files:
            file_path = os.path.join(root, file)
            total_size += os.path.getsize(file_path)
            files_count += 1
            a = f'{files_count} Files and {folders_count} Folders are found with the Total Size of {(total_size/1024)/1024} MB'
            spaces_needed = len(str(a)) + 1 
            backspaces = '\b' * spaces_needed
            print(f'{backspaces}{a}', end='', flush=True) 
        folders_count += 1
    return
  total_size = 0
  files_count = 0
  folders_count = 0
  for root, dirs, files in os.walk(folder_path):
      for file in files:
          file_path = os.path.join(root, file)
          total_size += os.path.getsize(file_path)
          files_count += 1
      folders_count += 1
  print(f'{files_count} Files and {folders_count} Folders are found with the Total Size of {(total_size/1024)/1024} MB')
def zip_files(input_folder, zip_filename):
    with zipfile.ZipFile(zip_filename, 'w', zipfile.ZIP_DEFLATED) as zipf:
        for root, dirs, files in os.walk(input_folder):
            count = 0
            for file in files:
                file_path = os.path.join(root, file)
                arcname = os.path.relpath(file_path, input_folder)  # Preserve relative structure
                zipf.write(file_path, arcname=arcname)
                count += 1
                a = f'{count} / {len(files)} files zipped'
                spaces_needed = len(str(a)) + 1
                backspaces = '\b' * spaces_needed
                print(f'{backspaces}{a}', end='', flush=True)
def unzip_files(zip_filename, extract_dir):
    with zipfile.ZipFile(zip_filename, 'r') as zipf:
        total_size = sum(zinfo.file_size for zinfo in zipf.infolist())  # Calculate total size
        with tqdm(total=total_size, unit='B', unit_scale=True, desc="Extracting") as pbar:
            for member in zipf.infolist():
                dirname = os.path.dirname(member.filename)
                if dirname:
                    os.makedirs(os.path.join(extract_dir, dirname), exist_ok=True)
                zipf.extract(member, extract_dir)
                pbar.update(member.file_size)
def decrypt(filename : str,decrypt_file_path : str, key_file : str) -> str:
    with open(key_file, 'rb') as f:
        key = f.read()
    with open(filename, 'rb') as f:
        iv = f.read(16)
        ct = f.read()
    cipher = AES.new(key, AES.MODE_CBC, iv)
    pt = unpad(cipher.decrypt(ct), AES.block_size)
    file_name = os.path.basename(filename)
    with open(f'{decrypt_file_path}/{file_name[:-4]}', 'wb') as f:
        f.write(pt)
def encrypt(filename : str,encrypt_filepath : str,key_path : str) -> str:
    with open(filename, 'rb') as f:
        data = f.read()
    with open(f'{key_path}', 'rb') as f:
        key = f.read()
    cipher = AES.new(key, AES.MODE_CBC)
    ct_bytes = cipher.encrypt(pad(data, AES.block_size))
    iv = cipher.iv
    file_name = os.path.basename(filename)
    with open(f'{encrypt_filepath}/{file_name}' + '.enc', 'wb') as f:
        f.write(iv)
        f.write(ct_bytes)
def generate_key(key_file_path : str,show_key = False) -> str:
    key = get_random_bytes(16)
    with open(f'{key_file_path}', 'wb') as f:
        f.write(key)
    print(f'Key saved to {key_file_path}')
    if show_key:
        return key
def count_files_recursively(path : str) -> str:
  total_files = 0
  for entry in scandir(path):
    if entry.is_file():
      total_files += 1
    elif entry.is_dir():
      total_files += count_files_recursively(entry.path)
  return total_files
def split_file(file_path : str, chunk_size : int , output_folder : str):
    chunk_size = chunk_size * (1024 * 1024)
    os.makedirs(output_folder, exist_ok=True)
    file_name = os.path.basename(file_path)
    with open(file_path, 'rb') as file:
        chunk_count = 1
        chunk = file.read(chunk_size)
        while chunk:
            chunk_file_path = os.path.join(output_folder, f'{file_name}_chunk{chunk_count:03d}')
            with open(chunk_file_path, 'wb') as chunk_file:
                chunk_file.write(chunk)
            print(chunk_count)
            chunk_count += 1
            chunk = file.read(chunk_size)
def merge_chunks(input_folder : str, output_file_path : str):
    with open(output_file_path, 'wb') as output_file:
        list = []
        for filename in os.listdir(input_folder):
            list.append((filename))
        list.sort()
        print(list)
        for filename in list:
            print(filename)
            chunk_path = input_folder + str(filename)
            print(f"Reading chunk: {chunk_path}")
            with open(chunk_path, 'rb') as chunk_file:
                chunk_data = chunk_file.read()
                output_file.write(chunk_data)
                print(chunk_path)