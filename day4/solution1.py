grid = []
filename = "/mnt/shares/h/adventofcode/day4/data.txt"
moveable_paper = 0
removed_paper = 0
changes = True

def print_grid(grid):
    for row in grid:
        for element in row:
            print(element, end="  ")  # Print element with two spaces, no newline
        print()  # Print a newline after each row

def get_adjacent_characters(grid, row, col):
    """
    Retrieves the characters in the 8 adjacent spaces around a given character
    in a 2D grid.

    Args:
        grid (list of lists): The 2D grid of characters.
        row (int): The row index of the central character.
        col (int): The column index of the central character.

    Returns:
        list: A list of characters found in the 8 adjacent spaces.
    """
    adjacent_chars = []
    num_rows = len(grid)
    num_cols = len(grid[0]) if num_rows > 0 else 0

    # Relative offsets for the 8 adjacent positions
    offsets = [
        (-1, -1), (-1, 0), (-1, 1),
        (0, -1),           (0, 1),
        (1, -1),  (1, 0),  (1, 1)
    ]

    for dr, dc in offsets:
        new_row, new_col = row + dr, col + dc

        # Check if the new coordinates are within the grid boundaries
        if 0 <= new_row < num_rows and 0 <= new_col < num_cols:
            adjacent_chars.append(grid[new_row][new_col])

    return adjacent_chars

def change_adjacent_to_x(local_grid, row, col):
    """
    Changes characters in a grid to 'X' if they are horizontally or vertically
    adjacent to a character with the same value.
    
    Note: This modifies the grid in-place.
    """
    global changes, removed_paper

    num_rows = len(local_grid)
    num_cols = len(local_grid[0]) if num_rows > 0 else 0
    # A list to mark cells that need changing, to avoid changing a cell
    # and immediately using the new 'X' to trigger more changes in the same pass.
    to_modify = local_grid.copy()
    
    # Relative offsets for the 8 adjacent positions
    offsets = [
        (-1, -1), (-1, 0), (-1, 1),
        (0, -1),           (0, 1),
        (1, -1),  (1, 0),  (1, 1)
    ]

    for dr, dc in offsets:
        new_row, new_col = row + dr, col + dc

        # Check if the new coordinates are within the grid boundaries
        if 0 <= new_row < num_rows and 0 <= new_col < num_cols:
            if to_modify[new_row][new_col] == '@':
                to_modify[new_row][new_col] = 'X'
                removed_paper += 1
    if local_grid != to_modify:
        print("Grid changed:")
        print_grid(to_modify)
        changes = True
    return to_modify

with open(filename, "r") as file_object:
    for line in file_object:
        # Remove trailing newline characters and split the line
        row_elements = list(line.strip()) # Split each character into a list
        grid.append(row_elements)
    changes = True
    while(changes):
      changes = False
      for r in range(len(grid)):
          for c in range(len(grid[0])):
              current_char = grid[r][c]
              adjacent_chars = get_adjacent_characters(grid, r, c)
              if adjacent_chars.count('@') < 4:
                  if current_char == '@':
                    #print(f"Character at ({r}, {c}): '{current_char}' has adjacent characters: {adjacent_chars}")
                    moveable_paper += 1
                    # NOTE: the only difference are the lines after this between part 1 and part 2
                    # remove paper
                    grid[r][c] = 'X'
                    removed_paper += 1
                    changes = True
                    #print("Grid changed:")
                    #print_grid(grid)

    print(f"Total moveable paper pieces: {moveable_paper}")
    print(f"Total removed paper pieces: {removed_paper}")