import sys
input = sys.stdin.readline

n = input().strip()
nl = []
k = int(n[12])
a = 0
for i in range(0, len(n)-1):
    if n[i] == '*':
        if i % 2 == 0:
            continue
        else:
            a = 1
    elif i % 2 == 0:
            nl.append(int(n[i]))
    else:
            nl.append(int(n[i]) * 3)  
if a == 1:
    for i in range(10):
        if k == (10 - ((sum(nl) + i*3) % 10)) % 10:
            print(i)
            break
else:
    for i in range(10):
        if k == (10 - ((sum(nl) + i) % 10)) % 10:
            print(i)
            break 