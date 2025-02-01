my_list = [1, 2, 3, 4, 5]

def mult_by2(x):
    return x*2
new_list = map(mult_by2, my_list)
print(list(new_list))