# Open file separated by '\n' and ' '
with open('input.txt', 'r') as file:
    file = list(map(lambda x: x.split(' '), str(file.read()).split('\n')))

# Remove last '\n'
file = file[:-1]

# Create the data structure that helps us to store the data
dict_shape_oponent = {'A': 'Rock', 'B': 'Paper', 'C': 'Scissors'}
dict_shape_you = {'X': 'Rock', 'Y': 'Paper', 'Z': 'Scissors'}
dict_points_result = {'Win': 6, 'Tie': 3, 'Lose': 0}
dict_points_shape = {'Rock': 1, 'Paper': 2, 'Scissors': 3}
dict_win = {'Rock': 'Scissors', 'Paper': 'Rock', 'Scissors': 'Paper'}

# Function that returns the result of the game
def result(you, oponent):
    if you == oponent:
        return 'Tie'
    elif dict_win[you] == oponent:
        return 'Win'
    else:
        return 'Lose'

# Calculate the result of every match and the point for the shape played
result = list(map(lambda x: dict_points_result[result(dict_shape_you[x[1]], dict_shape_oponent[x[0]])] + \
                            dict_points_shape[dict_shape_you[x[1]]], file))

# Sum all the points
print(sum(result))