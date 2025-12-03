# Specify the name of your text file
from numpy import number

filename = "/mnt/shares/h/adventofcode/day2/data.txt"
invalid = 0
count  = 0

# Open the file using a 'with' statement for automatic closing
with open(filename, "r") as file_object:
    # Iterate through each line in the file object
    for line in file_object:
        # separate the line by comma
        for var_range in line.split(","):
            # separate the range by hyphen
            range_parts = var_range.strip().split("-")
            # convert the range parts to integers
            start = int(range_parts[0])
            end = int(range_parts[1])
            # count up the invalid numbers. 
              # divide number by 2, if remainder is 0 then its even so we want to check it.
              # depending on what the divide is, check to see if the first half of the number is the same as the last half.
              # if they are the same, then it is invalid.
            # print("Checking range: ", start, " to ", end)
            for number in range(start, end+1):
                length = len(str(number))
                if length % 2 == 0: # if even length
                    midpoint = length // 2 #integer division
                    first_half = str(number)[:midpoint]
                    last_half = str(number)[midpoint:]
                    # print("Checking number: ", number, " First half: ", first_half, " Last half: ", last_half)
                    if first_half == last_half:
                        # print("Invalid number found: ", number)
                        invalid += number
                        count += 1
print("Total invalid number: ", invalid)
print("Total invalid count: ", count)
#test data should have 8 valid ids
#748 is too low