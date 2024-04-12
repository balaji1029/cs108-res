s = input().strip()
perm = list(map(int, input().strip().split()))
if set(perm) != set(range(len(s))):
    print('INVALID INPUT')
    exit()
else:
    final = ''
    for i in perm:
        final += s[i]
    print(final)