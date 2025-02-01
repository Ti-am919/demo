class People:
    def __init__(self,name):
        self.name = name

    def get_name(self):
        return self.name.upper()

people1 = People("amir")

print(people1.get_name())




