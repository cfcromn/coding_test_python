import sys
input = sys.stdin.readline

n = int(input())
for i in range(1, n+1):
    t = i
    itotal = 0
    for j in str(i):
        itotal += int(j)
    if i == n:
        print(0)
        break
    if n == t + itotal:
        print(i)
        break