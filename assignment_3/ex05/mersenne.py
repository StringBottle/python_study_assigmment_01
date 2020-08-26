var = int(input())

two_power_list = [2**n-1 for n in range(65)]

if var in two_power_list : 
    print('Yes')    
else :
    print('No')