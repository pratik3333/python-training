

# def decorator_function(original_function):
#     def wrapper_function(*args,**kwargs):
#         print('wrapper executed this before {}'.format(original_function.__name__))
#         return original_function(*args,**kwargs)
#     return wrapper_function

class decorator_class(object):
    def __init__(self,original_function):
        self.original_function=original_function

    def __call__(self, *args, **kwargs):
        print(f'call method executed this befor {self.original_function.__name__}')
        return self.original_function(*args,**kwargs)

@decorator_class
def display():
    print('display function ran')

@decorator_class
def display_info(name,age):
    print(f'dispaly_info ran with arguments [{name} {age}]')
display_info('john',24)


display()