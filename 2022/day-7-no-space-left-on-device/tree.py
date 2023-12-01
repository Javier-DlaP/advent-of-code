class FileSystem():

    def __init__(self, dir_name, prev_folder, depth=0):
        self.dir_name = dir_name
        self.size = None
        self.depth = depth
        self.prev_folder = prev_folder
        self.files = {}
        self.directories = {}

    def new_dir(self, dir_name):
        self.directories[dir_name] = FileSystem(dir_name, self, self.depth+1)

    def new_file(self, file_name, file_size):
        self.files[file_name] = {'size': int(file_size)}

    def cal_dir_size(self):
        size = 0
        for file_name in self.files.keys():
            size += self.files.get(file_name).get('size')
        for directory in list(self.directories.values()):
            directory.cal_dir_size()
            size += directory.size
        self.size = int(size)

    def __str__(self):
        string = ''
        string += ' '*((self.depth)*2) + '- ' + self.dir_name + ' (dir'
        if not self.size is None:
            string += ', size=' + str(self.size)
        string += ')\n'
        for directory in list(self.directories.values()):
            string += str(directory)
        for file_name in self.files.keys(): 
            string += ' '*((self.depth+1)*2) + '- ' + str(file_name) + ' (file, size=' + str(self.files.get(file_name).get('size')) + ')\n'
        return string

