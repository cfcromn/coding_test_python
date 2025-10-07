import sys
input = sys.stdin.readline

n, m = map(int, input().split())
board = []
t = []

for _ in range(n):
    board.append(input())

for i in range(n - 7):
    for j in range(m - 7):
        a1 = 0  
        b1 = 0  
        for a in range(i, i + 8):
            for c in range(j, j + 8): 
                if (a - i + c - j) % 2 == 0:  
                    if board[a][c] != 'W':
                        a1 += 1
                    if board[a][c] != 'B':
                        b1 += 1
                else:                          
                    if board[a][c] != 'B':
                        a1 += 1
                    if board[a][c] != 'W':
                        b1 += 1
        t.append(min(a1, b1))

print(min(t))