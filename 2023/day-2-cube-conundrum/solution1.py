import re

BAG = {'red': 12, 'green': 13, 'blue': 14}

# Read the file
input = None
with open('input.txt', 'r') as file:
    # Read the contents of the file
    input = file.readlines()


def possible_game(line: str) -> int:
    game, sets = line.split(': ')
    game = int(game.replace('Game ', ''))
    for cube in BAG.items():
        pattern = re.compile('[0-9]+(?= '+cube[0]+')')
        cubes_type_used = re.findall(pattern, sets)
        for cube_type in cubes_type_used:
            if int(cube_type) > cube[1]:
                return 0
    return game


total = 0
for line in input:
    total += possible_game(line)
print(total)
