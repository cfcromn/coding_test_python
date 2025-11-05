import sys
input = sys.stdin.readline

n = int(input())
nums = [int(input()) for i in range(n)]
nums.sort()
for i in nums:
    print(i)