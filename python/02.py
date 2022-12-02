import pathlib

# Reading in the file
f = open(pathlib.Path(__file__).resolve().parents[1] / "puzzle_input" / "puzzle_input_02.txt")

# Your total score is the sum of your scores for each round. The score for a
# single round is the score for the shape you selected (1 for Rock, 2 for
# Paper, and 3 for Scissors) plus the score for the outcome of the round (0
# if you lost, 3 if the round was a draw, and 6 if you won).

total_score = 0

for line in f:
    opponent = line.split()[0]
    you = line.split()[1]
    if opponent == "A":
        if you == "X":
            total_score += (1 + 3)
        if you == "Y":
            total_score += (2 + 6)
        if you == "Z":
            total_score += (3 + 0)
    if opponent == "B":
        if you == "X":
            total_score += (1 + 0)
        if you == "Y":
            total_score += (2 + 3)
        if you == "Z":
            total_score += (3 + 6)
    if opponent == "C":
        if you == "X":
            total_score += (1 + 6)
        if you == "Y":
            total_score += (2 + 0)
        if you == "Z":
            total_score += (3 + 3)

print("Totaly score is: ", total_score)

# Part 2
# "Anyway, the second column says how the round needs to end: X means you
# need to lose, Y means you need to end the round in a draw, and Z means
# you need to win. Good luck!"

f.seek(0)
total_score = 0

# I will start with the same structure to get the score, but I'll change
# the "you" variable based on the new rules.

for line in f:
    print("Doing line")
    opponent = line.split()[0]
    you = line.split()[1]
    # Figure out the "you" variable based on if I should win, lose, or tie
    if you == "X": # lose
        if opponent == "A":
            you = "Z"
        if opponent == "B":
            you = "X"
        if opponent == "C":
            you = "Y"
    elif you == "Y":  # tie
        if opponent == "A":
            you = "X"
        if opponent == "B":
            you = "Y"
        if opponent == "C":
            you = "Z"
    else:  # win
        if opponent == "A":
            you = "Y"
        if opponent == "B":
            you = "Z"
        if opponent == "C":
            you = "X"

    # This section stays the same
    print("Doing second part")
    if opponent == "A":
        if you == "X":
            total_score += (1 + 3)
        if you == "Y":
            total_score += (2 + 6)
        if you == "Z":
            total_score += (3 + 0)
    if opponent == "B":
        if you == "X":
            total_score += (1 + 0)
        if you == "Y":
            total_score += (2 + 3)
        if you == "Z":
            total_score += (3 + 6)
    if opponent == "C":
        if you == "X":
            total_score += (1 + 6)
        if you == "Y":
            total_score += (2 + 0)
        if you == "Z":
            total_score += (3 + 3)

    print(total_score)

print("Answer to second part is: ", total_score)