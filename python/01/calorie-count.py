input = open("input.txt", "r")
lines = [line.strip() for line in input.readlines()]
#
counts = []
calories = 0

for line in lines:
    if line:
        calories += int(line)
    else:
        counts.append(calories)
        calories = 0

# part 1
print(max(counts))

# part 2
print(sum(sorted(counts, reverse=True)[:3]))