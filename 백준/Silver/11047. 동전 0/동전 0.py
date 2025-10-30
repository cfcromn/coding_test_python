import sys
input = sys.stdin.readline

n, k= map(int, input().split())
w = []
for _ in range(n):
    i = int(input())
    w.append(i)
s = list(reversed(sorted(w)))
i = 0
cnt = 0
while k > 0:
    if k >= s[i]:
        k -= s[i]
        cnt += 1
    else:
        i += 1

print(cnt)