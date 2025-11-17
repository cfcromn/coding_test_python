import sys
input = sys.stdin.readline

n = int(input())

for i in range(n):
    s = list(input().split())
    s1 = []
    while True:
        m = input().strip()
        if m == 'what does the fox say?':
            break
        m = list(m.split())
        if m[2] in s:
            s1.append(m[2])
    for i in s:
        if i not in s1:
            print(i, end=' ')