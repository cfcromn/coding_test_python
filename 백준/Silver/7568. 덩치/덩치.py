import sys
input = sys.stdin.readline

n = int(input())
x = [0]*n
y = [0]*n
for i in range(n):
    x[i], y[i] = map(int, input().split())

r = []
for i in range(n):
    count = 1
    for j in range(n):
        if i == j:
            continue
        if x[i] < x[j] and y[i] < y[j]:
            count += 1
    r.append(count)
    
for i in r:
    print(i)