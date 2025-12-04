# loop through each line in the file
# each line is a bank, find the two largest numbers and add them together.
# then add each of those totals together to get the final answer.

# NOTE: the numbers must go in order so if a number is 891121, to get the highest number its 9 and 2 -> 92

filename = "/mnt/shares/h/adventofcode/day3/data.txt"
final_number = 0
overall_total  = 0
tens_digit = 0
ones_digit = 0

# Open the file using a 'with' statement for automatic closing
with open(filename, "r") as file_object:
    # Iterate through each line in the file object
    for line in file_object:
        line = line.strip()  # Remove any leading/trailing whitespace/newline characters

        tens_digit = line[0] # Start with the first digit
        ones_digit = line[1] # Start with the second digit

        # Loop through each number in the list
        for index, digit_char in enumerate(line):
            length = len(line)
            num = int(digit_char)  # Convert the string to an integer

            if index == 0:
                continue  # Skip the first digit since it's already assigned to tens_digit
            if index == length - 1:
                if int(ones_digit) < num:
                    ones_digit = digit_char
            elif int(tens_digit) < num: # increase the 10s digit and change 1s digit to the next number
                tens_digit = digit_char
                ones_digit = line[index + 1] # set this to the next number
            elif int(ones_digit) < num: # only increase the 1s digit if the 10s digit doesn't change
                ones_digit = digit_char
            
        final_number = tens_digit + ones_digit
        overall_total += int(final_number) # Add all of the largest numbers together
        print("Final number for line ", line, " is: ", final_number)

print("Overall total is: ", overall_total)