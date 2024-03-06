'''Import required modules'''
import json
import os

overall = {
    'marks': {},
    'total': 0,
    'feedback': {}
}

marks = {}

feedback = {}

for i in range(2):
    os.system(f'python3 main.py --path data/testcase{i + 1}/ > out.txt')
    f1 = open(f'out/testcase{i + 1}.txt', 'r', encoding='utf-8').readlines()
    f2 = open('out.txt', 'r', encoding='utf-8').readlines()
    if f1 == f2:
        marks[f'testcase{i + 1}'] = 2
        feedback[f'testcase{i + 1}'] = 'success'
    else:
        marks[f'testcase{i + 1}'] = 0
        feedback[f'testcase{i + 1}'] = 'failed'
    os.system('rm out.txt')

# --------------------------- Record ---------------------------
overall['marks'] = marks
overall['total'] = sum(compo for compo in marks.values())
overall['feedback'] = feedback
print('------------------------- MARKS ------------------------------')
print(json.dumps(marks, indent=4))
print('----------------------- FEEDBACK -----------------------------')
print(json.dumps(feedback, indent=4))
print('--------------------------------------------------------------')
with open('../evaluate.json', 'w', encoding='utf-8') as f:
    json.dump(overall, f, indent=4)
