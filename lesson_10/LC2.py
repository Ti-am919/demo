
my_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]


new_list2 = [x if x % 2 == 0 else print(f'{x} is not even') for x in my_list]

my_list = [1, 2, 3, 4, 5, 6, 7, 8, 10]
new_dict = {x: x * 3 for x in my_list}

print(new_dict)