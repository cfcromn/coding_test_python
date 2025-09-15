import sys
input = sys.stdin.readline

n = int(input())              
e = [input().strip() for i in range(n)]  
e = list(set(e))
e.sort()
e.sort(key=len)  

for i in e:
    print(i)