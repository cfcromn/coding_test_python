import sys
input = sys.stdin.readline
def back(depth):
    if depth == m:
        print(*bt)
        return
    
    for i in range(1, n + 1):
        if visited[i]:
            continue
        if bt:
            if bt[-1] > i:
                continue
        bt.append(i)

        back(depth + 1)
        
        visited[i] = False
        bt.pop()

        
n, m = map(int, input().split())
visited = [False] * (n + 1)
bt = []
back(0)