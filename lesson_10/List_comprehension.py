my_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10] # список
# задача каждый элемент списка умножить на 2
new_list = []

# цикл for
#for x in my_list:
#    new_list.append(x*2)
#print(new_list)

#list comprehension
#new_list = [x * 2 for x in my_list]
#print(new_list)

# map lambda
new_list =list(map(lambda x: x*2,  my_list))
print(new_list)