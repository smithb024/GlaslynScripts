import csv
import datetime
import os.path
import shutil

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

def exitProgram():
    logFile.write("Fault occurred. Exiting the script")
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
# Get a list of all the files in the previous backup
backedUpFiles = os.listdir(DESTINATION_PATH)

# Copy previous back up to the new location
logFile.write("Copy previous backup to a secondary location\n")
print('Copying old')
try:
    for fileName in backedUpFiles:
        logFile.write(f"Copying {fileName} to secondary backup location\n")
        shutil.copy(f'{DESTINATION_PATH}\\{fileName}', f'{SECONDARY_PATH}\\{fileName}')
except:
    logFile.write("ERROR: Failed on copy to secondary backup location")
    exitProgram()

logFile.write("All previous back up files copied\n\n")

# Begin backing up
logFile.write("Begin archiving folders\n")
print('Archiving')
try:
    backupLocations = OpenFile(FOLDERS_INDEXFILE)

    for backupLocation in backupLocations:
        compressedFile = f'{DESTINATION_PATH}\\{backupLocation[1]}'
        logFile.write(f'Archive {backupLocation[0]}\n')
        shutil.make_archive(compressedFile, 'zip', backupLocation[0])
    
        if os.path.exists(f'{compressedFile}.zip'):
            logFile.write(f'{backupLocation[1]} archive is complete\n')
        else:
            logFile.write(f'{backupLocation[1]}: ERROR Failed to archive\n')
            exitProgram()
except:
    logFile.write("ERROR: Failed on backup")
    exitProgram()

logFile.write("All folders archived\n\n")

# Close the log file
logFile.close()

print('Complete backup')