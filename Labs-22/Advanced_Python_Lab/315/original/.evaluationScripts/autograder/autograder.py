'''Import required modules'''
import json
import sys
import numpy as np
from main import *

overall = {
    'marks': {},
    'total': 0,
    'feedback': {}
}

marks = {}

feedback = {}

def check(i):
    global data
    out = sys.stdout
    sys.stdout = open('out.txt','w',encoding='utf-8')
    if i == 1:
        task1(data)
    elif i == 2:
        task2(data)
    elif i == 3:
        task3(data)
    elif i == 4:
        task4(data)
    elif i == 5:
        task5(data,2)
    file = open(f'./out/task{i}.txt','r',encoding='utf-8')
    sys.stdout = out
    if list(map(lambda x: x.strip(),file.readlines())) == list(map(lambda x: x.strip(),open('out.txt','r',encoding='utf-8').readlines())):
        if i == 1:
            marks[f'task{i}'] = 1
        elif i == 2:
            marks[f'task{i}'] = 2
        elif i == 3:
            marks[f'task{i}'] = 1
        elif i == 4:
            marks[f'task{i}'] = 2
        elif i == 5:
            marks[f'task{i}'] = 2
        feedback[f'task{i}'] = 'success'
    else:
        marks[f'task{i}'] = 0
        feedback[f'task{i}'] = 'failed'

data = np.genfromtxt('./data/matrix.csv',delimiter=',',dtype=int)
check(1)
check(2)
check(3)
check(4)
check(5)

# --------------------------- Record ---------------------------
overall['marks'] = marks
overall['total'] = sum(compo for compo in marks.values())
overall['feedback'] = feedback
print('------------------------- MARKS ------------------------------')
print(json.dumps(marks, indent=4))
print('----------------------- FEEDBACK -----------------------------')
print(json.dumps(feedback, indent=4))
print('--------------------------------------------------------------')
print(f'Total: {sum(compo for compo in marks.values())}/8')
print('--------------------------------------------------------------')
with open('../evaluate.json', 'w', encoding='utf-8') as f:
    json.dump(overall, f, indent=4)
