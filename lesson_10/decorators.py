def func1(give_me_a_function):
    print('before')

    give_me_a_function()

    print('after')

def simple1():
    print('simple1')

def simple2():
    print('I')
    print('LOVE')
    print('PYTHON')

func1(simple1)
func1(simple2)
# Функция принимает на вход другую функцию