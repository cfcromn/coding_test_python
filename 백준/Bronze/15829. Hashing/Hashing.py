import sys
input = sys.stdin.readline

d = {chr(i + 96): i for i in range(1, 27)}

n = int(input())
a = input().strip()
total = 0
to = 1
MOD = 1234567891

for i in a:
    k = d[i]
    total = (total + k * to) % MOD
    to = (to * 31) % MOD
print(total)