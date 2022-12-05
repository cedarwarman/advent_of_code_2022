import pathlib
import re

# Reading in the file
f = open(pathlib.Path(__file__).resolve().parents[1] / "puzzle_input" / "puzzle_input_05.txt")

# Reading in the first stacks (look for two newlines to stop)
stacks = [[] for x in range(9)]

for line in f:
    if line[1] == '1':
        break

    # Making a list of values for each stack
    y = 0
    for n in range(1, 34, 4):
        entry = line[n]
        if entry != ' ':
            stacks[y].insert(0, entry)
        y += 1

# Going through the main loop that moves the things
f.readline() # Blank line
for line in f:
    print(line)
    regex_results = re.findall("\s\d+", line)
    find_list = []
    for thing in regex_results:
        find_list.append(int(thing.strip()))
    print(find_list)

    # Doing the move(s)
    for z in range(find_list[0]):
        print(z)
        print(stacks[find_list[2] - 1])
        print(stacks[find_list[1] - 1])
        stacks[find_list[2] - 1].append(stacks[find_list[1] - 1].pop())
        print(stacks[find_list[2] - 1])
        print(stacks[find_list[1] - 1])

# Getting the answer from the last item in each stack
answer_string = ""
for stack in stacks:
    last_item = stack[-1]
    answer_string += last_item

print("Answer is: ", answer_string)
