import os
import sys

def is_present(line, orig_file):
    """
    Determine whether line is present in orig_file. Return true if it is.
    param line The line to test.
    param orig_file The file to test.
    """
    with open(orig_file, "r", encoding="utf-8") as f:
        for orig_line in f:
            if orig_line == line:
                return True
    return False

def export_results(all_lines):
    """
    Save the results in a result file. One line per row in all_lines.
    param all_lines: The lines to output.
    """
    with open(".\\newLines.txt", "w") as file:
        for line in all_lines:
            file.write(line)

# Detemine which files to work on.
orig_file = sys.argv[2]
new_file = sys.argv[1]
new_lines = []

print(f"original file {orig_file}")
print(f"new file {new_file}")

# Open new_file and go through each line. Test each line to see if its present in
# orig_file. If it isn't then output it to the results file.
with open(new_file, "r", encoding="utf-8") as f:
    line_count = 0
    for line in f:
        line_count += 1
        present = is_present(line, orig_file)
        if present == False:
            print(f"{line}")
            new_lines.append(line)

export_results(new_lines)
