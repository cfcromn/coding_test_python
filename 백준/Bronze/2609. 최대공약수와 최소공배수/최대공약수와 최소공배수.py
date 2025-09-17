import sys
input = sys.stdin.readline

x, y = map(int, input().split())
x1, y1 = x, y
while y:
    x, y = y, x % y

a = x1 // x
b = y1 // x
print(x)
print(a*b*x)