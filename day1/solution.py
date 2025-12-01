# Specify the name of your text file
filename = "/mnt/shares/h/adventofcode/day1/data.txt"

starting_number = 50
current_number = starting_number
counter = 0 # Increase this every time the current number equals 0

# Open the file using a 'with' statement for automatic closing
with open(filename, "r") as file_object:
    # Iterate through each line in the file object
    for line in file_object:
        # Each 'line' variable will contain a single line from the file,
        # including the newline character at the end (e.g., '\n').

        # STEP 1:
        # Starting number is at 50
        # Separate the first character from the rest of the line
        # STEP 2:
        # If the first character is "R" add to the number based on the number from the rest of the line
        # If the first character is "L" subtract from the number based on the number from the rest of the line
        # STEP 3:
        # If going R and the number is greater than 99, set the number to 0 + remaining amount
        # If going L and the number is less than 0, set the number to 99 - remaining amount
        # STEP 4:
        # Print the final number after processing all lines
        direction = line[0]
        amount = int(line[1:].strip()) # Strip remove whitespace including newline
        if direction == "R":
            current_number += amount
            while current_number > 99:
                current_number = current_number - 100
        elif direction == "L":
            current_number -= amount
            while current_number < 0:
                current_number = 100 + current_number
        print("Current number after ", line.strip(), ": ", current_number)
        if current_number == 0:
          counter += 1
print("The number of times the current number is 0: ", counter)
        