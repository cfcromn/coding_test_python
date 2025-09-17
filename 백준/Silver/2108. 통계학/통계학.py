import sys
from collections import Counter
input = sys.stdin.readline

n = int(input())
nums = [int(input()) for _ in range(n)]
nums.sort()

print(round(sum(nums)/n))

print(nums[n//2])


cnt = Counter(nums)
count_list = sorted(cnt.items(), key=lambda x: (-x[1], x[0]))  

if len(count_list) == 1:                 
    print(count_list[0][0])
else:
    if count_list[0][1] != count_list[1][1]:
        print(count_list[0][0])          
    else:
        print(count_list[1][0])          

print(nums[-1] - nums[0])
