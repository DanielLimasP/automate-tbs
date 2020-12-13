import os, shutil, zipfile
from pathlib import Path
import send2trash

if __name__ == "__main__":
    p = Path.cwd()

    # Folders that make up the destination must already exist,
    # or else Python will throw an exception.
    shutil.copy(p / 'files/spam.txt', p / 'test_folder')

    shutil.copytree(p / 'files', p / 'spam_backup')

    shutil.move('C:\\bacon.txt', 'C:\\eggs')

    # Example on how to delete every file in the root
    # with the stupid file extension.
    # Remember that blob takes a regexp and returns a 
    # generator with ocurrences of said regex in path
    # that called it.
    for filename in Path.home().glob('*.stupid'):
        os.unlink(filename)

    # Calling os.unlink(path) will delete the file at path.
    # Calling os.rmdir(path) will delete the folder at path. This folder must be empty of any files or folders.
    # Calling (path) will remove the folder at path, and all files and folders it contains will also be deleted.

    # In practice, is much better to use the send2trash module
    bacon_file = open('bacon.txt', 'a')  
    bacon_file.write('Bacon is not a vegetable.')
    bacon_file.close()
    send2trash.send2trash('bacon.txt')

    # os.walk() function
    for folderName, subfolders, filenames in os.walk(p/'delicious'):
        print('The current folder is ' + folderName)

        for subfolder in subfolders:
            print('SUBFOLDER OF ' + folderName + ': ' + subfolder)

        for filename in filenames:
            print('FILE INSIDE ' + folderName + ': '+ filename)

        print('')

    # Zip files
    example_zip = zipfile.ZipFile(p/'delicious.zip')
    print(example_zip.namelist())
    zophie = example_zip.getinfo('delicious/cats/zophie.PNG')
    print(zophie.file_size)
    print(zophie.compress_size)
    print(zophie.compress_type)
    example_zip.close()

    example_zip = zipfile.ZipFile(p / 'delicious.zip')
    example_zip.extractall()
    example_zip.close()

    new_zip = zipfile.ZipFile('new_zip.zip', 'w')
    new_zip.write('idiot.py', compress_type=zipfile.ZIP_DEFLATED)



