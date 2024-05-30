import datetime

print('Start ba')

# Open a log file and add initial entry.
logName = 'LogBa'
logName += datetime.datetime.now().strftime('%Y%m%d%H%M%S')
logName += '.txt'

logFile = open(rf"D:\logs\ba\{logName}", "w")
logFile.write("Start ba\n")







# Close the log file
logFile.close()