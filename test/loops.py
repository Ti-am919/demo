persons= {'john':155,'tom':173,'nate':124,'cody':198}

for person in persons.items():
    name,height = person
    print(f'{name},{height}')