from tree import FileSystem

# Read file and split by '$' and '\n'
with open('input.txt', 'r') as file:
    file = list(map(lambda x: x.split('\n')[:-1], file.read().split('$ ')))[1:]

# Create a tree containing the filesystem
fs = FileSystem('/', None)
fs_creator = fs
for command_execution in file[1:]:
    command = command_execution[0].split(' ')
    if command[0] == 'cd':
        if command[1] == '..':
            fs_creator = fs_creator.prev_folder
        else:
            if not command[1] in fs_creator.directories.keys():
                fs_creator.new_dir(command[1])
            fs_creator = fs_creator.directories.get(command[1])
    elif command[0] == 'ls':
        for item in command_execution[1:]:
            output = item.split(' ')
            if output[0] == 'dir':
                fs_creator.new_dir(output[1])
            else:
                fs_creator.new_file(output[1], output[0])
    else:
        raise Exception('Command not implemented')

# Calculate the size of every folder
fs.cal_dir_size()

# Get the size of the folders with a size less than 100000
def sum_dir_less_100k(fs):
    fs_ptr = fs
    size_dirs = 0
    if fs_ptr.size <= 100000:
        size_dirs += fs_ptr.size
    for directory in fs_ptr.directories.values():
        size_dirs += sum_dir_less_100k(directory)
    return size_dirs

print(fs)
print('The sum of the directories with a size less than 100_000 is:', sum_dir_less_100k(fs))
