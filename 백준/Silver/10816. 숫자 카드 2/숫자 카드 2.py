import sys
input = sys.stdin.readline

n = int(input())
n_list = list(map(int, input().split()))
m = int(input())
m_list = list(map(int, input().split()))

freq = {}
for x in n_list:
    freq[x] = freq.get(x, 0) + 1
  
out = [str(freq.get(q, 0)) for q in m_list]
print(' '.join(out))