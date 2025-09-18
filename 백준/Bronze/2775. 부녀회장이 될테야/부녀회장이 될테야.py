import sys
input = sys.stdin.readline

t = int(input())

for _ in range(t):
    k = int(input())
    n = int(input())
    fz = [x for x in range(1, n+1)]
    for i in range(1, k+1): 
        for j in range(1, n):
            fz[j] += fz[j-1]
    print(fz[-1])
