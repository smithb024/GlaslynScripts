import csv
import datetime

# Open the named file and return the contents.
def OpenFile(filename):
    contents = []
    with open(filename) as csvFile:
        csvReader = csv.reader(csvFile, delimiter=',')
        ignoreLine = True
        lineCount = 0

        
        for row in csvReader:
            if ignoreLine:
                logFile.write(f"Number of cells {len(row)}.\n")
                ignoreLine = False
                
                # Create arrays in contents
                numberOfArrays = (len(row) - 3)/2
                logFile.write(f"Number of arrays to create: {numberOfArrays}.\n")
                for i in range(0, int(numberOfArrays)):
                    content = []
                    contents.append(content)
                continue
                
            # Populate arrays in contents
            logFile.write(f"Row to analyse: {row}\n")
            for i in range(0, int(numberOfArrays)):
                index = i + 1
                logFile.write(f"Indexes interested in: {index * 2}: {index * 2 + 1}\n")
                if row[index * 2]:
                    logFile.write(f"{index} (1) {row[index * 2]}\n")
                    contents[i].append(row[index * 2])
                if row[index * 2 + 1]:
                    logFile.write(f"{index} (2) {row[index * 2 + 1]}\n")
                    contents[i].append(row[index * 2 + 1])
            lineCount += 1
        logFile.write(f"Processed {lineCount} lines.\n")
    return contents

print('Start ba')

# Open a log file and add initial entry.
logName = 'LogBa'
logName += datetime.datetime.now().strftime('%Y%m%d%H%M%S')
logName += '.txt'

logFile = open(rf"D:\logs\ba\{logName}", "w")
logFile.write("Start ba\n")

stn = OpenFile('stn.csv')
logFile.write(f"Number of returned cells {len(stn)}.\n")

for row in stn:
    logFile.write(f"stn row count {len(row)}.\n")

for output in stn[0]:
    logFile.write(f"output: {output}.\n")


# Close the log file
logFile.close()