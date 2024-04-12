file = open('q1-test_input.txt', 'r')
output = open('q1-test_output.txt', 'w')
queries = list(map(int, file.read().strip('\n').split()))
# print(type(queries))
n = queries[0]
del queries[0]

a = [1,]*10
a[0] = 0
a[1] = 0
for i in range(2, 10):
    for j in range(2*i, 10, i):
        a[j] = 0
# print(a)

def getk(p):
    k = [2,]
    i = 1
    while i < len(p):
        # print(k)
        if p[i] == (p[i-1] + 2):
            k.append(p[i])
            k.append(p[i])
            i += 1
        else:
            k.append(p[i])
            i += 1
    return k

for i in range(n):
    if 10*queries[i] > (len(a)-1):
        a += [1,]*(10*queries[i]-len(a)+1)
        for j in range(2, len(a)):
            for k in range(2*j, len(a), j):
                a[k] = 0
        # output.write(str(a[queries[i]]) + '\n')
        p = list(filter(lambda x: a[x] == 1, range(2, len(a))))
        # print(p)
        k = getk(p)
        # print(k)
        # print(len(k), queries[i])
        output.write(str(k[queries[i]-1]) + '\n')
        # print(p)
    else:
        # output.write(str(a[queries[i]]) + '\n')
        p = list(filter(lambda x: a[x] == 1, range(2, len(a))))
        # print(p)
        k = getk(p)
        # print(len(k), queries[i])
        output.write(str(k[queries[i]-1]) + '\n')
        # print(p)
