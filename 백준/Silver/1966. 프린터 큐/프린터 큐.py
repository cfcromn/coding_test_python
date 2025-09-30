import sys
input = sys.stdin.readline

n = int(input())

for i in range(n):
    n, m = map(int, input().split())
    lstN = [i for i in range(1, n+1)]
    lst = list(map(int, input().split()))
    m = lstN[m]
    cnt = 0
    while True:
    
        if lst[0] == max(lst):
            a = lstN.pop(0)
            lst.pop(0)
            cnt +=1
            if a == m:
                print(cnt)
                break
        else:
            a = lstN.pop(0)
            b = lst.pop(0)
            lstN.append(a)
            lst.append(b)