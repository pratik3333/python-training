
def prefix_decorators(prefix):
    def decorater_function(original_function):
        def wrapper_funtion(*args, **kwargs):
            print(prefix, 'Executed Before', original_function.__name__)
            result = original_function(*args, **kwargs)
            print(prefix, 'Executed After function', original_function.__name__, '\n')
            return result

        return wrapper_funtion
    return decorater_function

@prefix_decorators('TESTING:')
def display_info(name,age):
    print(f'Display info ran with argument ({name},{age})')

display_info('John',32)
display_info('Corey',33)
display_info('Kunal',22)