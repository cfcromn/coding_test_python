import sys
input = sys.stdin.readline

n = int(input())
q = []
for i in range(n):
    s = input().strip().split()
    if s[0][0] == 'p':
        if s[0][1] == 'u':
            q.append(int(s[1]))
        else:
            if not q:
                print(-1)
            else:
                print(q[0])
                q.pop(0)
    elif s[0][0] == 's':
        print(len(q))
    elif s[0][0] == 'e':
        if not q:
            print(1)
        else:
            print(0)
    elif s[0][0] == 'f':
        if not q:
            print(-1)
        else:
            print(q[0])
    elif s[0][0] == 'b':
        if not q:
            print(-1)
        else:
            print(q[-1])