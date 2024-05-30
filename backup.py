import datetime

print('Start backup')

# Open a log file and add initial entry.
logName = 'LogBackup'
logName += datetime.datetime.now().strftime('%Y%m%d%H%M%S')
logName += '.txt'

logFile = open(rf"D:\logs\backup\{logName}", "w")
logFile.write("Start backup\n")







# Close the log file
logFile.close()