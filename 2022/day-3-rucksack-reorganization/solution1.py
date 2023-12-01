# Open file separated by '\n'
with open('input.txt', 'r') as file:
    file = str(file.read()).split('\n')

# Remove last '\n'
file = file[:-1]

# Split each item in the list in half
file = list(map(lambda x: [x[:(len(x)//2)], x[(len(x)//2):]], file))

# Check witch item appears in each pairs of lists
file = list(map(lambda x: ''.join(map(lambda y: y if y in set(x[1]) else '', set(x[0]))), file))

# Assign a value to ech letter
file = list(map(lambda x: ord(x)-64+26 if x.isupper() else ord(x)-96, file))

print(sum(file))