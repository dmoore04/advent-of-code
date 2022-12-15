input = open("input.txt", "r").read()

def find_packet_marker(input):
    for i in range(0, len(input)-3):
        marker = input[i:i+4]
        if len(set(marker)) == 4:
            return i+4
    return None

print(find_packet_marker(input))

