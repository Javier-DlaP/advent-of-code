# Open file separated by '\n\n'
with open('input.txt', 'r') as file:
    file = str(file.read()).split('\n\n')

# Remove last '\n'
file[-1] = file[-1][:-2]

# Get the max number of categories using map functions
max_calories = max(list(map(lambda x: sum([int(y) for y in str(x).split('\n')]), file)))

print(max_calories)
