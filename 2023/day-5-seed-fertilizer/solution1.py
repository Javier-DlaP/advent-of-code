import re

# Read the file
input_file = None
with open('input.txt', 'r') as file:
    # Read the contents of the file
    input_file = file.read()

features = ['seeds', 'seed-to-soil map', 'soil-to-fertilizer map',
            'fertilizer-to-water map', 'water-to-light map',
            'light-to-temperature map', 'temperature-to-humidity map',
            'humidity-to-location map']

# Process the input
almanac = {}
for feature in features:
    pattern = re.compile('(?<='+feature+':)(\n?[0-9 ]*)*')
    data_feature = re.search(pattern, input_file).group().strip()
    data_feature = [[int(y) for y in x.split()] for x in data_feature.split('\n')]
    if not feature.__contains__('map'):
        data_feature = data_feature[0]
    almanac[feature] = data_feature

# Apply the maps to the seeds
locations = []
for seed in almanac['seeds']:
    for feature_maps in list(almanac.keys())[1:]:
        destination = None
        for map_range in almanac[feature_maps]:
            if seed in range(map_range[1], map_range[1] + map_range[2]):
                destination = map_range[0] + seed - map_range[1]
        if destination is None:
            destination = seed
        seed = destination
    locations.append(seed)

print(almanac)
print(locations)
print(min(locations))
