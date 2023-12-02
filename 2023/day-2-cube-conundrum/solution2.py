import re
import math

# Read the file
input = None
with open('input.txt', 'r') as file:
    # Read the contents of the file
    input = file.readlines()


def possible_game(line: str) -> int:
    game, sets = line.split(': ')
    game = int(game.replace('Game ', ''))
    max_cube = []
    for cube in ['red', 'green', 'blue']:
        pattern = re.compile('[0-9]+(?= '+cube[0]+')')
        cubes_type_used = list(map(int, re.findall(pattern, sets)))
        max_cube.append(max(cubes_type_used))
    return math.prod(max_cube)


total = 0
for line in input:
    total += possible_game(line)
print(total)
