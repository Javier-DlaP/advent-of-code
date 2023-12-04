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

# Get the copies of each card
copies = [1] * len(cards_numbers)
for i, (winning_numbers, own_numbers) in enumerate(cards_numbers):
    n_winning_own_numbers = 0
    for winning_number in winning_numbers:
        if winning_number in own_numbers:
            n_winning_own_numbers += 1
    for j in range(1, n_winning_own_numbers + 1):
        k = j + i
        if k < len(copies):
            copies[k] += copies[i]

print(sum(copies))
