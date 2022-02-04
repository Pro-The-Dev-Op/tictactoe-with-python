
'import modules to zip unzip file'
import zipfile
import os
import shutil
import sys
'function to unzip file'
def unzip(file_name):
    'unzip file'
    with zipfile.ZipFile(file_name, 'r') as zip_ref:
        zip_ref.extractall('unzipped')
'function to zip file'
def zip(file_name):
    'zip file'
    with zipfile.ZipFile(file_name + '.zip', 'w') as zip_ref:
        zip_ref.write(file_name)
'function to delete file'
def delete(file_name):
    'delete file'
    os.remove(file_name)
'function to rename file'
def rename(file_name, new_name):
    'rename file'
    os.rename(file_name, new_name)
'function to copy file'
def copy(file_name, new_name):
    'copy file'
    shutil.copy(file_name, new_name)
'function to move file'
def move(file_name, new_name):
    'move file'
    shutil.move(file_name, new_name)
'function to check if file exists'
def exists(file_name):
    'check if file exists'
    return os.path.isfile(file_name)
'function to check if directory exists'
def directory_exists(directory_name):
    'check if directory exists'
    return os.path.isdir(directory_name)
'function to check if file is empty'
def is_empty(file_name):
    'check if file is empty'
    return os.stat(file_name).st_size == 0
'function to check if file is not empty'
def is_not_empty(file_name):
    'check if file is not empty'
    return os.stat(file_name).st_size != 0
'function to check if file is a directory'
def is_directory(file_name):

    'check if file is a directory'
    return os.path.isdir(file_name)
'function to check if file is a file'
def is_file(file_name):
    'check if file is a file'
    return os.path.isfile(file_name)
'function to check if file is a link'
def is_link(file_name):
    'check if file is a link'
    return os.path.islink(file_name)
'function to check if file is a socket'
def is_socket(file_name):
    'check if file is a socket'
    return os.path.isfile(file_name)
'function to check if file is a block device'
def is_block_device(file_name):
    'check if file is a block device'
    return os.path.isfile(file_name)
'function to check if file is a character device'
def is_character_device(file_name):
    'check if file is a character device'
    return os.path.isfile(file_name)
'function to check if file is a fifo'
def is_fifo(file_name):
    'check if file is a fifo'
    return os.path.isfile(file_name)
'function to check if file is a symbolic link'
def is_symbolic_link(file_name):
    'check if file is a symbolic link'
    return os.path.islink(file_name)
'function to check if file is a regular file'
def is_regular_file(file_name):
    'check if file is a regular file'
    return os.path.isfile(file_name)