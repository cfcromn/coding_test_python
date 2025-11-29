import sys
input = sys.stdin.readline


L, C = map(int, input().split())
password = sorted(list(input().split()))
bt = []
vo = set("aeiou")
con = set("bcdfghjklmnpqrstvwxyz")
vistied = [False] * (C + 1)
def secret(depth):
    if depth == L and bool(set(vo) & set(bt)) and len(set(con) & set(bt)) > 1:
        for i in range(L):
            print(bt[i], end = '')
        print()
        
    for i in range(C):
        if vistied[i]:
            continue
        if bt:
            if bt[-1] > password[i]:
                continue
        vistied[i] = True
        bt.append(password[i])

        secret(depth + 1)

        vistied[i] = False
        bt.pop()

secret(0)