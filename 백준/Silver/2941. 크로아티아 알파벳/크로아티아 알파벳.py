import sys
input = sys.stdin.readline

s = input().strip()
c = ['c=', 'c-', 'dz=', 'd-', 'lj', 'nj', 's=', 'z=']

for p in c:
    s = s.replace(p, '*') 

print(len(s))