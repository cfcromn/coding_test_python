import sys
input = sys.stdin.readline

n = int(input())
a = sorted(list(map(int, input().split())))
b = list(reversed(sorted(map(int, input().split()))))
t = 0
for i in range(n):
    t += a[i] * b[i]
print(t)