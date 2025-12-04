# loop through each line in the file
# each line is a bank, find the twelve largest numbers and add them together.
# then add each of those totals together to get the final answer.

# NOTE: the numbers must go in order so if a number is 891121, to get the highest number its 9 and 2 -> 92

from unittest import case


filename = "/mnt/shares/h/adventofcode/day3/data.txt"
final_number = 0
overall_total  = 0
digit_num = 1

previous_index_one = 0
previous_index_two = 1
previous_index_three = 2
previous_index_four = 3
previous_index_five = 4
previous_index_six = 5
previous_index_seven = 6
previous_index_eight = 7
previous_index_nine = 8
previous_index_ten = 9
previous_index_eleven = 10
previous_index_twelve = 11

one_digit = 0
two_digit = 0
three_digit = 0
four_digit = 0
five_digit = 0
six_digit = 0
seven_digit = 0
eight_digit = 0
nine_digit = 0
ten_digit = 0
eleven_digit = 0
twelve_digit = 0

def update_digits(line, index, digit_start):
    global one_digit, two_digit, three_digit, four_digit, five_digit, six_digit
    global seven_digit, eight_digit, nine_digit, ten_digit, eleven_digit, twelve_digit
    global previous_index_one, previous_index_two, previous_index_three, previous_index_four
    global previous_index_five, previous_index_six, previous_index_seven, previous_index_eight
    global previous_index_nine, previous_index_ten, previous_index_eleven, previous_index_twelve
    
    if digit_start == 1:
        one_digit = line[index] # set this to the current number
        previous_index_one = index
        update_digits(line=line, index=index + 1, digit_start=2)
    elif digit_start == 2:
        two_digit = line[index] # set this to the next number
        previous_index_two = index
        update_digits(line=line, index=index + 1, digit_start=3)
    elif digit_start == 3:
        three_digit = line[index]
        previous_index_three = index
        update_digits(line=line, index=index + 1, digit_start=4)
    elif digit_start == 4:
        four_digit = line[index]
        previous_index_four = index
        update_digits(line=line, index=index + 1, digit_start=5)
    elif digit_start == 5:
        five_digit = line[index]
        previous_index_five = index
        update_digits(line=line, index=index + 1, digit_start=6)
    elif digit_start == 6:
        six_digit = line[index]
        previous_index_six = index
        update_digits(line=line, index=index + 1, digit_start=7)
    elif digit_start == 7:
        seven_digit = line[index]
        previous_index_seven = index
        update_digits(line=line, index=index + 1, digit_start=8)
    elif digit_start == 8:
        eight_digit = line[index]
        previous_index_eight = index
        update_digits(line=line, index=index + 1, digit_start=9)
    elif digit_start == 9:
        nine_digit = line[index]
        previous_index_nine = index
        update_digits(line=line, index=index + 1, digit_start=10)
    elif digit_start == 10:
        ten_digit = line[index]
        previous_index_ten = index
        update_digits(line=line, index=index + 1, digit_start=11)
    elif digit_start == 11:
        eleven_digit = line[index]
        previous_index_eleven = index
        update_digits(line=line, index=index + 1, digit_start=12)
    elif digit_start == 12:
        twelve_digit = line[index]
        previous_index_twelve = index

# Open the file using a 'with' statement for automatic closing
with open(filename, "r") as file_object:
    # Iterate through each line in the file object
    for line in file_object:
        line = line.strip()  # Remove any leading/trailing whitespace/newline characters

        one_digit = line[0] # Start with the first digit and so on
        two_digit = line[1]
        three_digit = line[2]
        four_digit = line[3]
        five_digit = line[4]
        six_digit = line[5]
        seven_digit = line[6]
        eight_digit = line[7]
        nine_digit = line[8]
        ten_digit = line[9]
        eleven_digit = line[10]
        twelve_digit = line[11]

        previous_index_one = 0
        previous_index_two = 1
        previous_index_three = 2
        previous_index_four = 3
        previous_index_five = 4
        previous_index_six = 5
        previous_index_seven = 6
        previous_index_eight = 7
        previous_index_nine = 8
        previous_index_ten = 9
        previous_index_eleven = 10
        previous_index_twelve = 11

          # Loop through each number in the list
        for index, digit_char in enumerate(line):
            length = len(line)
            num = int(digit_char)  # Convert the string to an integer

            # First digit, everything is set to the first possible number
            if index == 0:
                continue  # Skip the first digit since it's already assigned to tens_digit
            digit_num = 1
            while digit_num <= 12:
              
                match int(digit_num):
                  case 1:
                      if int(one_digit) < num and index <= length - 12: # increase the front digit and change the remaining digits
                          print("Update 1 digit from ", one_digit, " to ", num, " at index ", index)
                          update_digits(line, index, 1)
                  case 2:
                      if int(two_digit) < num and index <= length - 11: # only increase the 2s digit if the 1s digit doesn't change
                          #make sure that the current index is greater than the previous index of the one digit
                          if index > previous_index_one:
                            print("Update 2 digit from ", two_digit, " to ", num, " at index ", index)
                            update_digits(line, index, 2)
                  case 3:
                      if int(three_digit) < num and index <= length - 10: # only increase the 3s digit if the 2s digit doesn't change
                          #make sure that the current index is greater than the previous index of the one digit
                          if index > previous_index_two:
                            print("Update 3 digit from ", three_digit, " to ", num, " at index ", index)
                            update_digits(line, index, 3)
                  case 4:
                      if int(four_digit) < num and index <= length - 9: # only increase the 4s digit if the 3s digit doesn't change
                          #make sure that the current index is greater than the previous index of the one digit
                          if index > previous_index_three:
                            print("Update 4 digit from ", four_digit, " to ", num, " at index ", index)
                            update_digits(line, index, 4)
                  case 5:
                      if int(five_digit) < num and index <= length - 8: # only increase the 5s digit if the 4s digit doesn't change
                          if index > previous_index_four:
                            print("Update 5 digit from ", five_digit, " to ", num, " at index ", index)
                            update_digits(line, index, 5)
                  case 6:
                      if int(six_digit) < num and index <= length - 7: # only increase the 6s digit if the 5s digit doesn't change
                          if index > previous_index_five:
                            print("Update 6 digit from ", six_digit, " to ", num, " at index ", index)
                            update_digits(line, index, 6)
                  case 7:
                      if int(seven_digit) < num and index <= length - 6: # only increase the 7s digit if the 6s digit doesn't change
                          if index > previous_index_six:
                            print("Update 7 digit from ", seven_digit, " to ", num, " at index ", index)
                            update_digits(line, index, 7)
                  case 8:
                      if int(eight_digit) < num and index <= length - 5: # only increase the 8s digit if the 7s digit doesn't change
                          if index > previous_index_seven:
                            print("Update 8 digit from ", eight_digit, " to ", num, " at index ", index)
                            update_digits(line, index, 8)
                  case 9:
                      if int(nine_digit) < num and index <= length - 4: # only increase the 9s digit if the 8s digit doesn't change
                          if index > previous_index_eight:
                            print("Update 9 digit from ", nine_digit, " to ", num, " at index ", index)
                            update_digits(line, index, 9)
                  case 10:
                      if int(ten_digit) < num and index <= length - 3: # only increase the 10s digit if the 9s digit doesn't change
                          if index > previous_index_nine:
                            print("Update 10 digit from ", ten_digit, " to ", num, " at index ", index)
                            update_digits(line, index, 10)
                  case 11:
                      if int(eleven_digit) < num and index <= length - 2: # only increase the 11s digit if the 10s digit doesn't change
                          if index > previous_index_ten:
                            print("Update 11 digit from ", eleven_digit, " to ", num, " at index ", index)
                            update_digits(line, index, 11)
                  case 12:
                      # if index >= length - 12: # might increase the 12s digit if there are no more digits left
                      #     if int(twelve_digit) < num:
                      #       print("Update 12 digit from ", twelve_digit, " to ", num, " at index ", index)
                      #       twelve_digit = digit_char
                      if int(twelve_digit) < num and index <= length - 1: # only increase the 12s digit if the 11s digit doesn't change
                          if index > previous_index_eleven:
                            print("Update 12 digit from ", twelve_digit, " to ", num, " at index ", index)
                            update_digits(line, index, 12)
                digit_num += 1
        final_number = one_digit + two_digit + three_digit + four_digit + five_digit + six_digit + seven_digit + eight_digit + nine_digit + ten_digit + eleven_digit + twelve_digit
        overall_total += int(final_number) # Add all of the largest numbers together
        print("Final number for line ", line, " is: ", final_number)
print("Overall total is: ", overall_total)