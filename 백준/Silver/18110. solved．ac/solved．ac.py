import sys
input = sys.stdin.readline

n = int(input())
if n == 0:
    print(0)
    sys.exit()

cut = int(n * 0.15 + 0.5)

scores = [int(input()) for _ in range(n)]
scores.sort()

trim = scores[cut:n-cut]

den = n - 2*cut
total = sum(trim)

print((total + den//2) // den)
