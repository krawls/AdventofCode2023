cubes = {
    'red': 12,
    'green': 13,
    'blue': 14
}

# Given a Game string, return dict (game id and red/green/blue values)
# With the color values corresponding the largest number of each color in the given input string
def most_colors(input_string):
    d = dict()
    d['game'] = int(input_string.split(':')[0].split()[1])
    d['red'] = 0
    d['green'] = 0
    d['blue'] = 0

    # split the pulled cubes on the ';' character
    for i, pull in enumerate(input_string.split(':')[1].split(';')):
        # this split token will be something like '5 red, 4 blue, 3 green'
        for j, cube in enumerate(pull.split(',')):
            # split again to get the individual components (number, color)
            individual_cubes = cube.strip().split()
            number = int(individual_cubes[0])
            color = individual_cubes[1]

            # this split token will be something like '8 green'
            # compare to dictionary of current game values to see if is greater 
            # if greater, replace with that number
            match color:
                case 'red':
                    if number > d['red']:
                        d['red'] = number
                case 'green':
                    if number > d['green']:
                        d['green'] = number
                case 'blue':
                    if number > d['blue']:
                        d['blue'] = number
    return d

# Given a Game string, return dict (game id and bool if game is possible) based on given cubes
# if any one instance of cubes is pulled that is > sample, then return false
def is_game_possible_with_replace(input_string):
    d = dict()
    d['game'] = int(input_string.split(':')[0].split()[1])
    d['result'] = True

    # split the pulled cubes on the ';' character
    for i, pull in enumerate(input_string.split(':')[1].split(';')):
        # this split token will be something like '5 red, 4 blue, 3 green'
        for j, cube in enumerate(pull.split(',')):
            # split again to get the individual components (number, color)
            individual_cubes = cube.strip().split()
            number = individual_cubes[0]
            color = individual_cubes[1]

            # this split token will be something like '8 green'
            # compare to dictionary of cubes to see if any are greater (thus, impossible)
            match color:
                case 'red':
                    if int(number) > int(cubes['red']):
                        d['result'] = False
                        return d
                case 'green':
                    if int(number) > int(cubes['green']):
                        d['result'] = False
                        return d
                case 'blue':
                    if int(number) > int(cubes['blue']):
                        d['result'] = False
                        return d
    return d

# Return the sum of the possible game ids  of all the lines without replacement
def sum_possible_games_part1(filename):
    # open file for reading
    file = open(filename, 'r')
    # split file on newline into a list
    lines = file.read().split('\n')
    file.close()
    
    current_sum = 0

    # enumerate() will return an index and element
    for i, line in enumerate(lines):
        d = is_game_possible_with_replace(line)
        # Add to sum
        if d['result']:
            current_sum += d['game']

    return current_sum

# Return the sum of the possible game ids  of all the lines
def sum_powers_part2(filename):
    # open file for reading
    file = open(filename, 'r')
    # split file on newline into a list
    lines = file.read().split('\n')
    file.close()
    
    current_sum = 0

    # enumerate() will return an index and element
    for i, line in enumerate(lines):
        # multiply the returned values in the dictionary, add the product to the 
        # running total
        d = most_colors(line)
        current_sum += int(d['red']) * int(d['green']) * int(d['blue'])

    return current_sum


print("Day 02-1 Output: ", sum_possible_games_part1('input.txt'))
print("Day 02-2 Output: ", sum_powers_part2('input.txt'))