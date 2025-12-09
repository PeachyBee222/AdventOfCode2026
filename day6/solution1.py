grid = []
grand_total = 0
current_total = 0
start_element = 0
filename = "/mnt/shares/h/adventofcode/day6/data.txt"

def print_grid(grid):
    for row in grid:
        for element in row:
            print(element, end="  ")  # Print element with two spaces, no newline
        print()  # Print a newline after each row

def do_operation(operator, element2):
    global current_total
    print(f"Doing operation: {current_total} {operator} {element2}")
    if operator == '+':
        if current_total == 0:
            current_total = int(element2)
        else:
          current_total += int(element2)
    elif operator == '*':
        if current_total == 0:
            current_total = int(element2)
        else:
          current_total *= int(element2)
    else:
        raise ValueError(f"Unsupported operator: {operator}")

with open(filename, "r") as file_object:
    for line in file_object:
        # add each number separated by some amount of whitespace to a list
        row_elements = list(line.split())
        grid.append(row_elements)
    
    print_grid(grid)

    # loop through each column in the grid
    # get the last element of the column in the grid
    for c in range(len(grid[0])):
        last_element = grid[-1][c]
        # for each row in the specific column except for the last row
        # do the mathmetical operation specified by the last element
        for r in range(len(grid)-1):
            do_operation(last_element, grid[r][c])
            # current_total += temp
        print(f"Column {c} total: {current_total} for the operator {last_element}")
        grand_total += current_total
        current_total = 0  # reset for the next column

print(f"Grand total: {grand_total}")