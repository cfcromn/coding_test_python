import sys
input = sys.stdin.readline

n = int(input())
stack = []
for i in range(n):
    s = input().strip().split()    
    if s[0][0] == 'p':
        if s[0][1] == 'u':
            stack.append(int(s[1]))
        else:
            if not stack:
                print(-1)
            else:
                print(stack.pop())
                
    elif s[0][0] == 's':
        print(len(stack))
    elif s[0][0] == 'e':
        if not stack:
            print(1)
        else:
            print(0)
    elif s[0][0] == 't':
        if not stack:
            print(-1)
        else:
            print(stack[-1])