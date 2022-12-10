input = open("input.txt", "r")
rucksacks = [line.strip() for line in input.readlines()]
# part 1
prio = 0

for rucksack in rucksacks:
    compartments = [rucksack[:len(rucksack) // 2], rucksack[len(rucksack) // 2:]]
    intersection = set(compartments[0]).intersection(set(compartments[1]))

    for char in intersection:
        prio += ord(char) - 96 if char.islower() else ord(char) - 38

print(prio)