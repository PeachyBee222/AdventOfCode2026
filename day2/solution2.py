# Specify the name of your text file
from numpy import number

def check_repeat(main_number, target_number) -> int:
    main_str = str(main_number)
    target_str = str(target_number)
    count = main_str.count(target_str)
    if count > 1:
        return count
    else:
        return  0


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
                # loop through each digit in the number, checking to see if the digit(s) repeat in the rest of the number
                for i in range(length):
                  repeated = 1
                  first_part = str(number)[:i]
                  last_part = str(number)[i:]

                  # need to check that the last repeated digit(s) are the end of the number
                  times_repeated = check_repeat(number, first_part)
                  # print ("Number: ", number, " First part: ", first_part, " Last part: ", last_part, " Times repeated: ", times_repeated)

                  # if the number of times repeated times the length of the first part equals original length
                  # then the sequence is repeated throughout the number
                  if(times_repeated * len(str(first_part)) == len(str(number))):
                      repeated += 1

                  # if sequence repeated more than once, then its invalid
                  if repeated > 1:
                      # print ("Repeated Number: ", number, " First part: ", first_part, " Last part: ", last_part, " Times repeated: ", times_repeated)
                      invalid += number
                      count += 1
                      break

print("Total invalid number: ", invalid)
print("Total invalid count: ", count)
#test data should have 8 valid ids
#748 is too low