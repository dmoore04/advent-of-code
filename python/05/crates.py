import re
import copy

input = open("input.txt", "r")
lines = input.readlines()

input_stacks = lines[:lines.index('\n')]
index_row = input_stacks.pop()

def build_stacks():
    stacks = []
    for i, char in enumerate(index_row):
        if char.isnumeric():
            stack = []
            for row in reversed(input_stacks):
                if row[i].isalpha():
                    stack.append(row[i])
            stacks.append(stack)
    return stacks

input_instructions = lines[lines.index('\n') + 1:]

# part 1
stacks_p1 = build_stacks()
for instruction in input_instructions:
    x, start, end = [int(x) for x in re.findall(r'\d+', instruction)]
    for i in range(x):
        stacks_p1[end-1].append(stacks_p1[start-1].pop())

print("".join([stack.pop() for stack in stacks_p1]))

# part 2
stacks_p2 = build_stacks()
for instruction in input_instructions:
    x, start, end = [int(x) for x in re.findall(r'\d+', instruction)]
    popped = []
    for i in range(x):
        popped.insert(0, stacks_p2[start-1].pop())
    stacks_p2[end-1].extend(popped)
        
print("".join([stack.pop() for stack in stacks_p2]))
