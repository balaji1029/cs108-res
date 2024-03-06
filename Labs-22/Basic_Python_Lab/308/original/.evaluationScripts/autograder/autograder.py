'''Import required modules'''
from main import *
import json

overall = {
    'marks': {},
    'total': 0
}

marks = {
    'modulus': 0,
    'arg': 0,
    'abscissa': 0,
    'ordinate': 0,
    'distance': 0
}


# --------------------------- modulus ---------------------------

output = {}
with open('./test/modulus.txt', 'r', encoding='utf-8') as f:
    n = int(f.readline())
    for i in range(n):
        a, b = map(float, f.readline().split())
        try:
            output[i] = modulus(Complex(a, b))
        except:
            output[i] = -1

score = 0
with open('./test/out/modulus.txt', 'r', encoding='utf-8') as f:
    for i, o in output.items():
        if float(f.readline()) == o:
            score += 1

marks['modulus'] = 0.5 * score / len(output)

# --------------------------- arg ---------------------------

output = {}
with open('./test/arg.txt', 'r', encoding='utf-8') as f:
    n = int(f.readline())
    for i in range(n):
        a, b = map(float, f.readline().split())
        try:
            output[i] = arg(Complex(a, b))
        except:
            output[i] = -1

score = 0
with open('./test/out/arg.txt', 'r', encoding='utf-8') as f:
    for i, o in output.items():
        if float(f.readline()) == o:
            score += 1

marks['arg'] = 0.5 * score / len(output)

# --------------------------- abscissa ---------------------------

output = {}
with open('./test/abscissa.txt', 'r', encoding='utf-8') as f:
    n = int(f.readline())
    for i in range(n):
        a, b = map(float, f.readline().split())
        try:
            output[i] = abscissa(Polar(a, b))
        except:
            output[i] = -1

score = 0
with open('./test/out/abscissa.txt', 'r', encoding='utf-8') as f:
    for i, o in output.items():
        if float(f.readline()) == o:
            score += 1

marks['abscissa'] = 0.5 * score / len(output)

# --------------------------- ordinate ---------------------------

output = {}
with open('./test/ordinate.txt', 'r', encoding='utf-8') as f:
    n = int(f.readline())
    for i in range(n):
        a, b = map(float, f.readline().split())
        try:
            output[i] = ordinate(Polar(a, b))
        except:
            output[i] = -1

score = 0
with open('./test/out/ordinate.txt', 'r', encoding='utf-8') as f:
    for i, o in output.items():
        if float(f.readline()) == o:
            score += 1

marks['ordinate'] = 0.5 * score / len(output)

# --------------------------- distance ---------------------------

output = {}
with open('./test/distance.txt', 'r', encoding='utf-8') as f:
    n = int(f.readline())
    for i in range(n):
        a, b, c, d = map(float, f.readline().split())
        try:
            output[i] = distance(Complex(a, b), Complex(c, d))
        except:
            output[i] = -1

score = 0
with open('./test/out/distance.txt', 'r', encoding='utf-8') as f:
    for i, o in output.items():
        if f.readline().strip() == str(o):
            score += 1

marks['distance'] = 0.5 * score / len(output)

# --------------------------- Record ---------------------------
overall['marks'] = marks
overall['total'] = sum(compo for compo in marks.values())
print('------------------------- MARKS ------------------------------')
print(json.dumps(marks, indent=4))
print('--------------------------------------------------------------')
print(f'TOTAL: {sum(compo for compo in marks.values())}/2.5')
print('--------------------------------------------------------------')
with open('../evaluate.json', 'w', encoding='utf-8') as f:
    json.dump(overall, f, indent=4)
