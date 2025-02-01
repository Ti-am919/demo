def add_logs(func):

    def wrapper(*args):
        print(f'func {func.__name__} started')
        result = func(*args)
        print(f'func {func.__name__} finished')
        return result
    return wrapper

@add_logs
def simple1():
    print('simple1')

@add_logs
def calc1(x):
    print(x*2)
@add_logs
def calc2(x, y):
    print(x*y)

simple1()
calc1(5)
calc2(5,5)