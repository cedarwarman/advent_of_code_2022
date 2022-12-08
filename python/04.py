import pathlib

# Reading in the file
f = open(pathlib.Path(__file__).resolve().parents[1] / "puzzle_input" / "puzzle_input_04.txt")

n = 0

for line in f:
    first_half = line.strip().split(sep=',')[0]
    first_range = range(int(first_half.split(sep='-')[0]), int(first_half.split(sep='-')[1]) + 1)
    second_half = line.strip().split(sep=',')[1]
    second_range = range(int(second_half.split(sep='-')[0]), int(second_half.split(sep='-')[1]) + 1)
    set_intersection = set(first_range) & set(second_range)
    print(line)
    print(set_intersection)
    if len(set_intersection) == len(first_range) or len(set_intersection) == len(second_range):
        print("Contained\n\n")
        n += 1

print("Total: ", n)

# Second half
f.seek(0)
n = 0

for line in f:
    first_half = line.strip().split(sep=',')[0]
    first_range = range(int(first_half.split(sep='-')[0]), int(first_half.split(sep='-')[1]) + 1)
    second_half = line.strip().split(sep=',')[1]
    second_range = range(int(second_half.split(sep='-')[0]), int(second_half.split(sep='-')[1]) + 1)
    set_intersection = set(first_range) & set(second_range)
    print(line)
    print(set_intersection)
    if len(set_intersection) > 0:
        print("Some intersection\n\n")
        n += 1

print("Total: ", n)
