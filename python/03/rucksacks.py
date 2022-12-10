input = open("input.txt", "r")
rucksacks = [line.strip() for line in input.readlines()]
# part 1
prio = 0

def calculate_prio(char):
    return ord(char) - 96 if char.islower() else ord(char) - 38

for rucksack in rucksacks:
    compartments = [rucksack[:len(rucksack) // 2], rucksack[len(rucksack) // 2:]]
    intersection = set(compartments[0]).intersection(set(compartments[1]))
    prio += sum([calculate_prio(char) for char in intersection])

print(prio)

# part 2    
prio = 0
groups = [rucksacks[i:i + 3] for i in range(0, len(rucksacks), 3)]

for group in groups:
    intersection = set(group[0]).intersection(set(group[1]).intersection(set(group[2])))
    prio += sum([calculate_prio(char) for char in intersection])

print(prio)
