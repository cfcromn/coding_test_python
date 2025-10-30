s = input().strip()
result = [-1] * 26  

for i, ch in enumerate(s):
    idx = ord(ch) - ord('a')     
    if result[idx] == -1:       
        result[idx] = i

print(' '.join(map(str, result)))