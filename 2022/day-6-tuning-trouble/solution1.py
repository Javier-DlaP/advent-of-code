# Open file 
with open('input.txt', 'r') as file:
    file = file.read()

# Get the first marker appearance
i = 0
while len(set(file[i:i+4])) != 4:
    i += 1

print(i+4)
