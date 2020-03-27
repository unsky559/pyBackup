import os
import sys
import zipfile

MAIN_FILE_NAME = "pyBackup.py"
import_path = sys.argv[1]
output_path = sys.argv[2]
archive_name = "backup.zip"
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

def makeArchive(im_path = import_path, out_path = output_path, arch_name = archive_name):
    """Creating a new archive in exitxings path
    im_path -- path to folder from where you need to make archive
    out_path -- path to folder to export archive
    arch_name -- name of archive that gonna be created"""


    output_full_path = out_path + "/" + arch_name
    print('Start backup from ' + im_path + ' to ' + output_full_path)
    z = zipfile.ZipFile(output_full_path, 'w')
    for root, dirs, files in os.walk(im_path):
        for file in files:
           z.write(os.path.join(root,file))
    z.close()

    print('Done!')

if __name__ == "__main__":

    checkFlags()

    if(os.access(output_path, os.W_OK)):
        makeArchive()
    else:
        print('Can not access folder. Try to create newone')
        if not os.path.exists(output_path):
            print('Creating success')
            os.makedirs(output_path)
            makeArchive()
        else:
            print('Error: Access is denied')

            
