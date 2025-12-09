import re

filename = "/mnt/shares/h/adventofcode/day5/data.txt"
ingredients = False
valid_ranges = []
fresh_items = 0

with open(filename, "r") as file_object:
    for line in file_object:
        # Remove trailing newline characters and split the line
        if re.fullmatch(r'\s*\n', line):
            ingredients = True
            continue
        if not ingredients:
            # Looking at the valid ranges
            valid_ranges.append(line.strip()) # Split each character into a list
        else:
            # looking at the items to be checked if they are in the valid ranges
            item = line.strip()
            for ranges in valid_ranges:
                bounds = ranges.split("-")
                lower_bound = bounds[0]
                upper_bound = bounds[1]
                print ("Checking item ", item, " in range ", lower_bound, " to ", upper_bound)
                if int(item) >= int(lower_bound) and int(item) <= int(upper_bound):
                    fresh_items += 1
                    break
print("Number of fresh items: ", fresh_items)