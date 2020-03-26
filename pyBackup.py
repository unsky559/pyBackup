import os
import sys
import zipfile

MAIN_FILE_NAME = "pyBackup.py"
import_path = sys.argv[1]
output_path = sys.argv[2]
archive_name = "backup.zip"
output_full_path = output_path + "/" + archive_name
arg = sys.argv


def checkFlags(arg = sys.argv):
    """Check if flags/arguments was used from console
    arg -- list of console arguments
    return True if flags is used"""

    if("-help" in arg or "--help" in arg or "-h" in arg):
        print('\n\n')
        print('pyBackup help \n')
        print('usage: '+ MAIN_FILE_NAME +' [path to import] [path to export] ')
        print('example: '+ MAIN_FILE_NAME +' ./import_folder_path ./output_path \n')
        print('-config \t make new settings \n')
        return True
    return False

if __name__ == "__main__":

    checkFlags()

    if(os.access(output_path, os.W_OK)):
        print('Start backup from ' + import_path + ' to ' + output_full_path)

        z = zipfile.ZipFile(output_full_path, 'w')
        for root, dirs, files in os.walk(import_path):
            for file in files:
               z.write(os.path.join(root,file))
        z.close()

        print('Done!')
    else:
        print('Error: can not access to output path')
