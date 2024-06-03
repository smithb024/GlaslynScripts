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

FOLDERS_INDEXFILE = "backupFiles.txt"

print('Start backup')

# Open a log file and add initial entry.
logName = 'LogBackup'
logName += datetime.datetime.now().strftime('%Y%m%d%H%M%S')
logName += '.txt'

logFile = open(rf"D:\logs\backup\{logName}", "w")
logFile.write("Start backup\n")

backupLocations = OpenFile(FOLDERS_INDEXFILE)

for backupLocation in backupLocations:
    logFile.write(backupLocation[0])
    logFile.write('\n')
    shutil.make_archive(backupLocation[1], 'zip', backupLocation[0])
    logFile.write(f'{backupLocation[1]} Archive Complete\n')



# Close the log file
logFile.close()

print('Complete backup')