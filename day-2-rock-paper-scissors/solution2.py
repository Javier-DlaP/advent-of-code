# Open file separated by '\n' and ' '
with open('input.txt', 'r') as file:
    file = list(map(lambda x: x.split(' '), str(file.read()).split('\n')))

# Remove last '\n'
file = file[:-1]

# Create the data structure that helps us to store the data
dict_shape_oponent = {'A': 'Rock', 'B': 'Paper', 'C': 'Scissors'}
dict_result = {'X': 'Lose', 'Y': 'Tie', 'Z': 'Win'}
dict_points_result = {'Win': 6, 'Tie': 3, 'Lose': 0}
dict_points_shape = {'Rock': 1, 'Paper': 2, 'Scissors': 3}
dict_win = {'Rock': 'Scissors', 'Paper': 'Rock', 'Scissors': 'Paper'}

# Function that returns the shape that is going to be played
def shape_you(oponent, result_match):
    if result_match == 'Tie':
        return oponent
    elif result_match == 'Lose':
        return dict_win[oponent]
    else:
        return dict_win[dict_win[oponent]]

# Calculate the result of every match and the point for the shape played
result = list(map(lambda x: dict_points_result[dict_result[x[1]]] + \
                            dict_points_shape[shape_you(dict_shape_oponent[x[0]], dict_result[x[1]])], file))

# Sum all the points
print(sum(result))