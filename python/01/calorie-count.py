input = open("input.txt", "r")
lines = input.readlines()

counts = []
temp = 0

for line in lines:
    if line.strip():
        temp += int(line.strip())
    else:
        counts.append(temp)
        temp = 0

# part 1
print(max(counts))

# part 2
print(sum(sorted(counts, reverse=True)[:3]))