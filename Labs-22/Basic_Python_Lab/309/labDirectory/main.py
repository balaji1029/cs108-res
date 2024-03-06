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
  fileName=args.path+fileName
  f=open(fileName,"r")
  for line in f.readlines():
    lineList=line.split("-")
    lineList[1]=int(lineList[1])
    lineList[2]=int(lineList[2])
    lineList[3]=int(lineList[3])
    if lineList[0] not in totalData.keys():
      totalData[lineList[0]]=[0,0,0]
    totalData[lineList[0]][0]+=lineList[1]
    totalData[lineList[0]][1]+=lineList[2]
    totalData[lineList[0]][2]+=lineList[3]
# sort as per gold medals and break ties lexicographically
sortedData=dict(sorted(totalData.items(), key=lambda x:(-x[1][0], x[0])))
print(sortedData)