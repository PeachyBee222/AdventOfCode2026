import re

filename = "/mnt/shares/h/adventofcode/day5/data.txt"
ingredients = False
valid_ranges = []
fresh_items = 0

valid_ids = 0
valid_ids_no_overlap = []

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
            # once we have all of the ranges, we want to find and count
            # the valid ranges since sometimes the ranges will overlap
            for ranges in valid_ranges:
                bounds = ranges.split("-")
                lower_bound = bounds[0]
                upper_bound = bounds[1]
                for bound in range(int(lower_bound), int(upper_bound)+1):
                    if bound not in valid_ids_no_overlap:
                        #print("Adding valid id: ", bound)
                        valid_ids_no_overlap.append(bound)
                print("Valid ids no overlap: ", valid_ids_no_overlap)
valid_ids = len(valid_ids_no_overlap)
print("Number of valid ids: ", valid_ids)