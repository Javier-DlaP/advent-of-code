# Read the file
with open('input.txt') as file:
    instructions = list(map(lambda x: x.split(' '), file.read().split('\n')[:-1]))

# Calculate the state of the register in every cycle and the screen output
draw_pixel = lambda register, cycle: '#' if (cycle-1)%40+1 >= register and (cycle-1)%40+1 <= register+2 else '.'
register_history, screen_history = [], []
current_register, cycle = 1, 1
for instruction in instructions:
    if instruction[0] == 'noop':
        register_history.append(current_register)
        screen_history.append(draw_pixel(current_register, cycle))
        cycle += 1
        current_register = current_register
    elif instruction[0] == 'addx':
        register_history.append(current_register)
        screen_history.append(draw_pixel(current_register, cycle))
        cycle += 1
        current_register = current_register
        screen_history.append(draw_pixel(current_register, cycle))
        cycle += 1
        current_register = int(instruction[1]) + current_register
    else:
        raise Exception('Operation not implemented')
register_history.append(current_register)

# Visualize the screen
for i in range(int(len(screen_history)/40)):
    for pixel in screen_history[(i*40):(i*40)+40]:
        print(pixel, end='')
    print()

