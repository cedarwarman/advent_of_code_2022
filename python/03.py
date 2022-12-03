import pathlib
import string

# Reading in the file
f = open(pathlib.Path(__file__).resolve().parents[1] / "puzzle_input" / "puzzle_input_03.txt")

# Dictionary for scores
score_dict = {}
n = 1
for letter in string.ascii_lowercase[:26] + string.ascii_uppercase[:26]:
    score_dict[letter] = n
    n += 1

# The for loop
total_score = 0
for line in f:
    firsthalf, secondhalf = line[:len(line)//2], line[len(line)//2:]
    set_intersection = ''.join(set(firsthalf).intersection(secondhalf))
    score = score_dict[set_intersection]
    total_score += score

print("The total score for part 1 is: ", total_score)

# Part 2
f.seek(0)
total_score = 0
n = 1

# Going through the lines in groups of 3
line_1 = ""
line_2 = ""
line_3 = ""
for line in f:
    if n == 1:
        line_1 = line.strip()
        n += 1
    elif n == 2:
        line_2 = line.strip()
        n += 1
    else:
        line_3 = line.strip()
        # For every group of three, compare the sets
        set_intersection = set(line_1) & set(line_2) & set(line_3)
        total_score += int(score_dict[str(set_intersection)[2:3]])
        n = 1

print("The total score for part 2 is: ", total_score)






