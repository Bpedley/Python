#! python3
# selectiveCopy.py - Searches for files with a certain file extension (such
# as .pdf or .jpg). Copied these files from location they are in to a
# new folder.

import os, shutil

for folderName, subfolders, filenames in os.walk('D:\\Python\\Books\\Automate the boring stuff with python'):
    for filename in filenames:
        if filename.endswith('.png'):
            print('Copiyng picture %s to %s' % (filename, 'D:\Pics'))
            shutil.copy(os.path.join(folderName, filename), 'D:\\Pics\\')
