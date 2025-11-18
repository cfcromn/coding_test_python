import sys
input = sys.stdin.readline

n = int(input())
k = sorted([int(input()) for _ in range(n)])
maxlist = [0] * n
for i in range(len(k)):
    maxlist[i] = k[i] * (n - i)
print(max(maxlist))
    
