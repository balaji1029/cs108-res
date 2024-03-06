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

with open('testcases.txt','r',encoding='utf-8') as f:
    i = 0
    for line in f:
        num = int(line)
        os.system(f'timeout 3s python3 main.py {num} > out.txt')
        f1 = open(f'out.txt','r',encoding='utf-8')
        f2 = open(f'out/{num}.txt','r',encoding='utf-8')
        if f1.readlines() == f2.readlines():
            marks[f'testcase{i + 1}'] = 1
            feedback[f'testcase{i + 1}'] = "success"
        else:
            marks[f'testcase{i + 1}'] = 0
            feedback[f'testcase{i + 1}'] = "failed"
        os.system('rm out.txt')
        i += 1

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
