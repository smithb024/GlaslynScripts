import os

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
                for line in f:
                    route = split_line(line)
                    if exists(all_lines, route) == False:
                        all_lines.append(route)

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

folder = "C:\\"   # <-- change this
lines = read_all_lines(folder)

print(f"Loaded {len(lines)} lines:")
for line in lines:
    print(line)
