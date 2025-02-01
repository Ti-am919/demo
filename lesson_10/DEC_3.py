def add_text(func):

    def wrapper():
        print('before')
        func()
        print('after')
    return wrapper

@add_text # вместо переназначения используем функцию декоратора 
def simple1():
    print('simple1')

@add_text
def simple2():
    print('simple2')

simple1()
simple2()