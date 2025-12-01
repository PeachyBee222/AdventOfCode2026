# Specify the name of your text file
filename = "/mnt/shares/h/adventofcode/day1/data.txt"

starting_number = 50
current_number = starting_number
counter = 0 # Increase this every time the current number equals or passes over 0
previous_number = starting_number

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
            previous_number = current_number
            current_number += amount
            # Count how many complete wraps we make (crossing 0 each time)
            while current_number > 99:
                current_number = current_number - 100
                counter += 1 #crossed 0 or landed on 0
                #print("R Counter increased: prev # =", previous_number, " current# =", current_number, " counter =", counter)

        elif direction == "L":
            previous_number = current_number
            current_number -= amount
            #if previous_number == 0:
                #counter -= 1  # Adjust for double counting when starting from 0
            #if current_number == 0:
                #counter += 1  # We landed exactly on 0
                #print("L Counter ON zero: prev # =", previous_number, " current# =", current_number, " counter =", counter)
            while current_number < 0:
                current_number = 100 + current_number
                counter += 1 #crossed 0 or landed on 0
                #print("L Counter increased: prev # =", previous_number, " current# =", current_number, " counter =", counter)
        
        print("Current number after ", line.strip(), ": ", current_number)
print("The number of times the current number is or passed 0: ", counter)


# INCORRECT:
# 4646 is too low. this uses  if current_number != 0 and current_number < 0:
# 6480 is too high. this uses  if current_number != 0:
# 6561 is too high. this uses a counter inside the while loop
# 6067 is incorrect. This uses the counter only inside the while loop
# 5564 is incorrect. This uses the counter both inside the while loop and when landing exactly on 0 and if previous number was zero, subtract 1 from the double counted counter
# 6025 is incorrect.
# 6119 is incorrect.
# 6106 is RIGHT!