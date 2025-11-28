import sys
input = sys.stdin.readline

n = int(input())
for _ in range(n):
    t = 0
    m = int(input())
    win = [0]*(m+1)
    for i in range(1, m+1):
        w = int(input())
        win[i] = w
        t += w
    mx = max(win)
    f = win.index(mx)
    if win.count(mx) > 1:
        print("no winner")
    elif mx > t / 2:
        print(f"majority winner {f}")
    else:
        print(f"minority winner {f}")