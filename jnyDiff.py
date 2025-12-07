import os
import sys

def is_present(line, orig_file):
    with open(orig_file, "r", encoding="utf-8") as f:
        for orig_line in f:
            if orig_line == line:
                return True
    return False

def export_results(all_lines):
    """
    Save the results in a result fle. Output them as a comma separated file.
    param all_lines: The lines to output.
    """
    with open(".\\newLines.txt", "w") as file:
        for line in all_lines:
            file.write(line)
            #file.write("\n")

# Detemine which files to work on.
orig_file = sys.argv[2]
new_file = sys.argv[1]
new_lines = []

print(f"original file {orig_file}")
print(f"new file {new_file}")

with open(new_file, "r", encoding="utf-8") as f:
    line_count = 0
    for line in f:
        line_count += 1
        #print(f"Line {line_count} {line}")
        present = is_present(line, orig_file)
        if present == False:
            print(f"{line}")
            new_lines.append(line)

export_results(new_lines)
#print(f"Loaded {line_count} lines from {new_file}")
