my_list = [1, 3, 2, 4, 5]

for idx1 in range(len(my_list)):
    for idx2 in range(idx1+1, len(my_list)):
        if my_list[idx1] > my_list[idx2] :
            my_list[idx1], my_list[idx2] = my_list[idx2], my_list[idx1]
    

print(my_list)