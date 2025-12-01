# Specify the name of your text file
filename = "/mnt/shares/h/adventofcode/day1/data.txt"

starting_number = 50
current_number = starting_number
counter = 0 # Increase this every time the current number equals or passes over 0
looping = True

# Open the file using a 'with' statement for automatic closing
with open(filename, "r") as file_object:
    # Iterate through each line in the file object
    for line in file_object:
        # Each 'line' variable will contain a single line from the file,
        # including the newline character at the end (e.g., '\n').

        direction = line[0]
        amount = int(line[1:].strip()) # Strip remove whitespace including newline
        if direction == "R":
            current_number += amount
            looping = True
            # Count how many complete wraps we make (crossing 0 each time)
            while looping:
                if current_number > 99:
                    current_number = current_number - 100
                    counter += 1 #crossed 0 or landed on 0
                    print("R counter increased")
                else:
                    looping = False

        elif direction == "L":
            current_number -= amount
            looping = True
            while looping:
                if current_number == 0:
                    counter += 1
                    print("L landed on zero counter increased")
                    looping = False
                # when the previous number is zero is when we hit issues here. It would go into the negatives and add a counter which would double count from when it first turned zero
                if current_number + amount == 0:
                    current_number = 100 + current_number
                elif current_number < 0:
                    current_number = 100 + current_number
                    counter += 1 #crossed 0 or landed on 0
                    print("L counter increased")
                else:
                    looping = False
        
        print("Current number after ", line.strip(), ": ", current_number)
print("The number of times the current number is or passed 0: ", counter)


# INCORRECT:
# 4646 is too low. this uses  if current_number != 0 and current_number < 0:
# 6480 is too high. this uses  if current_number != 0:
# 6561 is too high. this uses a counter inside the while loop
# 6067 is incorrect. This uses the counter only inside the while loop
# 5564 is incorrect. This uses the counter both inside the while loop and when landing exactly on 0 and if previous number was zero, subtract 1 from the double counted counter
# 6067 without while loops and using modulo and integer division