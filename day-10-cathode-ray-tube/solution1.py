# Read the file
with open('input.txt') as file:
    instructions = list(map(lambda x: x.split(' '), file.read().split('\n')[:-1]))

# Calculate the state of the register in every cycle
register_history = []
current_register = 1
for instruction in instructions:
    if instruction[0] == 'noop':
        register_history.append(current_register) 
        current_register = current_register
    elif instruction[0] == 'addx':
        register_history.append(current_register)
        register_history.append(current_register)
        current_register = int(instruction[1]) + current_register
    else:
        raise Exception('Operation not implemented')
register_history.append(current_register)

# Calculate the sum of signal strenghts
sum_signal_strenght = 0
for cycle in [20, 60, 100, 140, 180, 220]:
    sum_signal_strenght += register_history[cycle-1] * cycle

print(sum_signal_strenght)
