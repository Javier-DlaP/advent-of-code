import numpy as np

# Read file as a numpy array
with open('input.txt') as file:
    forest = np.array(list(map(lambda line: list(line), file.read().split('\n')[:-1]))).astype(int)

# Get the trees that are visible
def visible(i, j, forest):
    return sum(list(map(lambda x: x<forest[i,j], forest[:i,j]))) == len(forest[:i,j]) or \
           sum(list(map(lambda x: x<forest[i,j], forest[i+1:,j]))) == len(forest[i+1:,j]) or \
           sum(list(map(lambda x: x<forest[i,j], forest[i,:j]))) == len(forest[i,:j]) or \
           sum(list(map(lambda x: x<forest[i,j], forest[i,j+1:]))) == len(forest[i,j+1:]) 
 
visible_trees = list(map(lambda i: list(map(lambda j: visible(i, j, forest), range(len(forest[0])))), range(len(forest))))

print(sum(list(map(lambda x: sum(x), visible_trees))))
