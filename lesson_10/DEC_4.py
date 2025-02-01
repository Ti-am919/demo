def add_logs(func):

    def wrapper():
        print(f'func {func.__name__} started')
        result = func()
        print(f'func {func.__name__} finished')
        return result
    
    return wrapper

@add_logs
def simple1():
    print('hello, world')

simple1()