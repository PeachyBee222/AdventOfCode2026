filename = "/mnt/shares/h/adventofcode/day7/data.txt"
grid = []
num_paths = 0

def print_grid(grid):
    for row in grid:
        print(row)
    print()

def count_paths(grid, row, col):
    """Count paths without modifying the grid - much faster!"""
    print("At position: (", row, ",", col, ")")
    # if we are at the bottom of the grid, we completed a path!
    if row >= len(grid):
        return 1
    
    # Out of bounds
    if col < 0 or col >= len(grid[0]):
        return 0
  
    current = grid[row][col]
    
    # if the character is "S", continue down
    if current == "S":
        return count_paths(grid, row + 1, col)
    
    # if character is ".", continue down
    if current == ".":
        return count_paths(grid, row + 1, col)
    
    # if character is "^", split into left and right paths
    if current == "^":
        left_paths = count_paths(grid, row + 1, col - 1)
        right_paths = count_paths(grid, row + 1, col + 1)
        return left_paths + right_paths
    
    # Any other character, no valid path
    return 0

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
            num_paths = count_paths(grid, row_index, col_index)

print("Number of different paths: ", num_paths)