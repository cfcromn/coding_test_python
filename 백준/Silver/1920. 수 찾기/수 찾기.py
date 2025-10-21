import sys
input = sys.stdin.readline
print = sys.stdout.write

n = int(input())
nl = set(map(int, input().split()))  

m = int(input())
ml = list(map(int, input().split()))

out = []
for x in ml:
    if x in nl:
        out.append("1\n")
    else:
        out.append("0\n")

print("".join(out))
