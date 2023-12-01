# Open file separated by '\n' and remove last '\n'
with open('input.txt', 'r') as file:
    file = str(file.read()).split('\n')[:-1]

# Split each item in the list by ',' and by '-'
file = list(map(lambda x: list(map(lambda y: list(map(lambda z: int(z), y.split('-'))), x.split(','))), file))

# Order the each of pairs by the number in the sections to clean
file = list(map(lambda x: sorted(x, reverse=True) if x[0][0] == x[1][0] else sorted(x), file))

# Get witch sections contains the other one of the pair
file = list(map(lambda x: int(x[0][0] <= x[1][0] and x[0][1] >= x[1][1]), file))

print(sum(file))