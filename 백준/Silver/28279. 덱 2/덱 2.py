import sys
from collections import deque

input = sys.stdin.readline

n = int(input())
q = deque()
for i in range(n):
    m = input().split()
    if m[0] == '1':
        q.insert(0, m[1])
    elif m[0] == '2':
        q.append(m[1])
    elif m[0] == '3':
        if q:
            print(q.popleft())
        else:
            print(-1)
    elif m[0] == '4':
        if q:
            print(q.pop())
        else:
            print(-1)
    elif m[0] == '5':
        print(len(q))
    elif m[0] == '6':    
        if q:
            print(0)
        else:
            print(1)
    elif m[0] == '7':
        if q:
            print(q[0])
        else:
            print(-1)
    elif m[0] == '8':
        if q:
            print(q[-1])
        else:
            print(-1)