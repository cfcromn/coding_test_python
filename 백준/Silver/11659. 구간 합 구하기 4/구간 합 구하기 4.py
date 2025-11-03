import sys
input = sys.stdin.readline

n, m = map(int, input().split())
d = list(map(int, input().split()))

p = [0] * (n + 1)
for i in range(1, n + 1):
    p[i] = p[i - 1] + d[i - 1]
    
for i in range(m):
    g, g2 = map(int, input().split())
    print(p[g2] - p[g - 1])