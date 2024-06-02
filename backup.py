import datetime

FOLDERS_INDEXFILE = "backupFiles.txt"

print('Start backup')

# Open a log file and add initial entry.
logName = 'LogBackup'
logName += datetime.datetime.now().strftime('%Y%m%d%H%M%S')
logName += '.txt'

logFile = open(rf"D:\logs\backup\{logName}", "w")
logFile.write("Start backup\n")

with open(FOLDERS_INDEXFILE) as file:
    backupLocations = [line.rstrip() for line in file]

for backupLocation in backupLocations:
    logFile.write(backupLocation)
    logFile.write('\n')



# Close the log file
logFile.close()