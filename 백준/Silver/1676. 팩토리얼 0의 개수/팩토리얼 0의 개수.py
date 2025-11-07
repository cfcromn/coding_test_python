n = int(input())
p = 1
count = 0

for i in range(1, n+1):
    p *= i
p = str(p)

for i in p[::-1]:
    if i == '0':
        count +=1
    else:
        break
print(count)