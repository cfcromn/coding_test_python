import sys
input = sys.stdin.readline

n = int(input())
total = 0
for i in range(n):
    s = input()
    lst = []
    t = ''
    cnt = 1
    for j in s:
        if j not in lst:
            lst.append(j)
            t = j
        else:
            if t != j:
                cnt = 0
                break
            else:
                continue
    if cnt == 1:
        total += 1
print(total)