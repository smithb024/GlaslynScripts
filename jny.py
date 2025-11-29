import os
import sys

def read_all_lines(folder_path):
    """
    Read all the txt files in the folder path. Analyse each line to determine
    all unique file lines. Sort them and return them.
    :param folder_path: The path.
    """
    all_lines = []

    for filename in os.listdir(folder_path):
        if filename.lower().endswith(".txt"):
            file_path = os.path.join(folder_path, filename)

            with open(file_path, "r", encoding="utf-8") as f:
                line_count = 0
                for line in f:
                    line_count += 1
                    route = split_line(line)
                    if exists(all_lines, route) == False:
                        all_lines.append(route)
                print(f"Loaded {line_count} lines from {file_path}")

    all_lines.sort()
    return all_lines

def split_line(line):
    """
    The line is tab separated. Split the line and return elements 2,3 and 4.
    Ensure that elements 2 and 3 are sorted alphabetically.
    :param line: The line to split.
    """
    parts = line.split("\t")
    alphabetical_route = sort_two_strings(parts[2], parts[3])
    route = [alphabetical_route[0], alphabetical_route[1], parts[4]]
    return route

def sort_two_strings(a: str, b: str):
    """
    Sort two string alphabetically.
    """
    return tuple(sorted([a, b]))

def exists(all_lines, route):
    """
    Go through the all_lines array and see if the route is already present. 
    Return a flag indicating presence.
    param all_lines: An array of known routes
    param route: The route to check
    """
    for line in all_lines:
        if line[0] == route [0] and line[1] == route [1] and line[2] == route [2]:
            return True
    return False

def export_results(all_lines):
    """
    Save the results in a result fle. Output them as a comma separated file.
    param all_lines: The lines to output.
    """
    with open(".\\results.txt", "w") as file:
        for line in all_lines:
            comma_separated = ",".join(line)
            file.write(comma_separated)
            file.write("\n")

# Read the base folder from the command line input.
folder = sys.argv[1]
lines = read_all_lines(folder)
export_results(lines)

print(f"Output {len(lines)} lines")
