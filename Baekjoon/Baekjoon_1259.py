import sys

input = sys.stdin.readline

while True:
    n = input().strip()
    if n == '0':
        break
    reversed_n = ''.join(reversed(n))

    if n == reversed_n:
        print('yes')
    else:
        print('no')