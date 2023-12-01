import re

# Read the file
input = None
with open('input.txt', 'r') as file:
    # Read the contents of the file
    input = file.readlines()

total_value = 0
# Iterate over all the lines
for line in input:
    # Search with regex the numbers
    numbers = re.findall(r'[0-9]', line)
    # Add to the total the value to be found on each line
    total_value += int(numbers[0]) * 10 + int(numbers[-1])

print(total_value)
