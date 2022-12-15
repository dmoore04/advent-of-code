input = open("input.txt", "r").read()

def find_marker(input: str, length: int= 4):
    for i in range(0, len(input[0:-length])):
        marker_end = i + length
        marker = input[i:marker_end]
        if len(set(marker)) == length:
            return marker_end
    return None
# part 1
print(find_marker(input))
# part 2
print(find_marker(input, 14))

