import sys
input = sys.stdin.readline

n, m = map(int, input().split())
d = {}
for i in range(n):
    s, p = input().split()
    d[s] = p

for i in range(m):
    s = input().strip()
    print(d[s])