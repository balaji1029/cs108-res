'''
    Olympics Medals
    Author: Saksham Rathi
'''

from argparse import ArgumentParser as ap
import os

parser = ap()
parser.add_argument('--path', type=str, required = True)
args = parser.parse_args()

# dictionary for the data
totalData = {}

# looping through the directory
for fileName in os.listdir(args.path):
    with open(f"{args.path}/{fileName}", "r") as file:
        lines = [line.split("-") for line in file.readlines()]
    for line in lines:
        if line[0] not in totalData:
            totalData[line[0]] = [0, 0, 0]
        totalData[line[0]][0] += int(line[1])
        totalData[line[0]][1] += int(line[2])
        totalData[line[0]][2] += int(line[3])
    # read the file

    # loop through data of file and set the values for the data


# sort as per gold medals and break ties lexicographically
totalData = sorted(totalData.items(), key = lambda x: (-x[1][0], x[0]))
totalData = {k: v for k, v in totalData}
print(totalData)