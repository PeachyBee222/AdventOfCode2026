# has a list of numbers that are paried with the number of spaces before them
import math

grid = []
operators = []
grand_total = 0
current_total = 0
filename = "/mnt/shares/h/adventofcode/day6/testdata.txt"

def print_grid(grid):
    for row in grid:
        for element in row:
            print(element, end="  ")  # Print element with two spaces, no newline
        print()  # Print a newline after each row

def count_spaces_iteratively():
    global filename, grid, operators
    space_count = 0
    try:            
        with open(filename, "r") as file_object:
            lines = file_object.readlines()
            num_lines = len(lines)

            for i, line in enumerate(lines):
                # the last line in the file is operators only
                if i == num_lines - 1:
                    operators = list(line.split())
                    continue
                # add each number separated by some amount of whitespace to a list
                row_element = ""
                row_elements = []
                space_count = 0
                for i, char in enumerate(line):
                    if char == ' ':
                        space_count += 1
                    else:
                        row_element = row_element + char
                        # if the next character is a space and exists
                        if i + 1 < len(line) and (line[i + 1] == ' ' or line[i + 1] == '\n'):
                            row_elements.append((row_element, int(space_count)))
                            space_count = 0
                            row_element = ""
                # row_elements = list(line.split())
                grid.append(row_elements)
        print_grid(grid)
    except FileNotFoundError:
        return f"Error: File '{filename}' not found."

def do_operation(operator, column, first = False):
    # loop through the column
    # number and number of spaces
    # add or multiply based on the operator
    # 123
    #+ 45 = 1+2+4+3+5

    global current_total

    total_per_column = []
    print(f"Doing operation: {operator} {column}")
    length = max(len(t[0]) for t in column)
    for element, spaces in column:
        temp_space = spaces
        elem_length = len(element)
        index = 0
        if operator == '+':
            while index < length:
                # if the fist column is being calculated
                if first:
                    # if there are spaces before the number, don't add anything for that space
                    # if index > elem_length:
                    #   break
                    if spaces > 0:
                        number = ""
                        spaces -= 1
                    else:
                        number = element[index-temp_space]
                    if index+1 > len(total_per_column):
                        if number != "":
                            total_per_column.append(number)
                    else:
                      total_per_column[index] = str(total_per_column[index]) + str(number)
                # if we looking at everything other than the first column
                else:
                    # this number has a space delimter before using the spaces to calculate, offset by one
                    if index >= elem_length:
                        break
                    elif spaces == 1:
                        number = element[index]
                    elif spaces > 1:
                        number = ""
                        spaces -= 1
                    else:
                        number = element[index-temp_space]
                    if index+1 > len(total_per_column):
                        if number != "":
                            total_per_column.append(number)
                    else:
                      total_per_column[index] = str(total_per_column[index]) + str(number)
                index += 1
            print(f"Total per column so far: {total_per_column}")
        elif operator == '*':
            while index < length:
                # if the fist column is being calculated
                if first:
                    # if index > elem_length:
                    #     break
                    # if there are spaces before the number, don't add anything for that space
                    if spaces > 0:
                        number = ""
                        spaces -= 1
                    else:
                        number = element[index-temp_space]
                    # if the index is not yet in total_per_column, add it
                    if index+1 > len(total_per_column):
                        if number != "":
                            total_per_column.append(number)
                    else:
                      total_per_column[index] = str(total_per_column[index]) + str(number)
                # if we looking at everything other than the first column
                else:
                    if index >= elem_length:
                        break
                    # this number has a space delimter before using the spaces to calculate, offset by one
                    elif spaces == 1:
                        number = element[index-spaces]
                    elif spaces > 1:
                        number = ""
                        spaces -= 1
                    else:
                        number = element[index-temp_space]
                    if index+1 > len(total_per_column):
                        if number != "":
                            total_per_column.append(str(number))
                        else:
                            total_per_column.append("")
                    else:
                      total_per_column[index] = str(total_per_column[index]) + str(number)
                index += 1
            print(f"Total per column so far: {total_per_column}")
        else:
            raise ValueError(f"Unsupported operator: {operator}")
    if operator == '+':
        # add the numbers together
        current_total += sum([int(x) for x in total_per_column])
        print(f"Addition current total: {current_total}")
    elif operator == '*':
        # multiply the numbers together
        product = 1
        for x in total_per_column:
        # Check if the item is a number (integer or float)
            if isinstance(x, (int, float)):
                product *= x
        current_total += product
        print(f"Multiplication current total: {current_total}")

count_spaces_iteratively()

# loop through each column in the grid
# get the last element of the column in the grid
for c in range(len(grid[0])):
    # for each row in the specific column except for the last row
    # do the mathmetical operation specified by the last element
    # for r in range(len(grid)-1):
    
    # if we are looking at the first column
    if c == 0:
        do_operation(operators[c], [row[c] for row in grid], first=True)
    else:
        do_operation(operators[c], [row[c] for row in grid])
    print(f"Column {c} total: {current_total} for the operator {operators[c]}")

    grand_total += current_total
    current_total = 0  # reset for the next column

print(f"Grand total: {grand_total}")