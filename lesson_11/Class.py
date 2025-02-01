class Auto:
    def __init__(self):
        self.number = []

    def get_number(self):
        return "".join(self.number)

    def set_number(self, number):


        if len(number)!= 6:
            print('error')
        else:
            self.number = list(number)



auto1 = Auto()
auto2 = Auto()
auto1.set_number('a919aa')
auto2.set_number('k919ee')
print(auto2.get_number())
print(auto1.get_number())