import re

# Return a string of digits only from alphanumeric input
# If there are no digits, return 0
def strip_non_numerals(input_string):
    stripped = ''.join(char for char in input_string if char.isdigit())
    return stripped if stripped else '0'

# Map words to digits
def word_to_digit(word):
    number_words = {
        'one': '1', 
        'two': '2', 
        'three': '3', 
        'four': '4', 
        'five': '5', 
        'six': '6', 
        'seven': '7', 
        'eight': '8', 
        'nine': '9'
    }
    return number_words.get(word, word)

# Given an input string, return the first either digit or spelled out word
def find_first_number(input_string):
    pattern = r'(one|two|three|four|five|six|seven|eight|nine|\d)'
    match = re.search(pattern, input_string)
    matches = re.findall(pattern, input_string)
    return word_to_digit(matches[0]) if match else None

# Given an input string, return the last either digit or spelled out word
# Reversed into a new string to catch and concatenated words like 'oneight'
def find_last_number(input_string):
    reversed_string = input_string[::-1]
    pattern = r'(?:\d|eno|owt|eerht|ruof|evif|xis|neves|thgie|enin)'  # Reversed pattern
    match = re.search(pattern, reversed_string)
    return word_to_digit(match.group()[::-1]) if match else None

# Return the sum of the calibration values of all the lines
def sum_calibration_values(filename):
    # open file for reading
    file = open(filename, 'r')
    # split file on newline into a list
    lines = file.read().split('\n')
    file.close()
    
    current_sum = 0

    # enumerate() will return an index and element
    for i, line in enumerate(lines):
        values = strip_non_numerals(line)
        # Add to sum: the first and last digit, concatenated together and casted to an int
        current_sum += int(values[0] + values[-1])

    return current_sum

# Return the sum of the calibration values of all the lines
def sum_calibration_values_part2(filename):
    # open file for reading
    file = open(filename, 'r')
    # split file on newline into a list
    lines = file.read().split('\n')
    file.close()
    
    current_sum = 0

    # enumerate() will return an index and element
    for i, line in enumerate(lines):
        # Add to sum: the first and last digit, concatenated together and casted to an int
        current_sum += int(find_first_number(line) + find_last_number(line))

    return current_sum


print("Day 01-1 Output: ", sum_calibration_values('input.txt'))
print("Day 01-2 Output: ", sum_calibration_values_part2('input.txt'))