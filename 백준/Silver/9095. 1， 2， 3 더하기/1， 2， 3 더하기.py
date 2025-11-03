import sys
input = sys.stdin.readline

l = [1,1,2,4,7,13,24,44,81,149,274]
t = int(input())

for i in range(t):
    n = int(input())
    print(l[n])