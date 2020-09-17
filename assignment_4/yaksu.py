val = int(input())
yaksu = []
for num in range(val):
    if val%(num+1) == 0:
        yaksu.append(num+1)
    
print(*yaksu, sep=' ')
