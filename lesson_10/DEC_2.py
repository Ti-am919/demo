def add_text(func):

    def wrapper():
        print('before')
        func()
        print('after')

    return wrapper


def simple1():
    print('simple1')

simple1()

simple1 = add_text(simple1) # переназначаем функцию на встроенную, которая содержит в себе wrapper

print(simple1)