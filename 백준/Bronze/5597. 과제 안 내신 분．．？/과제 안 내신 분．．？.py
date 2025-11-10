import sys
input = sys.stdin.readline

b = [1] * 31
b[0] = 0
for _ in range(28):
    s = int(input().strip())
    b[s] = 0

for i in range(31):
    if b[i] == 1:
        print(i)