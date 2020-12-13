#! python3
# backupToZip.py - Copies an entire folder and its contents into
# a ZIP file whose filename increments.

import zipfile, os
from pathlib import Path

def b2z(folder):

    # Back up the entire contents of "folder" into a ZIP file.

    folder = os.path.abspath(folder)   # make sure folder is absolute

    # Figure out the filename this code should use based on
    # what files already exist.
    n = 1
    while True:
        zip_file_name = os.path.basename(folder) + '_' + str(n) + '.zip'
        if not os.path.exists(zip_file_name):
            break
        n += 1

        # Create the ZIP file.
        print(f'Creating {zip_file_name}...')
        backup_zip = zipfile.ZipFile(zip_file_name, 'w')

        # Walk the entire folder tree and compress the files in each folder.
        for foldername, subfolders, filenames in os.walk(folder):
            print(f'Adding files in {foldername}...')
            # Add the current folder to the ZIP file.
            backup_zip.write(foldername)

                # Add all the files in this folder to the ZIP file.
            for filename in filenames:
                newBase = os.path.basename(folder) + '_'
                if filename.startswith(newBase) and filename.endswith('.zip'):
                    continue   # don't back up the backup ZIP files
                backup_zip.write(os.path.join(foldername, filename))
            backup_zip.close()
            
    print('Done.')

p = Path.cwd()
b2z(p/'files')