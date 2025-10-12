import sys
input = sys.stdin.readline

s = set()
n = int(input())

for _ in range(n):
    k = input().strip().split()

    if k[0][0] == 'a':
        if k[0][1] == 'd':
            s.add(int(k[1]))
        else:
            s = set(range(1, 21))
    elif k[0][0] == 'r':
        if int(k[1]) in s:
            s.remove(int(k[1]))
    elif k[0][0] == 'c':
        if int(k[1]) in s:
            print(1)
        else:
            print(0)
    elif k[0][0] == 't':
        if int(k[1]) in s:
            s.remove(int(k[1]))
        else:
            s.add(int(k[1]))
    elif k[0][0] == 'e':
        s = set()