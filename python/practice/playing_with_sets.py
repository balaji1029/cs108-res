file = open("q2-input.txt", "r")

sets = list()
for line in file:
    sets.append(set(map(int, line.strip().split(','))))

union = set()
for set in sets:
    union = union.union(set)
print(len(union))