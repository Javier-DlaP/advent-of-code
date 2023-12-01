import queue
import numpy as np

# Open file
with open('input.txt', 'r') as file:
    file = (file.read())

# Get the stack of crates and the rearrange procedure
creates, rearranges = file.split('\n\n')

# Create the datastructures to be used
creates_values = np.array([list(x[1::4]) for x in creates.split('\n')][:-1])
creates = [queue.LifoQueue() for _ in range(len(creates_values[0]))]
for i, stack_values in enumerate(creates_values.T[:,::-1]):
    for create_value in stack_values:
        if create_value != ' ':
            creates[i].put(create_value)
            
rearranges = list(map(lambda x: (lambda y: {'action': y[0], 'crates': int(y[1]), y[2]: int(y[3]), y[4]: int(y[5])})(x.split(' ')), rearranges.split('\n')[:-1]))

# Move the crates
for rearrange in rearranges:
    for i in range(rearrange['crates']):
        creates[rearrange.get('to')-1].put(creates[rearrange.get('from')-1].get())

# Get the top create of each stack
for create in creates:
    if create.empty():
        print(' ', end='')
    else:
        print(create.get(), end='')
print()
