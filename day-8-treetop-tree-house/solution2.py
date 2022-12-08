import numpy as np

# Read file as a numpy array
with open('input.txt') as file:
    forest = np.array(list(map(lambda line: list(line), file.read().split('\n')[:-1]))).astype(int)

# Calculate the scenic score
def score(i, j, forest):
    cur_height = forest[i,j]
    score = 1
    for sight in [list(reversed(forest[:i,j])), forest[i+1:,j], list(reversed(forest[i,:j])), forest[i,j+1:]]:
        k = 0
        score_tmp = 0
        while len(sight) != k and sight[k] < cur_height:
            score_tmp += 1
            k += 1
        if len(sight) != k:
            score_tmp += 1
        score *= score_tmp
    return score
 
score_trees = list(map(lambda i: list(map(lambda j: score(i, j, forest), range(len(forest[0])))), range(len(forest))))

print(max(list(map(lambda x: max(x), score_trees))))
