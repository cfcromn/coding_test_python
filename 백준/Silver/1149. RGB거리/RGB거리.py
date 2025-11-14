import sys
input = sys.stdin.readline

n = int(input())
r, g, b = map(int, input().split())
for _ in range(n-1):
    r2, g2, b2 = map(int, input().split())
    r2 += min(g, b)
    g2 += min(r, b)
    b2 += min(g, r)
    r, g, b = r2, g2, b2

print(min(r,g,b))