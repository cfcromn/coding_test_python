w, b = map(int, input().split())

total = 0
for i in range(w):
    che = input()
    for j in range(b):
        if j % 2 == 0:
           if  che[j] == 'W' and che[j+1] != 'B' or che[j] == 'B' and che[j+1] != 'W':
               total += 1
print(total)              
