'''Import required modules'''
import json
import cv2
import numpy as np

overall = {
    'marks': {},
    'total': 0,
    'feedback': {}
}

def calc(i):
    img1 = cv2.cvtColor(cv2.imread(f'../plots/plot{i}.png'),cv2.COLOR_BGR2GRAY)
    img2 = cv2.cvtColor(cv2.imread(f'./plots/plot{i}.png'),cv2.COLOR_BGR2GRAY)
    res = cv2.absdiff(img1,img2)
    res = res.astype(np.uint8)
    return np.count_nonzero(res) * 100 / res.size

marks = {}

feedback = {}

for i in range(9):
    p = calc(i)
    if p < 30.0 and p != 0:
        marks[f'plot{i}'] = 1
        feedback[f'plot{i}'] = 'success'
    else:
        marks[f'plot{i}'] = 0
        feedback[f'plot{i}'] = 'failed'

# --------------------------- Record ---------------------------
overall['marks'] = marks
overall['total'] = sum(compo for compo in marks.values())
overall['feedback'] = feedback
print('------------------------- MARKS ------------------------------')
print(json.dumps(marks, indent=4))
print('----------------------- FEEDBACK -----------------------------')
print(json.dumps(feedback, indent=4))
print('--------------------------------------------------------------')
print(f'Total: {sum(compo for compo in marks.values())}/9')
print('--------------------------------------------------------------')
with open('../evaluate.json', 'w', encoding='utf-8') as f:
    json.dump(overall, f, indent=4)
