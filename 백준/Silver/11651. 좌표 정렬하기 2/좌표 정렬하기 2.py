import sys
input = sys.stdin.readline
xy = []
n = int(input())
for i in range(n):
    x, y = map(int, input().split())
    xy.append((y, x))

xy.sort()
for x, y in xy:
    print(y, x)