def progression(limit=100):
    n = 2
    num = 1
    count = 1
    while count < limit:
        yield num
        num+=n
        count+=1

count = 1
for number in progression(10000):
    if count == 100:
        print(number)
        break
    count += 1
