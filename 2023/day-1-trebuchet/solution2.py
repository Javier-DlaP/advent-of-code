import re

dict_letters2number = {"one": 1, "two": 2, "three": 3, "four": 4, "five": 5,
                       "six": 6, "seven": 7, "eight": 8, "nine": 9}

# Read the file
input = None
with open('input.txt', 'r') as file:
    # Read the contents of the file
    input = file.readlines()

total_value = 0
# Iterate over all the lines
for line in input:
    first_letters, last_letters = [len(line), None], [0, None]
    for item in dict_letters2number.items():
        # Save the value of the max and min position of the first letter
        for x in re.finditer(item[0], line):
            if x.span()[0] < first_letters[0]:
                first_letters = [x.span()[0], item[1]]
            if x.span()[0] > last_letters[0]:
                last_letters = [x.span()[0], item[1]]

    list_line = list(line)
    if first_letters[1] is not None:
        list_line[first_letters[0]] = str(first_letters[1])
    if last_letters[1] is not None:
        list_line[last_letters[0]] = str(last_letters[1])
    line = "".join(list_line)
    # Search with regex the numbers
    numbers = re.findall(r'[0-9]', line)
    # Add to the total the value to be found on each line
    total_value += int(numbers[0]) * 10 + int(numbers[-1])

print(total_value)
