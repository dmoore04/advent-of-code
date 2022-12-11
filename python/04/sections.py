input = open("input.txt", "r")
lines = input.readlines()
pairs = [line.strip().split(",") for line in lines]

def assignment_to_range(assignment):
    bounds = [int(x) for x in assignment.split("-")]
    return range(bounds[0], bounds[1] + 1)
    
# part 1
full_overlaps = 0
# part 2
overlapping_pairs = 0


for pair in pairs:
    ranges = [assignment_to_range(assignment) for assignment in pair]
    intersection = set(ranges[0]).intersection(set(ranges[1]))

    if(len(intersection) > 0):
        overlapping_pairs += 1

    if len(intersection) == min([len(range) for range in ranges]):
        full_overlaps += 1

print(full_overlaps)
print(overlapping_pairs)
    

