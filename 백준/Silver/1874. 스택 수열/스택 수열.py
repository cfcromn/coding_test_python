import sys
input = sys.stdin.readline

n = int(input())
stack = []
ans = []
check = True
cur = 1

for _ in range(n):
    k = int(input())
    while cur <= k:
        stack.append(cur)
        ans.append('+')
        cur += 1
    if stack and stack[-1] == k:
        stack.pop()
        ans.append('-')
    else:
        check = False
        break

if check == True:
    for i in ans:
        print(i)
else:
    print('NO')