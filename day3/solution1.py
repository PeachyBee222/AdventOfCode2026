# loop through each line in the file
# each line is a bank, find the two largest numbers and add them together.
# then add each of those totals together to get the final answer.

# NOTE: the numbers must go in order so if a number is 891121, to get the highest number its 9 and 2 -> 92

filename = "/mnt/shares/h/adventofcode/day2/data.txt"
final_number = 0
overall_total  = 0
tens_digit = 0
ones_digit = 0

# Open the file using a 'with' statement for automatic closing
with open(filename, "r") as file_object:
    # Iterate through each line in the file object
    for line in file_object:
        line = line.strip()  # Remove any leading/trailing whitespace/newline characters
        numbers = line.split(",")  # Split the line into individual number strings

        # Initialize the two largest numbers to very small values
        largest = -1
        second_largest = -1

        # Loop through each number in the list
        for num_str in numbers:
            num = int(num_str)  # Convert the string to an integer

            # Update largest and second largest accordingly
            if num > largest:
                second_largest = largest
                largest = num
            elif num > second_largest:
                second_largest = num

        # Add the two largest numbers together and add to overall total
        overall_total += (largest + second_largest)