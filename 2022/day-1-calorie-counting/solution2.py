# Open file separated by '\n\n'
with open('input.txt', 'r') as file:
    file = str(file.read()).split('\n\n')

# Remove last '\n'
file[-1] = file[-1][:-2]

# Get the max number of categories using map functions
top3_max_calories = sum(sorted(list(map(lambda x: sum([int(y) for y in str(x).split('\n')]), file)), reverse=True)[:3])

print(top3_max_calories)
