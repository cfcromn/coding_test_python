import sys
input = sys.stdin.readline

def backtrack(end):
    for i in range(1, n+1):
        if end == m:
            print(*bt)
            return
        if i in bt:
            continue

        visited[i] = True
        bt.append(i)
        backtrack(end+1)
        visited[i] = False
        bt.pop()

n, m = map(int, input().split())
bt = []
visited = [False] * (n + 1)
backtrack(0)