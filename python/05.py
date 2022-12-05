import pathlib

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
            stacks[y].append(entry)
        y += 1

print(stacks)
