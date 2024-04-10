'''
    Let's go to casino
    Author: Saksham Rathi
'''
import sys
large_num = 1000000007

if len(sys.argv) != 2 or not sys.argv[1].isnumeric():
    print("Invalid input")
    sys.exit()

# Please write your code in this file.
n = int(sys.argv[1])
values = [0, 1, 2, 3, 4, 5]
values = [1, 2, 4, 8, 16, 32]
if n < 6:
    print(values[n-1])
    sys.exit()

for i in range(6, n):
    values.append((values[i-1] + values[i-2] + values[i-3] + values[i-4] + values[i-5] + values[i-6])%large_num)

print(values[-1])