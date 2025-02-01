from abc import abstractmethod

class Group:
    school_name = 42
    director = 'Marivanna'
    pupils = True

    def __init__(self, pupils_count, group_lead):
        self.pupils_count = pupils_count
        self.group_lead = group_lead

    def study(self):
        print('read!')

    @abstractmethod
    def move(self):
        pass


class PrimaryGroup(Group):
    min_age = 6
    max_age = 11
    building_section = 'left'

    def __init__(self, pupils_count, group_lead, classroom):
        super().__init__(pupils_count, group_lead)
        self.classroom = classroom


    def move(self):
        print('run fast')


class HighGroup(Group):
    min_age = 15
    max_age = 18
    
    def move(self):
        print('go slowly')


First_A = PrimaryGroup(16, 'td', 202)
Nine_A = HighGroup(22, 'ar')
print(Nine_A.pupils)
print(Nine_A.max_age)
print(Nine_A.min_age)
print(Nine_A.director)
#print(Nine_A.building_section)


print(First_A.pupils)
print(First_A.max_age)
print(First_A.min_age)
print(First_A.director)
print(First_A.building_section)
First_A.move()
Nine_A.move()
print(Nine_A.group_lead)
print(First_A.classroom)