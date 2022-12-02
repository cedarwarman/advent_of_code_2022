# Leaving this here for the future, but I learned that I have to be logged in
# to see the puzzle input, so I'll download it to a local file and read it in.
# import requests
#
# for line in requests.get("https://adventofcode.com/2022/day/1/input"):
#     print(line)

import pathlib

# Reading in the file
f = open(pathlib.Path(__file__).resolve().parents[1] / "puzzle_input" / "puzzle_input_01.txt")

sum = 0
sums = []

for line in f:
    print(line)
    if line.strip():
        sum = sum + int(line.strip())
        print("Sum = ", sum)

    else:
        print("Found empty line, appending sum and resetting")
        sums.append(sum)
        sum = 0

print("Max is: ", max(sums))

