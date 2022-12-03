# Open file separated by '\n'
with open('input.txt', 'r') as file:
    file = str(file.read()).split('\n')

# Remove last '\n'
file = file[:-1]

# Check witch item appears in each pairs of lists
file_ = list(map(lambda x, y: ''.join(list(filter(lambda a: a is not None, set(map(lambda z: z if z in set(y) else None, set(x)))))), file[0::3], file[1::3]))

# Check the items with the third list
file = list(map(lambda x, y: list(filter(lambda a: a is not None, set(map(lambda z: z if z in set(y) else None, set(x)))))[0], file_, file[2::3]))

# Assign a value to ech letter
file = list(map(lambda x: ord(x)-64+26 if x.isupper() else ord(x)-96, file))

print(sum(file))