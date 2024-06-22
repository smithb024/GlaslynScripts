import datetime

# Open the named file and return the contents.
def OpenFile(filename):
    contents = []
    with open(filename) as csvFile:
        csvReader = csv.reader(csvFile, delimiter=',')
        lineCount = 0
        for row in csvReader:
            content = []
            contents.append(content)
            lineCount += 1
        logFile.write(f'Processed {lineCount} lines.')
    return contents

print('Start ba')

# Open a log file and add initial entry.
logName = 'LogBa'
logName += datetime.datetime.now().strftime('%Y%m%d%H%M%S')
logName += '.txt'

logFile = open(rf"D:\logs\ba\{logName}", "w")
logFile.write("Start ba\n")







# Close the log file
logFile.close()