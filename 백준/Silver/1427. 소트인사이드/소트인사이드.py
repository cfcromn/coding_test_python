import sys
input = sys.stdin.readline

n = input().strip()
lst = []
for i in n:
    lst.append(int(i))
l = list(reversed(sorted(lst)))
for i in l:
    print(i, end="")