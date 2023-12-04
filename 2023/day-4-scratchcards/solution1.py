# Read the file
input_file = None
with open('input.txt', 'r') as file:
    # Read the contents of the file
    input_file = file.readlines()

# Format the input
cards_numbers = []
for line in input_file:
    numbers = line.split(': ')[1].split(' | ')
    numbers = [list(map(int, numbers[0].split())),
               list(map(int, numbers[1].split()))]
    cards_numbers.append(numbers)

# Sum the points of the winning numbers
total = 0
for winning_numbers, own_numbers in cards_numbers:
    n_winning_own_numbers = 0
    for winning_number in winning_numbers:
        if winning_number in own_numbers:
            n_winning_own_numbers += 1
    total += int(2**(n_winning_own_numbers-1))

print(total)
