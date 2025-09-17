import sys
input = sys.stdin.readline

n = int(input())
count = 1
cp = 1
while n > cp:
    cp += 6 * count
    count += 1
print(count)