# Read the file and get every move to do
with open('input.txt') as file:
    moves = list(map(lambda x: (lambda y: (y[0], int(y[1])))(x.split(' ')), file.read().split('\n')[:-1]))

# Set the initial parameters
dif_pos_tail = set()
pos_head, pos_tail = [0,0], [0,0]

# Define the functions needed to simulate the rope
def move_head(pos_head, move):
    if move == 'U':
        pos_head[0] += 1
    elif move == 'R':
        pos_head[1] += 1
    elif move == 'D':
        pos_head[0] -= 1
    elif move == 'L':
        pos_head[1] -= 1
    else:
        raise Exception('Vector not implemented')
    return pos_head

def move_tail(pos_head, pos_tail, move):
    if abs(pos_head[0] - pos_tail[0]) <= 1 and abs(pos_head[1] - pos_tail[1]) <= 1: # Adjent
        return pos_tail
    else: # Need to move the tail
        if move == 'U':
            pos_tail[0], pos_tail[1] = pos_head[0]-1, pos_head[1]
        elif move == 'R':
            pos_tail[0], pos_tail[1] = pos_head[0], pos_head[1]-1
        elif move == 'D':
            pos_tail[0], pos_tail[1] = pos_head[0]+1, pos_head[1]
        elif move == 'L':
            pos_tail[0], pos_tail[1] = pos_head[0], pos_head[1]+1
        else:
            raise Exception('Vector not implemented')
        return pos_tail

# Move the rope and store every tail move
for move in moves:
    for _ in range(move[1]):
        pos_head = move_head(pos_head, move[0])
        pos_tail = move_tail(pos_head, pos_tail, move[0])
        dif_pos_tail.add(tuple(pos_tail))

print(len(dif_pos_tail))
