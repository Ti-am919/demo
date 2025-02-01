def file_open():

    with open('data.txt', 'r') as data_file:
        data = data_file.read()
    for line in data_file.readlines():
        yield line


for data_line in file_open():
    with open('data2.txt', 'a') as new_file:
        new_file.write(data_line)
