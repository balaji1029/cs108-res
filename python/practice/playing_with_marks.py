file = open('buggy_marksheet.txt', 'r')

marks = list()

for line in file:
    name, mark = line.strip().split(' ')
    marks.append((list(map(str, name.split('_'))), mark))
marks = sorted(marks, key=lambda x: (int(x[0][2]), -int(x[1])))
for mark in marks:
    print('_'.join(mark[0]), mark[1])