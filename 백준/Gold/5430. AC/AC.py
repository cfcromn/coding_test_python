import sys
input = sys.stdin.readline
n = int(input())
for _ in range(n):
    cnt = 0
    RD = input().strip()
    m = int(input())
    lst = input().strip()[1:-1]
    new_list = [int(x) for x in lst.split(',') if x.strip()]

    if RD.count('D') > len(new_list):
        print('error')
        continue
            
    for i in range(len(RD)):
        if RD[i] == 'R':
            cnt += 1
        elif new_list:
            if cnt % 2 == 0:
                new_list.pop(0)
            else:
                new_list.pop(-1)

    if cnt % 2 == 1:
        new_list = list(reversed(new_list))

    print("[",end="")
    for i in range(len(new_list)):
        if i == len(new_list) - 1:
            print(new_list[i], end="")
        else:
            print(new_list[i], end =",")
    print("]")