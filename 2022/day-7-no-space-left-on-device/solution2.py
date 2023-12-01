from tree import FileSystem
import math

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

# Get the size of the smallest directory that would allow to have at least 30_000_000 of available size 
min_size_to_free = 30_000_000 - (70_000_000 - fs.size)
print(min_size_to_free)
def size_dir_to_rm(fs, min_size_to_free):
    fs_ptr = fs
    size_dir = math.inf 
    if fs_ptr.size >= min_size_to_free:
        size_dir = fs_ptr.size
    for directory in fs_ptr.directories.values():
        size_dir = min(size_dir, size_dir_to_rm(directory, min_size_to_free))
    return size_dir

print(fs)
print('The size of the smallest directory to remove is:', size_dir_to_rm(fs, min_size_to_free))
