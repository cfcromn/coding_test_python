import sys
input = sys.stdin.readline

stack = []
check = True
while True:
    s = input().rstrip('\n')
    if s == '.':
        break
    for i in s:
        if (i == ')' or i == ']') and not stack:
            check = False
            break
        if i == '(' or i == '[':
            stack.append(i)
        if i == ')':
            if stack[-1] != '(':
                check = False
                break
            else:
                stack.pop()
        if i == ']':
            if stack[-1] != '[':
                check = False
                break
            else:
                stack.pop()
    if check == False:
        print('no')
        stack = []
    elif not stack:
        print('yes')
    else:
        print('no')
        stack = []
    check = True      