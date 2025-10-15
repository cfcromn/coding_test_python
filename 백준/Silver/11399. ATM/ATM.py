import sys
input = sys.stdin.readline

n = int(input())
p = sorted(list(map(int, input().split()))[:n])
s = []
s.append(p[0])

for i in range(1, len(p)):
    s.append(s[i - 1] + p[i])
print(sum(s))