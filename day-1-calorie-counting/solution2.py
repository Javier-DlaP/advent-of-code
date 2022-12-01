import os

# Open file separated by '\n\n' and store as a numpy array
with open('input.txt', 'r') as file:
    np_file = str(file.read()).split('\n\n')

# Remove last '\n'
np_file[-1] = np_file[-1][:-2]

# Get the max number of categories using map functions
top3_max_calories = sum(sorted(list(map(lambda x: sum([int(y) for y in str(x).split('\n')]), np_file)), reverse=True)[:3])

print(top3_max_calories)
