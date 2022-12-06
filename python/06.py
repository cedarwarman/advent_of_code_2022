import pathlib

# Reading in the file
f = open(pathlib.Path(__file__).resolve().parents[1] / "puzzle_input" / "puzzle_input_06.txt")

print(f)

# Sliding window
# What is the total number of windows?

# Here's the indices of the first window
x = 0
y = 4
line = f.read()
print(line)
n = len(line) - 3
print(n)

while n > 0:
    window = line[x:y]
    print(window)
    if len("".join(set(window))) == 4:
        index = y
        print(index)
        break
    x += 1
    y += 1
    n -= 1

# Part 2
x = 0
y = 14
n = len(line) - 13
print(n)

while n > 0:
    window = line[x:y]
    print(window)
    if len("".join(set(window))) == 14:
        index = y
        print(index)
        break
    x += 1
    y += 1
    n -= 1

