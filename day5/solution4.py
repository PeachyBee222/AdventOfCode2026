# THIS NEEDS TO BE MORE EFFECIENT
from operator import index
import re

filename = "/mnt/shares/h/adventofcode/day5/data.txt"
ingredients = False
valid_ranges = []
fresh_items = 0

valid_ids = 0
valid_range_no_overlap = []

def check_itself():
    global valid_range_no_overlap
    going = True
    valid_range_no_overlap.sort()
    copy_no_overlap = valid_range_no_overlap.copy()
    while going:
      valid_range_no_overlap.sort()
      copy_no_overlap = valid_range_no_overlap.copy()
      for index1, item1 in enumerate(copy_no_overlap):
          bounds1 = item1.split("-")
          lower1 = bounds1[0]
          upper1 = bounds1[1] #my_list[start_index:], start=start_index
          for index2, item2 in enumerate(copy_no_overlap[index1+1:], start=index1+1):
              bounds2 = item2.split("-")
              lower2 = bounds2[0]
              upper2 = bounds2[1]
              print("Comparing: ", item1, " to ", item2)
              if item1 == item2:
                  continue
              if int(lower1) >= int(lower2) and int(upper1) <= int(upper2):
                print("Index1: Both bounds already in list: ", lower1, upper1)
                del copy_no_overlap[index1]
                index1 -= 1
                going = True
              elif int(lower2) >= int(lower1) and int(upper2) <= int(upper1):
                print("Index2: Both bounds already in list: ", lower2, upper2)
                del copy_no_overlap[index2]
                index2 -= 1
                going = True
              #lower bound in range
              elif int(upper1) >= int(lower2) >= int(lower1) and upper2 > upper1:
                  # low <= num <= high
                  # update item one to contain the bounds of item 2 and remove item 2
                  copy_no_overlap[index1] = f"{lower1}-{upper2}"
                  del copy_no_overlap[index2]
                  index2 -= 1
                  # IF we make a change, we need to re-check all ranges
                  # going = True
              #upper bound in range
              elif int(upper1) <= int(upper2) <= int(upper1) and lower2 < lower1:
                  # if only the upper bound is in the list
                  # update item one to contain the bounds of item 2 and remove item 2
                  copy_no_overlap[index1] = f"{lower2}-{upper1}"
                  copy_no_overlap.remove(item2)
                  # going = True
              #neither bound in range
              else:
                  continue
                  # going = False
      if copy_no_overlap == valid_range_no_overlap:
          going = False
      else:
          valid_range_no_overlap = copy_no_overlap.copy()
          going = True

with open(filename, "r") as file_object:
    for line in file_object:
        # Remove trailing newline characters and split the line
        if re.fullmatch(r'\s*\n', line):
            ingredients = True
            continue
        if not ingredients:
            # Looking at the valid ranges
            valid_ranges.append(line.strip()) # Split each character into a list
    # once we have all of the ranges, we want to find and count
    # the valid ranges since sometimes the ranges will overlap
    valid_range_no_overlap = valid_ranges.copy()
    check_itself()
    print ("Current valid ranges without overlap: ", valid_range_no_overlap)

    check_itself()
    print("Final valid ranges without overlap: ", valid_range_no_overlap)
    for ranges in valid_range_no_overlap:
        bounds = ranges.split("-")
        valid_ids += int(bounds[1]) - int(bounds[0]) + 1
    print("Number of valid ids: ", valid_ids)