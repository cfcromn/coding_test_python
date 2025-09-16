import sys
input = sys.stdin.readline

n, k = map(int, input().split())

def p(a):
    result = 1
    for i in range(1, a+1):   
        result *= i
    return result


np = p(n)
kp = p(k)
kn = p(n-k)

print(np // (kn*kp))