import os
import sys
import zipfile


import_path = sys.argv[1]
output_path = sys.argv[2] + ".zip"
arg = sys.argv


def checkFlags(arg = sys.argv):
    """Check if flags/arguments was used from console
    arg -- list of console arguments
    return True if flags is used"""

    if("-help" in arg or "--help" in arg or "-h" in arg):
        print('\n\n')
        print('pyBackup help \n')
        print('usage: app.py [path to import] [path to export] ')
        print('example: app.py ./import_folder_path ./output/archive_name \n')
        print('-config \t make new settings \n')

        return True

    return False

if __name__ == "__main__":

    checkFlags()
    print('Start backup from ' + import_path + ' to ' + output_path)
    z = zipfile.ZipFile(output_path, 'w')
    for root, dirs, files in os.walk(import_path):
        for file in files:
           z.write(os.path.join(root,file))

    z.close()
    print('Done!')
