import csv
import datetime
import os.path
import shutil
import sys

# Open the named file and return the contents.
def OpenFile(filename):
    contents = []
    with open(filename) as csvFile:
        csvReader = csv.reader(csvFile, delimiter=',')
        lineCount = 0
        for row in csvReader:
            print(f'OpenFile {filename} - line is {", ".join(row)}')
            contents.append(row)
            lineCount += 1
        print(f'Processed {lineCount} lines.')
    return contents

# Delete all the files in a folder.
def DeleteAllFilesInFolder(path):
    logFile.write(f"Delete all files from {path}\n")
    try:
        files = os.listdir(path)
        for file in files:
            filePath = os.path.join(path, file)
            if os.path.isfile(filePath):
                os.remove(filePath)
    except:
        logFile.write("ERROR: issue while deleting files.\n")
        exitScript()
    logFile.write("All files deleted successfully.\n")

# exit the script
def exitScript():
    logFile.write("Fault occurred. Exiting the script\n")
    logFile.close()
    sys.exit(1)

FOLDERS_INDEXFILE = "backupFiles.txt"
DESTINATION_PATH = "D:\\backups"
SECONDARY_PATH = "D:\\backups2"

print('Start backup')

# Open a log file and add initial entry.
logName = 'LogBackup'
logName += datetime.datetime.now().strftime('%Y%m%d%H%M%S')
logName += '.txt'

logFile = open(rf"D:\logs\backup\{logName}", "w")
logFile.write("Start backup\n\n")

# Save the previous backup
# Clear some space by emptying the location where the previous backup will go.
logFile.write("Clear the secondary location\n")
DeleteAllFilesInFolder(SECONDARY_PATH)
logFile.write("\n")

# Get a list of all the files in the previous backup
backedUpFiles = os.listdir(DESTINATION_PATH)

# Copy previous back up to the new location
logFile.write("Copy previous backup to a secondary location\n")
print('Copying old')
try:
    for fileName in backedUpFiles:
        logFile.write(f"Copying {fileName} to secondary backup location\n")
        print(f'Copying {fileName}')
        shutil.copy(f'{DESTINATION_PATH}\\{fileName}', f'{SECONDARY_PATH}\\{fileName}')
except:
    logFile.write("ERROR: Failed on copy to secondary backup location")
    exitScript()

logFile.write("All previous back up files copied\n\n")

# Clear the backup location prior to the archive state.
logFile.write("Clear the backup location\n")
print('Clear the backup location')
DeleteAllFilesInFolder(DESTINATION_PATH)
logFile.write("\n")

# Begin backing up
logFile.write("Begin archiving folders\n")
print('Archiving')
try:
    backupLocations = OpenFile(FOLDERS_INDEXFILE)

    for backupLocation in backupLocations:
        compressedFile = f'{DESTINATION_PATH}\\{backupLocation[1]}'
        print(f'Archiving {backupLocation[0]}')
        logFile.write(f'Archiving {backupLocation[0]}')
        shutil.make_archive(compressedFile, 'zip', backupLocation[0])
    
        if os.path.exists(f'{compressedFile}.zip'):
            logFile.write(f'{backupLocation[1]} archive is complete\n')
            print(f'{backupLocation[1]} archive is complete')
        else:
            logFile.write(f'{backupLocation[1]}: ERROR Failed to archive\n')
            print(f'{backupLocation[1]} ERROR Failed to archive')
            exitScript()
except:
    logFile.write("ERROR: Failed on backup")
    exitScript()

logFile.write("All folders archived\n\n")

# Close the log file
logFile.close()

print('Complete backup')