import re

input = open("input.txt", "r")
lines = input.readlines()

input_stacks = lines[:lines.index('\n')]
index_row = input_stacks.pop()

stacks = []

for i, char in enumerate(index_row):
    if char.isnumeric():
        stack = []
        for row in reversed(input_stacks):
            if row[i].isalpha():
                stack.append(row[i])
        stacks.append(stack)

input_instructions = lines[lines.index('\n') + 1:]

for instruction in input_instructions:
    x, start, end = [int(x) for x in re.findall(r'\d+', instruction)]
    for i in range(x):
        stacks[end-1].append(stacks[start-1].pop())
# part 1
print("".join([stack.pop() for stack in stacks]))
