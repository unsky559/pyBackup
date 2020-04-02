import os
import sys
import zipfile
import datetime
import json

MAIN_FILE_NAME = "pyBackup.py"
CONFIGURATION_FILE_NAME = "config.pybackup.json"
archive_name = "-backup.zip"
arg = sys.argv

try:
    import_path = arg[1]
except IndexError:
    import_path = None
try:
    output_path = arg[2]
except IndexError:
    output_path = None

def getCurrTimeString():
    now = datetime.datetime.now()
    return str(now.year)+'-'+str(now.month)+'-'+str(now.day)+'_'+str(now.hour)+'.'+str(now.minute)+'.'+str(now.second)

def checkFlags(arg = sys.argv):
    """Check if flags/arguments was used from console
    arg -- list of console arguments
    return True if flags is used"""


    if("-help" in arg or "--help" in arg or "-h" in arg):
        print('\n\n')
        print('pyBackup help \n')
        print('usage: '+ MAIN_FILE_NAME +' [path to import] [path to export] ')
        print('example: '+ MAIN_FILE_NAME +' ./import_folder_path ./output_path \n')
        print('-config \t to change config setup \n')
        return True
    if("-config" in arg or "--config" in arg or "-c" in arg):
        configSetup()
    return False

def makeArchive(im_path = import_path, out_path = output_path, arch_name = getCurrTimeString()+archive_name):
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


def configInit():
    """Initialize a config file"""

    if(os.path.exists(CONFIGURATION_FILE_NAME)):
        print('Config file finded.')
        config_file = open(CONFIGURATION_FILE_NAME, 'r')
        CONFIGURATION = json.JSONDecoder().decode(config_file.read())
    else:
        configSetup()
        print('Config file does not exits. Creating new one')

def configSetup():
    print('Running a config setup')
    config = {}
    config['default_folder_import'] = str(input('Path to default import folder: '))
    config['default_folder_export'] = str(input('Path to default export folder: '))
    n = input('Number of backups (If the number of backups exceeds this number, the oldest backup will be deleted. Leave blank to disable this option.): ')
    if(n):
        config['number_of_backups'] = int(n)
    else:
        config['number_of_backups'] = 0
    json_str = json.JSONEncoder().encode(config)
    config_file = open(CONFIGURATION_FILE_NAME, 'w')
    config_file.write(json_str)
    config_file.close()
    configInit()

def readConfig():
    if(os.path.exists(CONFIGURATION_FILE_NAME)):
        print('Try to load settings.')
        config_file = open(CONFIGURATION_FILE_NAME, 'r')
        CONFIGURATION = json.JSONDecoder().decode(config_file.read())
        return CONFIGURATION
    else:
        print('Config file does not exits.')
        return None

def doStuff(import_path, output_path):
    if(os.access(output_path, os.W_OK)):
        makeArchive(import_path, output_path)
    else:
        print('Can not access folder. Try to create newone')
        if not os.path.exists(output_path):
            os.makedirs(output_path)
            print('Creating success')
            makeArchive(import_path, output_path)
        else:
            print('Error: Access is denied')


def removeOldest(number_of_backups):
    if(number_of_backups):
        dir_list = os.listdir(output_path)
        if(len(dir_list) > number_of_backups):
            print("Number of backups exceeds. Start to remove the oldest one.")
            os.remove(output_path+"/"+dir_list[0])

if __name__ == "__main__":

    checkFlags()
    configInit()
    conf = readConfig()


    try:
        import_path = conf['default_folder_import']
    except IndexError:
        import_path = None

    try:
        output_path = conf['default_folder_export']
    except IndexError:
        output_path = None

    try:
        number_of_backups = conf['number_of_backups']
    except IndexError:
        number_of_backups = None

    if(import_path and output_path):
        doStuff(import_path, output_path)
        removeOldest(number_of_backups)


    else:
        print('Error. No input/output path. Set it using -c or -config')
