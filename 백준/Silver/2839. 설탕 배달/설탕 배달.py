import sys
input = sys.stdin.readline


n = int(input())
m = 3
count = 0

while True:
    if n < 3:
        break
    if n % 5 == 0:
        m = 5
    n -= m
    count +=1

if n != 0:
    print(-1)
else:
    print(count)