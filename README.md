# pyBackup
This python script is intended for automatically creating simple cli zip/rar backup system

## Usage
To run in manual mode use

    python pyBackup.py ./import_folder_path ./output_path

To run in config mode use

    python pyBackup.py

Launching for the first time entails launching configuration settings

**Required** _Path to default import folder:_ It is a path from where pyBackup will make backups

**Required** _Path to default export folder:_ Path to folder where pyBackup will store your backups (if not exists, it will be created automatically)

_Number of backups:_ The number, how many backups will stored at export folder. It will remove the oldest if number of archives exceeds this number. Leave it blank if you do not need it

To rebuild config use

    python pyBackup.py -c

To get help use

    python pyBackup.py -help
