import sys
input = sys.stdin.readline

n, m = map(int, input().split())
dbj = set(input().strip() for _ in range(n)) & set(input().strip() for _ in range(m))
print(len(dbj))
for i in sorted(dbj):
    print(i)