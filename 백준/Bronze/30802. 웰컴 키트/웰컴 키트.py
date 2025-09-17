import sys
input = sys.stdin.readline

n = int(input())
t = sorted(list(map(int, input().split())))
a, b = map(int, input().split())
cnt = 0
for i in t:
    if i % a != 0:
        cnt +=1
    cnt += i // a
print(cnt)
print(n//b, n%b)