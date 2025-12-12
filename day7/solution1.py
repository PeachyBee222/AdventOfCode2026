filename = "/mnt/shares/h/adventofcode/day7/data.txt"
grid = []
num_split = 0

def print_grid(grid):
    for row in grid:
        print(row)
    print()

def recursive_method(grid_copy, row, col):
    global num_split    

    # if we are at the bottom of the grid, stop the recursion
    if row >= len(grid_copy):
        return
  
    # if the character is "S" change the character below to | and call again
    if grid_copy[row][col] == "S":
        grid_copy[row + 1][col] = "|"
        #print_grid(grid_copy)
        recursive_method(grid_copy, row + 2, col)
        return

    # base case, if character is a . and above is a | go down an index and call again
    if grid_copy[row][col] == "." and grid_copy[row-1][col] == "|":
        grid_copy[row][col] = "|"
        #print_grid(grid_copy)
        recursive_method(grid_copy, row + 1, col)
        return

    # if character is "^", change the characters to the left and right to "|" if they aren't
    # already "|", then call method again for left and right indexes
    # make sure the row above this is a |
    test_1 = grid_copy[row][col]
    test_2 = grid_copy[row - 1][col]
    if grid_copy[row][col] == "^" and grid_copy[row - 1][col] == "|":
        num_split += 1
        if col - 1 >= 0 and grid_copy[row][col - 1] != "|":
            grid_copy[row][col - 1] = "|"
            #print_grid(grid_copy)
            recursive_method(grid_copy, row + 1, col - 1)
        if col + 1 < len(grid_copy[0]) and grid_copy[row][col + 1] != "|":
            grid_copy[row][col + 1] = "|"
            #print_grid(grid_copy)
            recursive_method(grid_copy, row + 1, col + 1)
        return

with open(filename, 'r') as file_object:
    for line in file_object:
        # Strip whitespace (including newline) and split by spaces
        row = list(line.strip())
        grid.append(row)

# The grid is now in a list, we need to do our recursive method
# call method, passing grid and starting coords of letter "S"

print_grid(grid)

for row_index, row in enumerate(grid):
    # Iterate over the columns in the current row
    for col_index, char in enumerate(row):
        # Check if the current character matches the target
        if char == 'S':
            # Return the position (row, column) immediately upon finding it
            recursive_method(grid, row_index, col_index)

print("Number of splits: ", num_split)