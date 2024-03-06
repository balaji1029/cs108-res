'''
    Olympics Medals
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

    # read the file

    # loop through data of file and set the values for the data


# sort as per gold medals and break ties lexicographically

